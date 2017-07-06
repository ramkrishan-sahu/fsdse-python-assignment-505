import pandas as pd
import numpy as np
import re

def load_data():
    global df
    # df = pd.read_csv("./files/olympics.csv")
    df = pd.read_csv("./files/olympics.csv", skiprows=1)
    df = df.rename(columns={'01 !': 'Gold', '02 !': 'Silver', "03 !": "Bronze",
                            '01 !.1': 'Gold_W', '02 !.1': 'Silver_W', "03 !.1": "Bronze_W",
                            '01 !.2': 'Gold_T', '02 !.2': 'Silver_T', "03 !.2": "Bronze_T"})
    df['country'], df['count'] = df['Unnamed: 0'].str.split("\xc2\xa0", 1).str
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.index = df['country'].str[:] # the [0] element is the country name (new index)
    df.drop("country", axis=1, inplace=True)
    df = df.drop('Totals')
    return df

def first_country(df):
    return df.iloc[0]

def gold_medal(df):
    x = df["Gold"]
    return x.sort_values(ascending = False).index[0]

def biggest_difference_in_gold_medal(df):
    x = df.Gold
    y = df["Gold_W"]
    z = x - y
    return z.sort_values(ascending = False).index[0]

def get_points(df):
    Points = df['Gold_T'] * 3 + df['Silver_T'] * 2 + df['Bronze_T'] * 1
    df["Points"] = Points
    return df.Points


# df = load_data()
# print(first_country(df)["# Summer"])
# print(gold_medal(df))
# print(biggest_difference_in_gold_medal(df))
# print(get_points(df))
