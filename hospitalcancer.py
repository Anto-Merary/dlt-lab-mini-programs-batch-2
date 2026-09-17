import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


mean = X_train.mean(axis=0)
std = X_train.std(axis=0) + 1e-8

X_train = (X_train - mean) / std
X_test = (X_test - mean) / std


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


weights = np.zeros(X_train.shape[1])
bias = 0
lr = 0.01

for i in range(1000):

    
    z = np.dot(X_train, weights) + bias
    y_pred = sigmoid(z)

    
    dw = np.dot(X_train.T, (y_pred - y_train)) / len(y_train)
    db = np.mean(y_pred - y_train)

    weights -= lr * dw
    bias -= lr * db


y_test_pred = sigmoid(np.dot(X_test, weights) + bias)
y_test_pred = (y_test_pred >= 0.5).astype(int)


accuracy = accuracy_score(y_test, y_test_pred)

print("Accuracy:", accuracy)