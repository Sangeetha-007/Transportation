import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

accident=pd.read_csv("/Users/sangeetha/Downloads/FARS2023NationalCSV/accident.csv")

print(accident)
#There were 37654 accidents in 2023

print(accident.isnull().sum())

state_counts= accident ['STATENAME'].value_counts().sort_values(ascending=False)
print(state_counts)

plt.figure(figsize=(12,6))
state_counts.plot(kind='bar')
plt.xlabel('State')
plt.ylabel('Number of Accidents')
plt.title('Number of Accidents by State in the US - 2023')
plt.tight_layout()
plt.show()

state_deaths=accident.groupby('STATENAME')['FATALS'].sum().sort_values(ascending=False)
print(state_deaths)

plt.figure(figsize=(12,6))
state_deaths.plot(kind='bar', color='red')
plt.xlabel('State')
plt.ylabel('Number of Casualities')
plt.title('Number of Deaths from a Car Accident in 2023')
plt.tight_layout()
plt.show()