import pandas as pd

df = pd.read_csv("real_route_positions.csv", sep=';')


df = df.groupby('Timestamp').first()

print (df)

df.to_csv(r'fff2.csv', sep=';')