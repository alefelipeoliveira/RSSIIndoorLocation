import pandas as pd

df = pd.read_csv("fingerprinting_data.csv", sep=';')

#df = df[['Timestamp', 'Wifi_RP1', 'Wifi_RP2', 'Wifi_RP3','Wifi_RP4', 'Wifi_RP5']]

df = df.groupby('Cell_number').mean()

print (df)

df.to_csv(r'fff3.csv', sep=';')