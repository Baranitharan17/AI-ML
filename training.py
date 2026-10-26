from sklearn.datasets import load_iris, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score,f1_score,confusion_matrix
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.cluster import KMeans
from collections import Counter
import pandas as pd
import numpy as np

#1)load the iris dataset
#iris=load_iris()

#seperate features and target labels
#X=iris.data
#y=iris.target

#split the dataset into 80% training and 20% testing
# X_train, X_test, y_train, y_test=train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
#)
# #print the shapes
# print("Total samples:", len(X))
# print("Training samples:", len(X_train))
# print("Testing samples:", len(X_test))
# print("X_train shape:", X_train.shape)
# print("X_train shape:", X_test.shape)
# print("y_train shape:", y_train.shape)
# print("y_train shape:", y_test.shape)

#2)Train a LogisticRegression model (supervised) and print accuracy, F1 score (macro) and
#the confusion matrix

# #create the logistic regression model
# model=LogisticRegression(max_iter=200)

# #train the model(supervised learning)
# model.fit(X_train,y_train)

# #make predictions
# y_pred=model.predict(X_test)

# #evaluate the model
# accuracy=accuracy_score(y_test,y_pred)
# f1=f1_score(y_test,y_pred,average="macro")
# cm=confusion_matrix(y_test,y_pred)

# #print evaluation metrics
# print("Accuracy:", accuracy)
# print("F1 score (Macro):", f1)
# print("Confusion matrix:")
# print(cm)

#3)Run KMeans(n_clusters=3) on the same features without using labels (unsupervised) and
#print the cluster sizes

# #create the K-means model
# kmeans=KMeans(n_clusters=3,random_state=42,n_init=10)

# #train the model without labels(unsupervised training)
# kmeans.fit(X)

# #get cluster assignments
# clusters=kmeans.labels_

# #print cluster sizes
# cluster_sizes=Counter(clusters)

# print("Cluster Sizes:")
# for cluster_id in sorted(cluster_sizes):
#     print(f"Cluster{cluster_id}:{cluster_sizes[cluster_id]}samples")

# #4) Compare the clusters with the real species and write 3 lines on what you observe
# # Apply kmeans without using actual labels
# kmeans=KMeans(n_clusters=3,random_state=42,n_init=10)
# clusters=kmeans.fit_predict(X)

# #compare clusters with real spices
# print("Confusion Matrix:")
# print(confusion_matrix(y, clusters))

# #compare each cluster with actual species
# df= pd.DataFrame(
#     {
#         "Actual Species":iris.target_names[y],
#         "KMeans cluster": clusters
#     }
# )
# print(pd.crosstab(df["Actual Species"].df["KMeans Cluster"]))

#TASK -2
#Load the diabetes dataset (or any numeric dataset given by your trainer) and split it 80/20
#1)load the diabetes dataset
# diabetes=load_diabetes()

# #seperate features and target labels
# X=diabetes.data
# y=diabetes.target

# #split the dataset into 80% training and 20% testing
# X_train, X_test, y_train, y_test=train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )
# # #print the shapes
# print("Total samples:", len(X))
# print("Training samples:", len(X_train))
# print("Testing samples:", len(X_test))
# print("X_train shape:", X_train.shape)
# print("X_train shape:", X_test.shape)
# print("y_train shape:", y_train.shape)
# print("y_train shape:", y_test.shape)

#2)Train LinearRegression and print MAE, RMSE and R-squared on the test set

# diabetes=load_diabetes()
# #seperate features and target labels
# X=diabetes.data
# y=diabetes.target

# #split the dataset into 80% training and 20% testing
# X_train, X_test, y_train, y_test=train_test_split(
# X,
# y,
# test_size=0.2,
# random_state=42
# )
# #create the linear regression model
# model=LinearRegression()
# #train the model
# model.fit(X_train,y_train)
# #predict on the test set
# y_pred=model.predict(X_test)
# #calculate evaluation metrics
# mae=mean_absolute_error(y_test,y_pred)
# rmse=np.sqrt(mean_squared_error(y_test,y_pred))
# r2=r2_score(y_test,y_pred)
# #print the results
# print("MAE:", mae)
# print("RMSE:",rmse)
# print("R-Squared:",r2)

#3)Build a baseline that always predicts the mean of the training target and print its MAE and
# RMSE
# diabetes=load_diabetes()
# #seperate features and target labels
# X=diabetes.data
# y=diabetes.target

# #split the dataset into 80% training and 20% testing
# X_train, X_test, y_train, y_test=train_test_split(
# X,
# y,
# test_size=0.2,
# random_state=42
# )

# #calculate the means of the training target
# mean_value=np.mean(y_train)
# # always predict the training mean
# y_pred=np.full(len(y_test),mean_value)
# #calculate MAE and RMSE
# mae=mean_absolute_error(y_test,y_pred)
# rmse=np.sqrt(mean_squared_error(y_test,y_pred))
# #print results
# print("Training target mean:", mean_value)
# print("Baseline MAE:",mae)
# print("Baseline RMSE:",rmse)
