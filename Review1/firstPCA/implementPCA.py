# importing computation data manipulation and plotting modules
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

dataset = pd.read_csv("diabetes.csv")

# Get properties described in dataset to X
X = dataset.iloc[:,0:8]

# Get the last column(outcome)
y = dataset.iloc[:,8]

# limiting feature space with mean 0 and variance 1
X_std = (X-np.mean(X,axis = 0))/np.std(X,axis = 0)

# Get covariance matrix of X
cov_matrix = np.cov(X_std, rowvar=False)

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors, = np.linalg.eig(cov_matrix)

# sort eigenvalues by making pairs with eigenvectors
eigen_pairs = [(eigenvalues[index], eigenvectors[:,index]) for index in range(len(eigenvalues))]
eigen_pairs.sort()
eigen_pairs.reverse()

# Get eigenvalues and eigenvectors
eigvalues_sort = [eigen_pairs[index][0] for index in range(len(eigenvalues))]
eigvectors_sort = [eigen_pairs[index][1] for index in range(len(eigenvalues))]

# Considering the top 2 principal components
# 8 x 2 matrix
topTwo = np.array(eigvectors_sort[0:2]).transpose()

# n x 2 matrix
Proj_data_2D = np.dot(X_std,topTwo)

# Plot data for tests that are negative
negative = plt.scatter(Proj_data_2D[:,0][y == 0], Proj_data_2D[:,1][y == 0])

# Plot data for tests that are positive
positive = plt.scatter(Proj_data_2D[:,0][y == 1], Proj_data_2D[:,1][y == 1], color = "red")

plt.title('First PCA')

# y-axis
plt.ylabel('Principal Component 2')

# x-axis
plt.xlabel('Principal Component 1')

# legend
plt.legend([negative,positive],["Nondiabetic", "Diabetic"])

# plot
plt.show()