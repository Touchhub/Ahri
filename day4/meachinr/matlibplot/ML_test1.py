import numpy as np
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris=datasets.load_iris()
iris_X=iris.data
iris_y=iris.target

# print(iris_X[:2,:])
# print(iris_y)
X_train,X_test,y_train,y_test=train_test_split(
    iris_X,iris_y,test_size=0.3
)
#print(y_test)
knn=KNeighborsClassifier()
knn.fit(X_train,y_train)
a=knn.predict(X_test)
b=(y_test)
count=0
for i in range(len(a+1)):
    print((a[i])-b[i])
    if a[i]-b[i]==0:
        count+=1
print(count/len(a))