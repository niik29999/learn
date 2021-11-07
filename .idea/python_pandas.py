import numpy as np
import pandas as pd
from numpy.random import randn

# Series
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'s':20,'x':30}

print(pd.Series(data=my_list))
print(pd.Series(data=my_list,index=labels))
print(pd.Series(data=arr))
print(pd.Series(data=arr,index=labels))
print(pd.Series(data=d))

ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])
print(ser1)
print(ser2)
print(ser1['USSR'])
print(ser1 + ser2)

# DataFrames
print('DataFrames')
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print(df['W'])
print(df[['W','Z']])
print(df.W)

df['new'] = df['W'] + df['Y']
print(df)

df.drop('new',axis=1,inplace=True)
print(df)

df.drop('E',axis=0,inplace=True)
print(df)

print(df.loc['A'])
print(df.iloc[2])
print(df.loc['B','Y'])
print(df.loc[['A','B'],['W','Y']])

# operations
print('operations')
booldf = df>0
print(df[booldf])
print(df[df>0])
print(df[df['W']>0])
print(df[df['W']>0]['Y'])
print(df[df['W']>0][['Y','X']])
print(df[(df['W']>0) & (df['Y'] < 0)])
print(df[(df['W']>0) | (df['Y'] < 0)])

# index
print('Index')
print(df.reset_index())

newind = 'CA NY WY OR'.split()
df['States'] = newind
print(df.set_index('States'))
df2 = df
df2.set_index('States',inplace=True)
print(df2)

# Index Levels
print('Index Levels')
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['A','B'])
print(df)
print(df.loc['G1'])
print(df.loc['G1'].loc[1])

df.index.names = ['Group','Num']
print(df)
print(df.xs('G1'))
print(df.xs(['G1',1]))
print(df.xs(1,level='Num'))

# Missing Data
print('Missing Data')
d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
print(df)
print(df.dropna())
print(df.dropna(axis=1))
print(df.fillna(value=0))
print(df.fillna(value=df.mean()))

# Groupby
print('Groupby')
data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)
print(df.groupby('Company').mean())
print(df.groupby('Company').min()[]
print(df.groupby('Company').count())
print(df.groupby('Company').describe())
print(df.groupby('Company').count().transpose())
print(df.groupby('Company').count().transpose()['FB'])

# Concatenating
print('Concatenating')
import pandas as pd
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],axis=1))

# Merging, Joining
left = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K2', 'K3'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# Merging
print('Merging')
print(pd.merge(left,right,how='inner',on='key1'))
print(pd.merge(left,right,how='inner',on=['key1', 'key2']))
print(pd.merge(left,right,how='left',on=['key1', 'key2']))
print(pd.merge(left,right,how='outer',on=['key1', 'key2']))

# Joining
print('Joining')
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

print(left.join(right))
print(left.join(right, how='outer'))

# Operations
print('Operations')
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyzw']})
print(df.head())
print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())
print(df[(df['col1']>2) & (df['col2']==444)])

def times2(x):
    return x*2

print(df['col2'].apply(times2))
print(df['col2'].apply(lambda x: x*2))
print(df['col3'].apply(len))
print(df['col2'].sum())
print(df.columns)
print(df.index)
print(df.sort_values(by='col2'))
print(df.isnull())

# pivot_table
print('pivot_table')
data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)
print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))

# Data Input and Output
### CSV Input
print('CSV')
df = pd.read_csv('E:\work\Python\deep_learning\example')
print(df)

### CSV Output
df.to_csv('E:\work\Python\deep_learning\example_out',index=False)

### Excel Input
print('Excel')
df = pd.read_excel('E:\work\Python\deep_learning\Excel_Sample.xlsx',sheet_name='Sheet1')
print(df)

### Excel Output
df.to_excel('E:\work\Python\deep_learning\Excel_Sample_Out.xlsx',sheet_name='Sheet1')

### HTML Input
# df = pd.read_html('https://ru.tradingview.com/screener/')
# print(df[0])

# SQL
# The key functions are:
#
# * read_sql_table(table_name, con[, schema, ...])
# * Read SQL database table into a DataFrame.
# * read_sql_query(sql, con[, index_col, ...])
# * Read SQL query into a DataFrame.
# * read_sql(sql, con[, index_col, ...])
# * Read SQL query or database table into a DataFrame.
# * DataFrame.to_sql(name, con[, flavor, ...])
# * Write records stored in a DataFrame to a SQL database.
print('SQL')
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
df.to_sql('data', engine)
sql_df = pd.read_sql('data',con=engine)
print(sql_df)

# изменение типа колонки
df_guide_tbl6_all=df_guide_tbl6_all.astype({'substance_code':str,'source': str})
