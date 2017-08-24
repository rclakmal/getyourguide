import pandas as pd
data = pd.read_csv("data.csv")
position = data.groupby('Company', as_index=False)['Position'].mean()
ctr = data.groupby('Company', as_index=False)['CTR'].mean()
revenue =  data.groupby('Company', as_index=False)['Revenue'].mean()
impressions = data.groupby('Company', as_index=False)['Impressions'].mean()
cost = data.groupby('Company', as_index=False)['Cost'].mean()

result = position.merge(ctr, on='Company').merge(revenue, on='Company').merge(impressions, on='Company').merge(cost, on='Company')
result['SEM'] = result['CTR']*result['Impressions']*result['Position']* (result['Revenue']/result['Cost'])
result.sort_values('SEM',  ascending=False)
result.to_csv("result.csv", sep='\t')
