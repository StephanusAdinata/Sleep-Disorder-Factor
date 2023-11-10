#INTRODUCTION
#Nama : Stephanus Adinata Susanto
#Batch : SBY 001
#Objective : Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. Adapun dataset yang dipakai adalah dataset tentang faktor-faktor yang mempengaruhi seseorang terkena sleep disorder


import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)



def get_data():
    '''
    Fuction for Import Data from Postgres to Python
    '''
    conn_string="dbname='FTDS' host='localhost' user='postgres' password='------'" #Credential Password
    conn=db.connect(conn_string)

    df=pd.read_sql("select * from table_g7", conn)
    return df


def cleaning_data(cf):
    '''
    Fungsi untuk cleaning data
    '''
    df = cf.copy()

    df['Blood Pressure'] = df['Blood Pressure'].astype(str)
    df['BMI Category'] = df['BMI Category'].replace('Normal', 'Normal Weight')
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    return df

def save_data(df_clean):
    '''
    Fungsi untuk save data
    '''
    df_clean.to_csv(('P2G7_Stephanus_data_clean.csv'), index=False)


def import_data(df_clean):
    '''
    Fungsi untuk import data ke Kibana
    '''
    es = Elasticsearch("http://localhost:9200")
    for i,r in df_clean.iterrows():
        doc=r.to_json()
        res=es.index(index="data1_gc7", body=doc)


if __name__ == "__main__":
    df = get_data()
    df_clean = cleaning_data(df)
    save_data(df_clean)
    import_data(df_clean)
    print("complete")