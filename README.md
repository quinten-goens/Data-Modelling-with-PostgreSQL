# Data Modeling with PostgreSQL<img align="right" width="25%" height="25%" src="https://fedingo.com/wp-content/uploads/2021/09/Python-PostgreSQL.jpg">

This project is part of the course **Relational Databases** in the **Data Engineering Nanodegree** on Udacity. The final version of the repository will be submitted to Udacity for review and grading.  

## Course Topics
- OLAP & OLTP Database Systems
- Normalization / Normal Forms
- Denormalization
- Fact and dimension tables
- Star and snowflake schemas 

## Project Context

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description

In this project, I applied what I've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, I needed to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.  

## Dependencies
- Pandas
- Psycopg2

## Files
- **create_tables.py**: Allows for the creation of the database tables.
- **sql_queries.py**: Contains all postgeSQL insert, create statements. 
- **etl.ipynb**: A notebook for testing purposes to test out SQL statements before running them on all files.
- **etl.py**: The code to process all the data and insert it in the tables by using the queries defined in sql_queries.py.
- **test.ipynb**: A notebook to check the contents of the database to validate whether the data is indeed correctly inserted.
- **LICENSE**: The project license.

## Usage
To use the code written to create the database and tables, use the following in a terminal.
```bash
python create_tables.py
```

To insert the data from the /data directory in the database use the following:
```bash
python etl.py
```

## Contributing
Pull requests to show improvements of the existing code are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
