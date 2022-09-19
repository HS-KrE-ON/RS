"""Import von movie_titles"""
import pandas as pd
df = pd.read_csv(
    "https://raw.githubusercontent.com/HS-KrE-ON/RS/main/archive/movie_titles.csv",
                 encoding = "ISO-8859-1", on_bad_lines='skip')
df1 = df.head(3)
print(df1)
