import pandas as pd

df = pd.read_csv("measured_track_example.csv", sep=';')

#df = df[['Timestamp', 'Wifi_RP1', 'Wifi_RP2', 'Wifi_RP3','Wifi_RP4', 'Wifi_RP5']]

df = df.groupby('Timestamp').first()

print (df)

df.to_csv(r'fff2.csv', sep=';')