# python -m pip install --upgrade pip
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.db import connection
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle
import zipfile
# install and import here your required modules like pandas, numpy etc by using pip
# install them in your virtual environments or you can use my virtual env too
# if you are using the external script import the file here
# . pip, django is already installed. You have to install pandas, numpy
# or create your own virtual environment
# This file is accessing a name variable and rendering a demo result in output.html file
#you can import your own script and replace the returned result with this result array 

def index(request):
    	return render(request,'index.html')

# 	if request.method == 'POST':
# 		print('index post')
# 		name = request.POST.get('name')
# 		#This is the input
# 		print(name)
# 		zip = zipfile.ZipFile(r'./dataset.zip')
# 		zip.extractall(r'./')
# 		dataset = pd.read_csv(r'./dataset.csv')
# 		X = dataset.iloc[:,[*range(11,73),*range(74,89)] ].values
# 		J = dataset.iloc[:,:].values
# 		z=  dataset.iloc[:,[4] ].values
# 		y=  dataset.iloc[:,[1] ].values
# 		y=list(y)
# 		k=[]
# 		for Num in range(len(y)):
# 			if(y[Num][0]==name):
# 				k.append(J[Num])
# 		mid=[]
# 		for K in k:
# 			mid.append({'uid':K[0],'name':K[1],'DOB':K[3]})
# 		return render(request,'dataset/mid.html',{'mid':mid})
# 		# Apply your logic here or call the external python script giving the arguement name 
# 		# and put the returned value in result
# 		# For example if returned value from your python script is an array of two elements
# 		# Then 
# 		result = [{'firstname':"PLAYER NAME" , 'age':"PLAYER AGE"}]
# 		X = dataset.iloc[:,[*range(11,73),*range(74,89)] ].values
# 		J = dataset.iloc[:,:].values
# 		z=  dataset.iloc[:,[4] ].values
# 		y=  dataset.iloc[:,[1] ].values
# 		w= list(y)
# 		zip = zipfile.ZipFile(r'./jantu.zip')
# 		zip.extractall(r'./')
# 		filename='jantu.sav'
# 		knn=pickle.load(open(filename, 'rb'))


# 		#--------------------run from here---------------
# 		n=w.index([name])
# 		k=knn.kneighbors(X[n],return_distance=False).reshape(-1,1)

# 		Ans=[]
# 		for i in k:
# 			Ans.append(np.append(np.append(X[i],i),z[i]))
			
# 		Ans = sorted(Ans, key=lambda r: r[-1])
# 		print("________","Similar player to" ,y[n][0],"__________")
# 		for p in Ans:
# 			result.append({'firstname':y[p[-2]][0],'age':p[-1]})

# 		return render(request, 'dataset/output.html',{'result':result})
# 	else:
# 		return render(request, 'dataset/index.html')

# def mid(request):
# 	if request.method == 'POST':
		
# 		dataset = pd.read_csv(r'./dataset.csv')
# 		mid = request.POST.get('mid')
# 		print("THIS IS "+mid)
# 		result = [{'firstname':"PLAYER NAME" , 'age':"PLAYER AGE"}]
# 		X = dataset.iloc[:,[*range(11,73),*range(74,89)] ].values
# 		J = dataset.iloc[:,:].values
# 		z=  dataset.iloc[:,[4] ].values
# 		aq= dataset.iloc[:,[1] ].values
# 		y=  dataset.iloc[:,[0] ].values
# 		w= list(y)
# 		zip = zipfile.ZipFile(r'./jantu.zip')
# 		zip.extractall(r'./')
# 		filename='jantu.sav'
# 		knn=pickle.load(open(filename, 'rb'))


# 		#--------------------run from here---------------
# 		n=w.index([int(mid)])
# 		k=knn.kneighbors(X[n].reshape(1,-1),return_distance=False).reshape(-1,1)

# 		Ans=[]
# 		for i in k:
# 			Ans.append(np.append(np.append(X[i],i),z[i]))
			
# 		Ans = sorted(Ans, key=lambda r: r[-1])
# 		print("________","Similar player to" ,y[n][0],"__________")
# 		for p in Ans:
# 			result.append({'firstname':aq[p[-2]][0],'age':p[-1]})

# 		return render(request, 'dataset/output.html',{'result':result})
# 	else:


# def output2(request):
# 		pass
		

# def output(request):
# 	render(request,'dataset/output.html')

# def check(request):
# 	render(request,'dataset/index.html')
