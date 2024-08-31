import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("news_database.db")
cursor = conn.cursor()


# Fetch data from the tables
def fetch_data(query):
    return pd.read_sql_query(query, conn)


# Streamlit app
def main():
    st.title("News and Country Correlation Dashboard")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select a page:", ["News Correlation", "Country Correlation"]
    )

    if page == "News Correlation":
        st.header("News Correlation Statistics")

        # Fetch news_cor data
        news_cor_df = fetch_data("SELECT * FROM news_cor")

        # Display the dataframe
        st.dataframe(news_cor_df)

        # Plotting
        st.subheader("News Correlation Plots")
        if st.checkbox("Show mean sentiment plot"):
            fig, ax = plt.subplots()
            news_cor_df.plot(kind="bar", x="source_name", y="mean_sentiment", ax=ax)
            st.pyplot(fig)

        if st.checkbox("Show title content similarity plot"):
            fig, ax = plt.subplots()
            news_cor_df.plot(
                kind="bar", x="source_name", y="title_content_similarity", ax=ax
            )
            st.pyplot(fig)

    elif page == "Country Correlation":
        st.header("Country Correlation Statistics")

        # Fetch country_cor data
        country_cor_df = fetch_data("SELECT * FROM country_cor")

        # Display the dataframe
        st.dataframe(country_cor_df)

        # Top 10 and Bottom 10 by mention count
        top_10_df = country_cor_df[0:10]
        bottom_10_df = country_cor_df.nsmallest(10, "NumberOfMentions")

        # Plotting
        st.subheader("Top 10 Countries by Mention Count")
        if st.checkbox("Show top 10 mention count plot"):
            fig, ax = plt.subplots()
            top_10_df.plot(
                kind="bar",
                x="NumberOfMediaOrganizations",
                y="NumberOfMentions",
                ax=ax,
                color="blue",
            )
            ax.set_title("Top 10 Countries by Mention Count")
            st.pyplot(fig)

        st.subheader("Bottom 10 Countries by Mention Count")
        if st.checkbox("Show bottom 10 mention count plot"):
            fig, ax = plt.subplots()
            bottom_10_df.plot(
                kind="bar",
                x="NumberOfMediaOrganizations",
                y="NumberOfMentions",
                ax=ax,
                color="red",
            )
            ax.set_title("Bottom 10 Countries by Mention Count")
            st.pyplot(fig)


if __name__ == "__main__":
    main()
