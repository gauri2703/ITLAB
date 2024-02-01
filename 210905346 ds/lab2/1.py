import pandas as pd
import numpy as np

df = pd.read_csv('wine_for_Week2.xls', header=None)

print(df.head())
print(df.tail())
print(df.index())
