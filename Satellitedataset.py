import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer


data = load_breast_cancer()
X = data.data                                                                                                           
y = data.target.reshape(-1, 1)

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

X = (X - mean) / std


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)


W1 = np.random.randn(30, 10)
b1 = np.zeros((1, 10))

W2 = np.random.randn(10, 1)
b2 = np.zeros((1, 1))

# Activation functions
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def tanh_derivative(a):
    return 1 - a**2

for epoch in range(1000):

    Z1 = np.dot(X_train, W1) + b1
    A1 = np.tanh(Z1)

    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)


    dZ2 = A2 - y_train
    dW2 = np.dot(A1.T, dZ2)
    db2 = np.sum(dZ2, axis=0, keepdims=True)

    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * tanh_derivative(A1)

    dW1 = np.dot(X_train.T, dZ1)
    db1 = np.sum(dZ1, axis=0)

    lr = 0.01

    W1 -= lr * dW1
    b1 -= lr * db1
    W2 -= lr * dW2
    b2 -= lr * db2


Z1 = np.dot(X_test, W1) + b1
A1 = np.tanh(Z1)

Z2 = np.dot(A1, W2) + b2
A2 = sigmoid(Z2)

y_pred = (A2 > 0.5).astype(int)

accuracy = np.mean(y_pred == y_test) * 100

print("Accuracy:", accuracy)