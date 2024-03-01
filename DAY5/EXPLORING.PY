import pandas as pd

df = pd.read_csv("DAY5/results.csv")

# print(df.info())

# print(df.describe())

# std = how far away from the mean does the average variable sit

# print(df["home_score"].value_counts(normalize = True) * 100)

mask = df["home_score"] > 6

df = df[~mask]

print(df["home_score"].mean())