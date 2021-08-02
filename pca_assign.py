# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 23:09:53 2021

@author: Amarnadh Tadi

"""
### PCA for Wine data

import pandas as pd 
import numpy as np

wine = pd.read_csv(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign6\wine.csv")
wine.describe()
wine.columns




from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 


# Normalizing the numerical data 
wine_normal = scale(wine)
wine_normal

pca = PCA(n_components = 6)
pca_values = pca.fit_transform(wine_normal)

# The amount of variance that each PCA explains is 
var = pca.explained_variance_ratio_
var

pca.components_
pca.components_[0]
# Cumulative variance 

var1 = np.cumsum(np.round(var, decimals = 4) * 100)
var1

# Variance plot for PCA components obtained 
%matplotlib inline
plt.plot(var1, color = "red")

# PCA scores
pca_values

pca_data = pd.DataFrame(pca_values)
pca_data.columns = "comp0", "comp1", "comp2", "comp3", "comp4", "comp5"
final = pd.concat([wine.Type, pca_data.iloc[:, 0:3]], axis = 1)

# Scatter diagram
import matplotlib.pylab as plt
plt.scatter(x = final.comp0, y = final.comp1)
###performing hclustring for wine data
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch 
z = linkage(wine_normal, method = "complete", metric = "euclidean")
# Dendrogram
plt.figure(figsize=(12,8));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 
)
plt.show()
# Now applying AgglomerativeClustering choosing 3 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering
h_complete = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = "euclidean").fit(wine_normal) 
h_complete.labels_
h_complete.n_clusters
cluster_labels=pd.Series(h_complete.labels_)
wine['clust']=cluster_labels

wine.head()
# Aggregate mean of each cluster
wine.iloc[:, 1:].groupby(wine.clust).mean()
###performing hclustring for wine data after PCA
z1 = linkage(final, method = "complete", metric = "euclidean")
# Dendrogram
plt.figure(figsize=(12,8));plt.title('Hierarchical Clustering Dendrogram(After PCA');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(z1, 
    leaf_rotation = 0,  # rotates the x axis labels
    leaf_font_size = 10 
)
plt.show()
# Now applying AgglomerativeClustering choosing 3 as clusters from the above dendrogram
from sklearn.cluster import AgglomerativeClustering
h_complete1 = AgglomerativeClustering(n_clusters = 3, linkage = 'complete', affinity = "euclidean").fit(final) 
h_complete1.labels_
h_complete1.n_clusters
cluster_labels1=pd.Series(h_complete1.labels_)
final['clust']=cluster_labels1
x=h_complete.children_
y=h_complete1.children_
final.head()
# Aggregate mean of each cluster
final.iloc[:, 1:].groupby(final.clust).mean()
##Kmeans clustring on given data
from sklearn.cluster import	KMeans
###### scree plot or elbow curve ############
TWSS = []
k = list(range(2, 9))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(wine_normal)
    TWSS.append(kmeans.inertia_)
TWSS   
#screeplot 
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")
###### scree plot or elbow curve for data after aPCA formed ############
TWSS1 = []
k = list(range(2, 9))

for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(final)
    TWSS.append(kmeans.inertia_)
TWSS1   
#screeplot 
plt.plot(k, TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS")

####################################################################################
##PCA for Pharma data

import pandas as pd 
import numpy as np

pharma = pd.read_csv(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign6\heart disease.csv")
pharma.describe()
pharma.columns


pharma1 = pharma.drop(['exang'], axis = 1)

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale 


# Normalizing the numerical data 
pharma1_normal = scale(pharma)
pharma1_normal

pca = PCA(n_components = 6)
pca_values = pca.fit_transform(pharma1_normal)

# The amount of variance that each PCA explains is 
var = pca.explained_variance_ratio_
var

pca.components_
pca.components_[0]
# Cumulative variance 

var1 = np.cumsum(np.round(var, decimals = 4) * 100)
var1

# Variance plot for PCA components obtained 
%matplotlib inline
plt.plot(var1, color = "red")

# PCA scores
pca_values

pca_data = pd.DataFrame(pca_values)
pca_data.columns = "comp0", "comp1", "comp2", "comp3", "comp4", "comp5"
final = pd.concat([uni.Univ, pca_data.iloc[:, 0:3]], axis = 1)

# Scatter diagram
import matplotlib.pylab as plt
plt.scatter(x = final.pc0, y = final.pc1)

