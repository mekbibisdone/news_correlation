import sqlite3
import os
import sys

rpath = os.path.abspath("..")

if rpath not in sys.path:
    sys.path.insert(0, rpath)

from src.get_insights import get_news_insight, get_country_insight


db_path = "../news_database.db"


# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the `news_cor` table if it doesn't already exist
create_table_query = """
CREATE TABLE IF NOT EXISTS news_cor (
    organization_name TEXT PRIMARY KEY,
    article_count INTEGER,
    GlobalRank INTEGER,
    mean_sentiment REAL,
    median_title_word_count INTEGER,
    title_content_similarity REAL
);
"""
cursor.execute(create_table_query)

create_country_table_query = """
CREATE TABLE IF NOT EXISTS country_cor (
    country TEXT PRIMARY KEY,
    organization_count INTEGER,
    mention_count INTEGER
);
"""
cursor.execute(create_country_table_query)

# Get the data
news_cor = get_news_insight()
country_cor = get_country_insight()
# Insert data into the table
news_cor.to_sql("news_cor", conn, if_exists="replace", index=False)
country_cor.to_sql("country_cor", conn, if_exists="replace", index=False)
# Commit the transaction and close the connection
conn.commit()
conn.close()
