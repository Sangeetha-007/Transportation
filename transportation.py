import pandas as pd
import numpy as np

accident=pd.read_csv("/Users/sangeetha/Downloads/FARS2023NationalCSV/accident.csv")

print(accident)
#There were 37654 accidents in 2023

print(accident.isnull())

weather=pd.read_csv("/Users/sangeetha/Downloads/FARS2023NationalCSV/weather.csv")
