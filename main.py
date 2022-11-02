import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('R.csv')

# size of the dataset 
print('Number of columns ',data.shape[1])
print('Number of rows ',data.shape[0])
print('--------------------------- \n')

# number of empty values cells 
print('Number of empty values \n')
print(data.isna().sum())
print('--------------------------- \n')

print('Sample discription of numaric columns \n')
print(data.drop('plant no',axis=1).describe())
print('--------------------------- \n')


colors=[
  '#FF00FF','#800080','#000080','#0000FF','#008080','#008000','#808000','#800000','#808080','#000000',
  '#0dbdb2','#8c1664','#fc03ff','#8a2be2'
]

# plant height vs 
fig,((plt1,plt2),(plt3,plt4))=plt.subplots(2,2)
fig.set_size_inches((10,9))


plt1.scatter(data[['plant height']],data[['plant weight']],c='#bf911d')
plt1.set_title("Plant Height vs Plant Weight")
plt1.set_ylabel("Weight")

plt2.scatter(data[['plant height']],data[['no of leaves']],c='#b33f12')
plt2.set_title("Plant Height vs no of leaves")
plt2.set_ylabel("No of leaves")

plt3.scatter(data[['plant height']],data[['no of roots']],c='#b4bd0d')
plt3.set_title("Plant Height vs no of roots")
plt3.set_ylabel("no of roots")

plt4.scatter(data[['plant height']],data[['root length']],c='#218a07')
plt4.set_title("Plant Height vs root length")
plt4.set_ylabel("root length")



# plant weight vs plots 

fig2,(plt1,plt2,plt3)=plt.subplots(1,3)
fig2.set_size_inches((14,5))

plt1.scatter(data[['plant weight']],data[['no of leaves']],c='#5b5e5b')
plt1.set_title("Plant Height vs Plant Weight")
plt1.set_ylabel("no of leaves")
plt1.set_xlabel("Plant weight")

plt2.scatter(data[['plant weight']],data[['no of roots']],c='#06996f')
plt2.set_title("Plant Weight vs no of leaves")
plt2.set_ylabel("No of leaves")
plt2.set_xlabel("Plant weight")

plt3.scatter(data[['plant weight']],data[['root length']],c='#2c7385')
plt3.set_title("Plant Weight vs no of roots")
plt3.set_ylabel("root length")
plt2.set_xlabel("Plant weight")


# no of leaves vs no of roots 
fig3,plt1=plt.subplots(1)
plt1.scatter(data[['no of leaves']],data[['no of roots']],c='#092aba')
plt1.set_title("Number of leaves vs number of roots")
plt1.set_xlabel('no of leaves')
plt1.set_ylabel('no of roots')


# no of roots vs root length 

fig4,plt1=plt.subplots(1)
plt1.scatter(data[['no of roots']],data[['root length']],c='#7518a1')
plt1.set_title("number of roots vs root length")
plt1.set_xlabel("no of roots")
plt1.set_ylabel("root length")

# ax = fig.add_subplot(projection='3d')
# ax.scatter(data["plant height"], data["plant weight"], data["no of leaves"])
# ax.set_xlabel('plant height')
# ax.set_ylabel('plant weight')
# ax.set_zlabel('no of leaves')

# plant number vs root length first 100 plants 
fig5,plt1=plt.subplots(1)
plt1.set_title("Plant number vs root length (first 100 plants)")
plt1.scatter(data[['plant no']][:100],data[['root length']][:100])
plt1.set_xlabel("plant no")
plt1.set_ylabel("root length")




#plt.show()




plt.show()