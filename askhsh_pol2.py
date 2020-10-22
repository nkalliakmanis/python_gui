# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:33:58 2020

@author: user
"""

from tkinter import *
from tkinter import scrolledtext
import random as r
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

from sklearn import tree
#import pydotplus
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
import matplotlib.image as pltimg

scale = StandardScaler()
L=[]

class NewFile:
    def __init__(self):
        self.w=Tk()
        self.w.title("New File")
        self.w.geometry("500x500")
        
        l=Label(self.w,text="How many Numbers?")
        l.grid(column=0,row=0)
               
        
        self.e1=Entry(self.w)
        
        
        self.e1.grid(column=1,row=0)
        
        l=Label(self.w,text="Filename:")
        l.grid(column=0,row=1)
        self.e2=Entry(self.w)
        self.e2.grid(column=1,row=1)
        self.l1=Label(self.w,text="")
        self.l1.grid(column=1,row=2)
        
        b1=Button(self.w,text="Save",command=self.savenums)
        b1.grid(column=0,row=3)
        self.w.mainloop()
        
        
    def savenums(self):
        try:
            n=int(self.e1.get())
            filename=self.e2.get()
            Ltmp=[]
            txt=""
            for i in range (n):
                x=r.randint(0,1)
                y=r.randint(0,1)
                z=r.randint(0,1)
                w=r.randint(0,1)
                k=r.randint(0,1)
                R=int(((not(x and y)) or (z or w)) and (not(k)))
                Ltmp.append([x,y,z,w,k,R])
            txt=""
            for l in Ltmp:
                ccc=0
                for c in l:
                    if ccc==0:
                        ccc=1
                        txt=txt+str(c)
                    else:
                        txt=txt+","+str(c)
                txt=txt+"\n"
            f=open(filename,"w")
            f.write(txt)
            f.close()
        except:
            self.e1.delete(0,'end')
            self.e1.insert(0,"error")
        
        
        
        
class Load:
    def __init__(self):
        self.w=Tk()
        self.w.title("Load numbers")
        self.w.geometry("500x500")
        
        l=Label(self.w,text="Filename:")
        l.grid(column=0,row=0)
        self.e=Entry(self.w)
        self.e.grid(column=1,row=0)
        b1=Button(self.w,text="Load",command=self.load)
        b1.grid(column=0,row=1)
        self.w.mainloop()
        
    def load(self):
        global L
        f=open(self.e.get(),"r")
        nn=f.read()
        
        
        df = pandas.read_csv(self.e.get(),names=["x","y","z","w","k","R"])
        L=df.values.tolist()
        f.close()
        
        
        
        
class Neural:
    def __init__(self):
        global L,X,Y
        self.w=Tk()
        self.w.title("Neural")
        self.w.geometry("500x500")
        
        txt=scrolledtext.ScrolledText(self.w,width=40,height=20)
        txt.grid(column=0,row=0)
        
        X=[[x,y,z,w,k] for [x,y,z,w,k,r] in L]
        Y=[r for [x,y,z,w,k,r] in L]
        
        print(X)
        print(Y) 
          
        
        regr = linear_model.LinearRegression() 
        regr.fit(X, Y) 
        
        X2=[[1,0,0,1,1],[1,1,0,1,1],[1,1,1,0,0],[1,0,1,0,0]]
        pp=regr.predict(X2)
        print(pp)
        P=[int(round(p)) for p in  pp]
    
        print(P)
        R=[]
        for x in X2:
            R.append(int(((not(x[0] and x[1])) or (x[2] or x[3])) and (not(x[4]))))
        
        print(R)
        txt.insert(INSERT,"Real:"+str(R)+"\n")
        txt.insert(INSERT,"Predict:"+str(P))
        
        
        

        self.w.mainloop()
        
    
class Tree:
    def __init__(self):
        global L,X,Y
        self.w=Tk()
        self.w.title("Decision Tree Classifier")
        self.w.geometry("600x600")
        
        txt=scrolledtext.ScrolledText(self.w,width=40,height=20)
        txt.grid(column=0,row=0)
        
        X=[[x,y,z,w,k] for [x,y,z,w,k,r] in L]
        Y=[r for [x,y,z,w,k,r] in L]
        print(X)
        print(Y)
       
        dtree = DecisionTreeClassifier() 
        dtree = dtree.fit(X, Y) 
        X2=[[1,0,0,1,1],[1,1,0,1,1],[1,1,1,0,0],[1,0,1,0,0]]
       
        P=dtree.predict(X2)
        print(P) 
        R=[]
        for x in X2:
            R.append(int(((not(x[0] and x[1])) or (x[2] or x[3])) and (not(x[4]))))
        
        print(dtree.score(X2,R))

        
        txt.insert(INSERT,str(dtree.score(X2,R))+"\n")
        txt.insert(INSERT,str(R)+"\n")
        txt.insert(INSERT,str(P)+"\n")
        

        self.w.mainloop()
        

class MLP:
    def __init__(self):
        global L,X,Y
        self.w=Tk()
        self.w.title("Decision Tree Classifier")
        self.w.geometry("600x600")
        
        txt=scrolledtext.ScrolledText(self.w,width=40,height=20)
        txt.grid(column=0,row=0)
        
        X=[[x,y,z,w,k] for [x,y,z,w,k,r] in L]
        Y=[r for [x,y,z,w,k,r] in L]
        print(X)
        print(Y)
       
        mlp = MLPClassifier(hidden_layer_sizes=(10,10,10)) 
        mlp.fit(X, Y) 
        X2=[[1,0,0,1,1],[1,1,0,1,1],[1,1,1,0,0],[1,0,1,0,0]]
       
        P=mlp.predict(X2)
        print(P) 
        R=[]
        for x in X2:
            R.append(int(((not(x[0] and x[1])) or (x[2] or x[3])) and (not(x[4]))))
        
        print(mlp.score(X2,R))

        
        txt.insert(INSERT,str(mlp.score(X2,R))+"\n")
        txt.insert(INSERT,str(R)+"\n")
        txt.insert(INSERT,str(P)+"\n")
        

        self.w.mainloop()
        
        

class MyWindow:
    def __init__(self):
        self.w=Tk()
        self.w.title("My program")
        self.w.geometry("600x600")
        

        b1=Button(self.w,text="New File",command=self.newfile)
        b2=Button(self.w,text="Load",command=self.load)
        b3=Button(self.w,text="Neural",command=self.neural)
        b4=Button(self.w,text="Tree",command=self.tree)
        b5=Button(self.w,text="MLP-Classifier",command=self.tree)
        b6=Button(self.w,text="Exit",command=self.exit1)
        
        b1.config(width=25)
        b2.config(width=25)
        b3.config(width=25)
        b4.config(width=25)
        b5.config(width=25)
        b6.config(width=25)
        
        
        
        b1.grid(column=0,row=1)
        b2.grid(column=0,row=2)
        b3.grid(column=0,row=3)
        b4.grid(column=0,row=4)
        b5.grid(column=0,row=5)
        b6.grid(column=0,row=6)
        self.w.mainloop()
        
    def newfile(self):
        w2=NewFile()

    def load(self):
        w2=Load()
        
    def neural(self):
        w2=Neural()
    
    def tree(self):
        w2=Tree()
    
    def mlp(self):
        w2=MPL()
        
    def exit1(self):
        self.w.destroy()
       
myframe=MyWindow()