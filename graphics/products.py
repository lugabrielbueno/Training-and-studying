import pandas as pd
import seaborn as sns
from collections import Counter

prod = pd.read_csv('olist_products_dataset.csv')

fig = sns.mpl.pyplot.figure(None,(10,8))
xx = pd.value_counts(prod['product_category_name'])
sns.mpl.pyplot.title('Best-selling products between 2016-2018 by Olist',fontsize= 20)

amount = [xx[0],xx[1],xx[2],xx[3],xx[4],xx[5],xx[6],xx[7],xx[8],xx[9]]

produc = ['housewear',
'sports and leisure',
'furniture and decoration',
'health and beauty',
'housewares',
'automotive',
'computers accessories',
'toys',
'watches and gifts',
'telephony' ]
sns.barplot(y=amount,x = produc, palette= 'rainbow')
sns.mpl.pyplot.grid()
fig.autofmt_xdate()
sns.mpl.pyplot.ylabel('Orders',fontsize = 16)
sns.mpl.pyplot.show()