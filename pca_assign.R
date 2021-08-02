
library(readr)
wine <- read_csv(file.choose())



attach(wine)


pcaObj <- princomp(wine, cor = TRUE, scores = TRUE, covmat = NULL)

str(pcaObj)
summary(pcaObj)

loadings(pcaObj)

plot(pcaObj) # graph showing importance of principal components 

biplot(pcaObj)

plot(cumsum(pcaObj$sdev * pcaObj$sdev) * 100 / (sum(pcaObj$sdev * pcaObj$sdev)), type = "b")

pcaObj$scores
pcaObj$scores[, 1:3]

# Top 3 pca scores 
final <- cbind(wine[ ,1], pcaObj$scores[, 1:3])
View(final)

# Scatter diagram
plot(final$Comp.1, final$Comp.2)
##############################################################################
#PCA for pharma data
library(readr)
pharma <- read_csv(file.choose())



attach(pharma)


pcaObj <- princomp(pharma, cor = TRUE, scores = TRUE, covmat = NULL)

str(pcaObj)
summary(pcaObj)

loadings(pcaObj)

plot(pcaObj) # graph showing importance of principal components 

biplot(pcaObj)

plot(cumsum(pcaObj$sdev * pcaObj$sdev) * 100 / (sum(pcaObj$sdev * pcaObj$sdev)), type = "b")

pcaObj$scores
pcaObj$scores[, 1:3]

# Top 3 pca scores 
final <- cbind(pharma[ ,1], pcaObj$scores[, 1:3])
View(final)

# Scatter diagram
plot(final$Comp.1, final$Comp.2)
