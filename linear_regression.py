import matplotlib.pyplot as plt
import numpy as np
from random import *
xl=np.array([])
yl=np.array([])
for i in range(11):
    x=randint(1,4)
    y=randint(1,4)
    #xl=np.append(xl,x)
    #yl=np.append(yl,y)
plt.scatter(xl,yl)
mean_x=sum(xl)/len(xl)
mean_y=sum(yl)/len(yl)
distance_x=[i-mean_x for i in xl]
distance_y=[i-mean_y for i in yl]
square=[i*i for i in distance_x]
multip=[distance_x[i]*distance_y[i] for i in range(len(distance_x))]
b1=sum(multip)/sum(square)
b0=mean_y-(b1*mean_x)
plt.plot(xl,(b1*xl)+b0,color="red")
plt.show()