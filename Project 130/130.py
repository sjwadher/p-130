import pandas as pd

df1 = pd.read_csv('Final_Final.csv')


del df1["Star_name"]

df1 = df1.dropna()


df1.to_csv('dfffff1.csv')





