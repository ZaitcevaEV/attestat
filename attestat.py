import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.concat([pd.Series(1, index=data.index, name='whoAmI_' + val) for val in data['whoAmI'].unique()], axis=1).fillna(0)

data = pd.concat([data, one_hot_data], axis=1)
data = data.drop('whoAmI', axis=1)

data.head()
