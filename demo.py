from sklearn.linear_model import 1.linearRegression
import pandas as pd
data={
    'size':[800,1000,1200,1500],
    'bedrooms':[2,2,3,3],
    'price':[240000,280000,360000,420000]
}
df=pd.dataframe(data)
x=df[['size','bedroom']]
y=df['price']
#model
model=linearRegression()
model.fit(x,y)
#predict new_ house                                                                                                                                                                                                                                                                                                                                                                                                