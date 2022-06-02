import pandas as pd
data = [['Alex',10, 2009],['Bob',12, 2011],['Clarke',13, 2012]]
df = pd.DataFrame(data,columns=['Name','Age', 'Year'])
k = pd.read_csv(r'/home/exio/Downloads/a.csv')
print(k)