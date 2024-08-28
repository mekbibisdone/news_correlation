import re
import pandas as pd


def extract_domain(url):
    match = re.search(r"https?://(?:www\.)?([^/]+)", url)
    return match.group(1) if match else None


def count_country_mentions(text, countries):
    mention_counts = {country: 0 for country in countries}
    if pd.notnull(text):
        for country in countries:
            mention_counts[country] += len(
                re.findall(rf"\b{re.escape(country)}\b", text, flags=re.IGNORECASE)
            )
    return mention_counts
