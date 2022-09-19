import pandas as pd
import numpy as np
df = pd.read_csv("https://raw.githubusercontent.com/HS-KrE-ON/RecommendationSystem/jannik/archive/movie_titles.csv", encoding = "ISO-8859-1", on_bad_lines='skip')
df1 = df.head(3)
print(df1)

