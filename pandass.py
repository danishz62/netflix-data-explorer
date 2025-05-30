import pandas as pd
df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
    