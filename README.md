# Project: Data Modeling with PostgreSQL<img align="right" width="25%" height="25%" src="https://fedingo.com/wp-content/uploads/2021/09/Python-PostgreSQL.jpg">


This project is part of the Data Engineering Nanodegree on Udacity. The final version of the repository will be submitted to Udacity for review and grading.  

## Project Context

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description

In this project, I applied what I've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, I needed to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.  

## Dependencies
- Pandas
- Psycopg2

## Contributing
Pull requests to show improvements of th existing code are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
