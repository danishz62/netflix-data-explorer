import pandas as pd
import os
print(os.getcwd())
odf = pd.read_csv("e-commerce/OrderDetails.csv")
# print(odf.head())
# print(odf.info())
# print(odf.groupby('Category').sum())
odf1 = odf[["Category" , 'Quantity','Amount','Profit']].groupby('Category').sum()
ldf = pd.read_csv("e-commerce/ListofOrders.csv")
sdf = pd.read_csv("e-commerce/Salestarget.csv")

# print(sdf.head())
# print(odf.head())
# print(ldf.head())
odf2 = odf[["Order ID" , "Amount", 'Profit' , ] ].groupby('Order ID').sum().reset_index()
ldf2 = ldf[["Order ID", 'CustomerName' , 'State', 'City']].reset_index()

clist = pd.merge(ldf2, odf2, on = 'Order ID' , how = 'right')

bstc  = clist.loc[[clist["Amount"].idxmax()]]

dat = bstc[['Order ID' , 'CustomerName']]
print(clist.head(10))

print(f"Customer Of The Year Award Goes To {dat.values} With amount of shopping {bstc['Amount'].values}")


