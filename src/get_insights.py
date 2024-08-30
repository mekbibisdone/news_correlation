import pandas as pd
import sys
import os

rpath = os.path.abspath("..")

if rpath not in sys.path:
    sys.path.insert(0, rpath)
from src.loader import NewsDataLoader
from src.utils import count_country_mentions, extract_domain

# Get Data
ndl = NewsDataLoader("../data")
data = ndl.load_data()
domain = ndl.load_domain_location()
traffic = ndl.load_traffic()
similarity = ndl.load_title_content_similarity()

data["Domain"] = data["url"].map(extract_domain)
# Get insights

## number of articles
article_count = (
    data.groupby("source_name")
    .count()
    .reset_index()
    .loc[:, ["source_name", "article_id"]]
)
article_count.rename(columns={"article_id": "article_count"}, inplace=True)
## news organization traffic
data_traffic = data.merge(traffic, left_on="Domain", right_on="Domain")
data_traffic_unique_asc = (
    data_traffic.sort_values(by="GlobalRank", ascending=True)
    .drop_duplicates(subset="Domain")
    .reset_index(drop=True)
)
organization_traffic = data_traffic_unique_asc.loc[:, ["source_name", "GlobalRank"]]

## mean sentiment
sentiment_mapping = {"Positive": 1, "Neutral": 0, "Negative": -1}
data["Sentiment"] = data["title_sentiment"].map(sentiment_mapping)
sentiment_stats = (
    data.groupby("source_name")
    .agg(
        mean_sentiment=pd.NamedAgg(column="Sentiment", aggfunc="mean"),
    )
    .reset_index()
)
# title median word count
data["title_word_count"] = data["title"].map(lambda x: len(str(x).split()))

title_stats = (
    data.groupby("source_name")["title_word_count"]
    .agg(median_title_word_count="median")
    .reset_index()
)

# Merge insights
dfs = [
    article_count,
    organization_traffic,
    sentiment_stats,
    title_stats,
    similarity,
]


def get_news_insight():
    news_insight = dfs[0]
    for df in dfs[1:]:
        news_insight = pd.merge(news_insight, df, on="source_name")
    return news_insight


country_counts = (
    domain.groupby("Country")
    .count()
    .reset_index()
    .loc[:, ["Country", "SourceCommonName"]]
)
countries = domain["Country"].dropna().unique()
country_mentions = data["content"].map(lambda x: count_country_mentions(x, countries))


def get_country_insight():
    mentions = pd.DataFrame(country_mentions.tolist())
    total_mentions = mentions.sum().sort_values(ascending=False).reset_index()
    total_mentions.columns = ["Country", "NumberOfMentions"]
    country_organization_mention = pd.merge(
        total_mentions, country_counts, left_on="Country", right_on="Country"
    )
    country_organization_mention.columns = [
        "Country",
        "NumberOfMentions",
        "NumberOfMediaOrganizations",
    ]
    return country_organization_mention
