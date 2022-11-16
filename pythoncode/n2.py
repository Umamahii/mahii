import pandas as pd
data={'country':['Belgium','india','brazil'],
'capital':['Bass','newdelhi','brasillia'],
'population':[11234,34561,23456]}
df = pd.DataFrame(data,columns=['country','capital','population','street'])
print(df)