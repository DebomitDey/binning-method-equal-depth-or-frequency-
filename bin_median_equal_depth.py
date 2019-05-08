import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
#import statsmodels.api as sm
import statistics
import math
from collections import OrderedDict


x=[]
print("enter the data")
x=list(map(float,input().split()))

print("enter the number of bins")
bi=int(input())

#X_dict will store the data in sorted order
X_dict=OrderedDict()
#x_old will store the original data
x_old={}
#x_new will store the data after binning
x_new={}

for i in range(len(x)):
	X_dict[i]=x[i]
	x_old[i]=x[i]

x_dict=sorted(X_dict.items(), key=lambda x: x[1])


#list of lists(bins)
binn=[]
#a variable to find the mean of each bin
avrg=[]

i=0
k=0
num_of_data_in_each_bin=int(math.ceil(len(x)/bi))
#performing binning
for g,h in X_dict.items():
	if(i<num_of_data_in_each_bin):
		avrg.append(h)
		i=i+1
	elif(i==num_of_data_in_each_bin):
		k=k+1
		i=0
		binn.append(statistics.median(avrg))
		avrg=[]
		avrg.append(h)
		i=i+1

binn.append(statistics.median(avrg))

#store the new value of each data
i=0
j=0
for g,h in X_dict.items():
	if(i<num_of_data_in_each_bin):
		x_new[g]=round(binn[j],3)
		i=i+1
	else:
		i=0
		j=j+1
		x_new[g]=round(binn[j],3)
		i=i+1

print("number of data in each bin")
print(math.ceil(len(x)/bi))
for i in range(0,len(x)):
	print('index {2}            old value  {0}         new value  {1}'.format(x_old[i],x_new[i],i))

