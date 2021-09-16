import pandas as pd
import numpy as np

data = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
plot_df = data[["Mortality rate, infant (per 1,000 live births)",
               "GDP per capita (constant 2010 US$)", "Country Name"]]

print(plot_df.plot(x=0, y=1, kind='scatter',
      xlabel="Mortality rate", ylabel="GDP"))
