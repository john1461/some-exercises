import pandas as pd
df = pd.read_csv("https://github.com/rudeboybert/JSE_OkCupid/raw/master/profiles.csv.zip")
df[(df.orientation == 'gay') & (df.sex == 'f')]
