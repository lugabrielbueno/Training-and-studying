import pandas as pd
import seaborn as sns

client = pd.read_csv('olist_customers_dataset.csv')
seller = pd.read_csv('olist_sellers_dataset.csv')

fig3 = sns.mpl.pyplot.figure(None,(11,9))
fig3.suptitle('E-commerce customers and sellers in brazil by state', fontsize=20)
fig3.add_subplot(2,1,1)
fig3.autofmt_xdate()
sns.countplot(client['customer_state'],color = 'orange',alpha = 0.8)
sns.mpl.pyplot.ylim(0,15000)
sns.mpl.pyplot.xlabel("State",fontsize=16)
sns.mpl.pyplot.ylabel('Count',fontsize = 16)
sns.mpl.pyplot.legend(['Customers'])

fig3.add_subplot(2,1,2)
fig3.autofmt_xdate()
sns.countplot(seller['seller_state'],color = 'purple',alpha = .8)
sns.mpl.pyplot.ylim(0,600)
sns.mpl.pyplot.xlabel("State",fontsize=16)
sns.mpl.pyplot.ylabel('Count',fontsize = 16)
sns.mpl.pyplot.legend(['Sellers'])

sns.mpl.pyplot.show()