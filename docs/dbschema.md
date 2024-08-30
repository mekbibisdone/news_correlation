Project news_data {
database_type: 'PostgreSQL'
Note:'This database contain infromation about the correlation of many factors and their news ranking. There are also other insights related to news article.'
}

Table news_cor {
organization_name string [primary key]
article_count integer
GlobalRank integer
mean_sentiment float
median_title_word_count integer
title_content_similarity float
}

Table country_cor {
country string [primary key]
organization_count number
mention_count number
}
