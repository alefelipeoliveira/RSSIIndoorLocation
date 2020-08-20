import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from Trilateration import *
from pathloss import calculate_distance
from error import error
from knn import knn

dataset_list = ['Sadowski_1', 'Sadowski_2', 'Sadowski_3']

dataset = st.sidebar.selectbox("Escolha o dataset",dataset_list)
tech = st.sidebar.selectbox("Escolha a tecnologia", ['BLE', 'Zigbee', 'WIFI'])
Positions = st.sidebar.selectbox("Escolha as posições",['Database', 'Test'])
algorithm = st.sidebar.selectbox("Escolha o algoritmo",['Trilateration', 'KNN'])
if (algorithm == 'KNN'):
    k = st.sidebar.selectbox("Escolha um número de vizinhos",[2,3,4,5,6])

Layout = ".//data//" + dataset + "//Layout.jpg"
Positions = ".//data//" + dataset + "//" + tech + "//" + Positions + ".csv"
database = ".//data//" + dataset + "//" + tech + "//" + "Database.csv"
testset = ".//data//" + dataset + "//" + tech + "//" + "Test.csv"
Anchors = ".//data//" + dataset + "//Anchors.csv"
Limits = ".//data//" + dataset + "//Limits.csv"
Pathloss_model = ".//data//" + dataset + "//" + tech +"//pathloss.csv"
 
#Reading floor plan to use as Background image
img = plt.imread(Layout)

Positions = pd.read_csv(Positions, sep=";")
database = pd.read_csv(testset, sep=";")
testset = pd.read_csv(testset, sep=";")
Anchors = pd.read_csv(Anchors, sep=";")
Limits = pd.read_csv(Limits, sep=";")
Pathloss_model = pd.read_csv(Pathloss_model, sep=";")

fig, ax = plt.subplots()

ax.scatter(list(Anchors['x']), list(Anchors['y']))
if(algorithm == 'Trilateration' ):
    ax.scatter(list(Positions['x']), list(Positions['y']))
    Positions = Trilateration(Positions, Anchors, Pathloss_model)
    for i in range(len(list(Positions['x']))):
        ax.plot([Positions['x'][i], Positions['x_calc'][i]], [Positions['y'][i], Positions['y_calc'][i]], color = 'r')
    ax.scatter(list(Positions['x_calc']), list(Positions['y_calc']))
elif(algorithm == 'KNN' ):
    ax.scatter(list(testset['x']), list(testset['y']))
    Positions = knn(database, testset, k)
    for i in range(len(list(Positions['x']))):
        ax.plot([Positions['x'][i], Positions['x_calc'][i]], [Positions['y'][i], Positions['y_calc'][i]], color = 'r')
    ax.scatter(list(Positions['x_calc']), list(Positions['y_calc']))

#adapt picture dimensions to floorplan dimension (25x25m) to trajectory points match with floorplan
ax.imshow(img, extent=list(Limits['limits']))

st.pyplot()
#st.dataframe(Positions[['x','y', 'x_calc', 'y_calc', 'error']])
st.dataframe(Positions)