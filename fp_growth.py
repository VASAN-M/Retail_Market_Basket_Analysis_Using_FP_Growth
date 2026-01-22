

import pandas as pd
import numpy as np

df=pd.read_csv(r"/content/Market_Basket_Optimisation.csv")

df.info()

df.astype('string')

df.head(5)

from mlxtend.preprocessing import TransactionEncoder
te=TransactionEncoder()
tr_arr=te.fit_transform(df)
df=pd.DataFrame(tr_arr,columns=te.columns_)

df

from mlxtend.frequent_patterns import fpgrowth
fpgrowth(df,min_support=0.001)

