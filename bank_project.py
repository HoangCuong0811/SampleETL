# Code for ETL operations on Country-GDP data

# Importing the required libraries
import pandas as pd
import numpy as np
import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime



def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a') as f: 
        f.write(f'{timestamp}: {message} \n')

def extract(url, table_atr):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')
    
    df = pd.DataFrame(columns=table_atr)
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')

    for row in rows: 
        col = row.find_all('td')
        if len(col) >= 3:  # Đảm bảo có ít nhất 3 cột
            bank_name = col[1].find_all('a')[-1].text.strip() if col[1].find_all('a') else col[1].text.strip()
            mc_value = col[2].text.strip().replace(',', '')  # Xóa dấu phẩy khỏi số

            data_dict = {'Name': bank_name, 'MC_USD_Billion': mc_value}
            df1 = pd.DataFrame([data_dict])
            df = pd.concat([df, df1], ignore_index=True)

    return df

def transform(df, exchange_rate_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    #doc du lieu tu phai exchange rate va chuyen thanh 1 dictionary
    exchange_rate_df = pd.read_csv(exchange_rate_path)
    exchange_rate = exchange_rate_df.set_index('Currency').to_dict()['Rate']

    #doi MC_USD_Billion sang dang float
    df['MC_USD_Billion'] = df['MC_USD_Billion'].astype(float)

    #transform du lieu theo exchange rate
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]

    return df
    


    

    return df

def load_to_csv(df, csv_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(csv_path, index = False)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists = 'replace', index = False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''\
    
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

url = 'https://web.archive.org/web/20230318102345/https://en.wikipedia.org/wiki/List_of_largest_banks'
exchange_rate_path = './BankProject/exchange_rate.csv'
log_file = './BankProject/code_log.txt'
table_atr = ['Name', 'MC_USD_Billion']
table_atr_final = ['Name', 'MC_USD_Billion', 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion', ]
db_name = './BankProject/Banks.db'
table_name = 'Largest_banks'
csv_path = './BankProject/Largest_banks_data.csv'

conn = sqlite3.connect(db_name)


# log_progress('Preliminaries complete. Initiating ETL process')
print(extract(url, table_atr))
log_progress("this is extract hahahaa")

df = extract(url, table_atr)

df = transform(df, exchange_rate_path)

# print(df['MC_EUR_Billion'][4])

# print(df[df['MC_EUR_Billion'] == df['MC_EUR_Billion'][4]])
load_to_csv(df, csv_path)

load_to_db(df, conn, table_name)

query = 'SELECT * FROM Largest_banks'
query_2 = "SELECT ROUND(AVG(MC_GBP_Billion),2) FROM Largest_banks"
query_3 = "SELECT Name,  from Largest_banks LIMIT 5"
run_query(query_2, conn)
