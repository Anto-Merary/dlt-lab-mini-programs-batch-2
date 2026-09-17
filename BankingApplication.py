import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target.reshape(-1, 1)

# Normalize using mean and standard deviation
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)
X = (X - mean) / (std + 1e-8)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Initialize weights and bias
W = np.zeros((X_train.shape[1], 1))
b = 0

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Training
for i in range(1000):

    # Forward propagation
    Z = np.dot(X_train, W) + b
    A = sigmoid(Z)

    # Error
    error = A - y_train

    # Update weights
    W -= 0.01 * np.dot(X_train.T, error)
    b -= 0.01 * np.sum(error)

# Prediction
Z = np.dot(X_test, W) + b
A = sigmoid(Z)

y_pred = (A > 0.5).astype(int)

# Accuracy
accuracy = np.mean(y_pred == y_test) * 100

print("Accuracy:", accuracy)