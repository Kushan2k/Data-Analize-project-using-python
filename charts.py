import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


data=pd.read_csv('R.csv')

colors=[
  '#FF00FF','#800080','#000080','#0000FF','#008080','#008000','#808000','#800000','#808080','#000000',
  '#0dbdb2','#8c1664','#fc03ff','#8a2be2'
]


# mediums pie chart 


fig7,(plt1,plt2)=plt.subplots(1,2)
fig7.set_size_inches((10,5))

count=data[['Medium']].value_counts()
plt1.pie(count,labels=data['Medium'].unique())
plt1.set_title("Medium Distribution")
plt1.legend(title='Mediums')

# plant height acroding to mediums 

plt2.bar(data['Medium'],data['plant height'],color=random.choice(colors))
plt2.set_title('plants height acording to mediums')
plt2.set_xlabel('Medium')
plt2.set_ylabel('Height ')


fig8,(plt1,plt2)=plt.subplots(1,2)
fig8.set_size_inches((10,5))
acNon=data[['AC/NON']].value_counts()

plt1.pie(acNon,labels=data['AC/NON'].unique())
plt1.set_title("AC/NON Distribution")
plt1.legend(title='AC/NON')


plt2.bar(data['AC/NON'],data['plant height'],width=0.6,color=random.choice(colors))
plt2.set_title('plants height acording to AC/NON')
plt2.set_xlabel('AC/NON')
plt2.set_ylabel('Height ')


# tile yes or no 
fig9,(plt1,plt2)=plt.subplots(1,2)
fig9.set_size_inches((10,5))
acNon=data[['Tile yes/no']].value_counts()

plt1.pie(acNon,labels=data['Tile yes/no'].unique())
plt1.set_title("Tile yes/no Distribution")
plt1.legend(title='Tile yes/no')


plt2.bar(data['Tile yes/no'],data['plant height'],width=0.6,color=random.choice(colors))
plt2.set_title('plants height acording to Tile yes/no')
plt2.set_xlabel('Tile yes/no')
plt2.set_ylabel('Height ')



fig10,plt1=plt.subplots(1)
plt1.bar(data['Tile yes/no'],data['plant weight'],width=0.6,color=random.choice(colors))
plt1.set_title('plants weight acording to Tile yes/no')
plt1.set_xlabel('Tile yes/no')
plt1.set_ylabel('Weight ')



fig11,plt1=plt.subplots(1)
plt1.bar(data['Medium'],data['plant weight'],width=0.6,color=random.choice(colors))
plt1.set_title('plants Weight acording to Medium')
plt1.set_xlabel('Medium')
plt1.set_ylabel('Weight ')


fig12,plt1=plt.subplots(1)
plt1.bar(data['AC/NON'],data['plant weight'],width=0.6,color=random.choice(colors))
plt1.set_title('plants Weight acording to AC/NON')
plt1.set_xlabel('AC/NON')
plt1.set_ylabel('Weight ')


fig13,plt1=plt.subplots(1)
plt1.bar(data['AC/NON'],data['no of leaves'],width=0.6,color=random.choice(colors))
plt1.set_title('plants no of leaves acording to AC/NON')
plt1.set_xlabel('AC/NON')
plt1.set_ylabel('no of leaves ')

fig14,plt1=plt.subplots(1)
plt1.bar(data['Medium'],data['no of leaves'],width=0.6,color=random.choice(colors))
plt1.set_title('plants no of leaves acording to Medium')
plt1.set_xlabel('Medium')
plt1.set_ylabel('no of leaves ')

fig15,plt1=plt.subplots(1)
plt1.bar(data['Tile yes/no'],data['no of leaves'],width=0.6,color=random.choice(colors))
plt1.set_title('plants no of leaves acording to Tile yes/no')
plt1.set_xlabel('Tile yes/no')
plt1.set_ylabel('no of leaves ')



plt.show()