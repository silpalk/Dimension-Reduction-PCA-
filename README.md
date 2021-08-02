# Dimension-Reduction-PCA-
Principal Component Analysis with python on Wine data set


Principal Component Analysis with python



PROBLEM STATEMENT:

Perform Principal component analysis and perform clustering using first 3 principal component scores ( Hierarchical). Use Scree plot or elbow curve and obtain optimum number of clusters and check whether we have obtained same number of clusters with the original data
Objective:
 Use Scree plot or elbow curve and obtain optimum number of clusters and check whether we have obtained same number of clusters with the original data

STEPS TO BE FOLLOWED TO OBTAIN SOLUTION:
STEP1:
Loading of wine data on which PCA method are applied. wine data set is of 8 rows and 15 columns. The details of the data is
 
STEP2:

AFTER describing data ,to obtain PCA s PCA module is imported from sklearn.decomposition .  PCA  technique is applied only on normalized data. For normalization Scale module is imported from sklearn.preprocessing .
 STEP3:
For n_components = 6 ;PCA  is obtained and its fitted to normalized wine data. Variance plot for PCA components obtained
 
STEP3

Later pca data is concated to main data index column and Scatter diagram is plotted
 
STEP 5:
check whether we have obtained same number of clusters with the original data Clustring techniques is applied on original wine data.
Dendogram is drawn for original wine data
 
STEP 6:
performing hclustering for wine data after PCA  and Dendogram is drawn
 
STEP7:
After plotting Dendogram for both the data cluster groups were obtained from AgglomerativeClustering which is imported from sklearn.cluster by complete method

cluster grouping for main data
 
cluster grouping for data after PCA framed
 

STEP8:
Same way kmeans clustering is applied on both the data sets of given and after PCA formed.
to do kmeans ,the regarding module kmeans is imported from sklearn.cluster.
STEP 9:
scree plot or elbow curve is plotted between no.of clusters picked and total data points with in sum of squares.
 
scree plot is plotted for PCA applied data 
 
Summary:
Using Scree plot or elbow curve we can determine the  obtain optimum number of clusters obtained same number of clusters with the original data






PROBLEM STATEMENT:
A Pharmaceutical drug manufacturing company is studying on a new medicine to treat Heart diseases, it has gathered data from its secondary sources, and it would like you to provide high level analytical insights on the data, its aim is to segregate patients depending on their age group and other factors as given in the data, perform PCA and Clustering Machine learning Algorithm on the dataset given, and check if the clusters formed before and after PCA are same and provide a brief report on your model. You can also explore more on ways to improve your model. 
Objective:
Aim is to segregate patients depending on their age group and other factors as given in the data, perform PCA and Clustering Machine learning Algorithm on the dataset given, and check if the clusters formed before and after PCA are same and provide a brief report on your model. You can also explore more on ways to improve your model. 
STEPS TO BE FOLLOWED TO OBTAIN SOLUTION:
STEP1:
Loading of Pharma data on which PCA method are applied. wine data set is of 8 rows and 14columns. The details of the data is

 
STEP 2
from sklearn.decomposition import PCA ,with that PCA are obtained


Variance plot for PCA components is plotted
 
STEP:
PCA are concated to the given data  index column and then scattered plot is plotted between first two components of final data
 

