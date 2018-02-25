import numpy as np 
import math

'''this is regression'''

''' prepare the inputs and outputs first'''
x=np.array([1,2,3,4,5,6,7,8,9,10], dtype=np.float64)
y=np.array([2,4,6,8,10,12,14,16,18,20], dtype=np.float64)

'''the equation is y=a+bx'''
'''first. find b by methods, find covariance of x and y first from data training'''
covariance=np.cov([x, y]) [0][1]
var=np.var([x])
x_max=np.max ([x])
y_max=np.max ([y])

b=covariance/var

a=y_max - (b * x_max)

#print a
#print b 
'''for predict'''
#class regression():
#	def __init__(self):
#		self.a=a
#		self.b=b

def predict(inputs):
	y_output=a + (b * inputs)
	return y_output
#if __name__ == '__main__':

s=4.3
	#test=regression()
a=predict(s)
print a 