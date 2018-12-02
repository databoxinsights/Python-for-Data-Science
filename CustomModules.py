
# Author: Davis Vickers
# CreatedOn: 12/1/2018
# Purpose: Create reusable methods to call in ML & data analysis models within Python scripts. 
# import required libraries

import pymssql
import pandas

def get_sql_info(): 
    """ requires server, and db info which will be stored and used within the read_sql_from_file() method. 
    """
    server = input("ServerName:")
    db = input("Database:")
    return server, db

def sql_file_path(filename):
    """This function read read the SQL file script and return as a string object."""
    ## reading the sql file and then put results into data frame
    with open(filename) as file:
        sql = file.read()
    return sql

def read_sql_from_file(sqlQuery, server, db):
    
    """
    Creates an connection to the SQL server and executes a SQL query based on the 
    file you pass in. 
	
	- sqlQuery: Pass a literal SQL query, or read from file. Best used when calling the 
	  sql_file_path() method if reading SQL from a .sql or .txt file. 
	- server: Enter the server name. Can callthe get_SQL_info() method if preferred
	- db: Enter the database name on the server. Can also use the get_SQL_info() method. 
    
    """

    #Provide windows authentication, server and database info to run the SQL query
    #uid, pwd = get_credentials()
    #server, db = server, db
    
    #Establish the connection to SQl server based on get_SQL_info() return values
    conn = pymssql.connect(
    server = server, 
    database = db)
    
    # use pymssql to establish cursuor and return SQL results into Pandas Dataframe
    cursor = conn.cursor(as_dict = True)
    cursor.execute(sqlQuery)
    query = cursor.fetchall()
    query = pandas.DataFrame(query)
    
    return query

