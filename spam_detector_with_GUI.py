#importing the libraries
from tkinter import *
import pandas as pd
import numpy as np
root = Tk()

#importing the dataset
dataset = pd.read_csv("https://raw.githubusercontent.com/amankharwal/SMS-Spam-Detection/master/spam.csv", encoding= 'latin-1')
dataset.head()
x = np.array(dataset["message"])
y = np.array(dataset["class"])

#creating the bag of words model
from sklearn.feature_extraction.text import  CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(x).toarray()

#Train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.32,random_state=42)

#fitting the classifier
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train,y_train)

#predicting the test set result
y_pred = classifier.predict(X_test)

#Making the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)

def check():
    sample=t1.get()
    dataset = cv.transform([sample]).toarray()
    messagebox.showinfo("answer",classifier.predict(dataset))

def clean():
    t1.delete(0,END)


root.title("Spam Detection GUI")
root.geometry("800x400")
l1 = Label(root,text="Enter the message :-",width=15,font=("arial",10))
l1.grid(row=0,column=0)
t1=Entry(root,width=80)
t1.grid(row=0,column=1)
b1=Button(root,text="Checking",width=10,height=2,command=check)  #button click event
b1.grid(row=2,column=0)
b2=Button(root,text='Clear',width=10,height=2,command=clean)
b2.grid(row=2,column=1)
root.mainloop()