import pandas as pd
df = pd.read_csv('online-retail.csv')
df.head()
print(df)
df['LinePrice'] = df['Quantity']*df['UnitPrice']
df.head()
print(df)

df_customers = df.groupby('CustomerID').agg(
                orders=('InvoiceNo', 'nunique'),
                skus = ('StockCode','nunique'),
                Quantity=('Quantity','sum'),
                revenue = ('LinePrice','sum'),
).reset_index()
df_customers.head()
print(df_customers)