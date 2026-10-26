# A função do Pandas é ler o CSV e transforma-lo em dataframe
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data.csv')
profile = ProfileReport(df, title='Profiling Report')
profile.to_file("output.html")