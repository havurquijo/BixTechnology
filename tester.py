from localFilter import isRemovable
import numpy as np
import pandas as pd

df = pd.read_csv("air_system_previous_years.csv",dtype=object)
df = df.replace("na",np.nan)
class_ = df.iloc[:,0]
data_ = df.iloc[:,1:]
base = data_.apply(pd.to_numeric)

print(isRemovable(base.ae_000,10)==True)
