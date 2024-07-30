import numpy as np
import matplotlib.pyplot as plt

def transform_data(X):
    transformed = []
    for x in X:
        if x[0] > 0 and x[1] > 0:
            transformed.append([1, 1])
        elif x[0] < 0 and x[1] < 0:
            transformed.append([-1, -1])
        elif x[0] > 0 and x[1] < 0:
            transformed.append([1, -1])
        else:
            transformed.append([-1, 1])
    return np.array(transformed)

def train_test_split(X, y, test_size=0.2):
    n_samples = len(X)
    n_test = int(n_samples * test_size)
    indices = np.random.permutation(n_samples)
    test_indices = indices[:n_test]
    train_indices = indices[n_test:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

np.random.seed(0)
X = np.random.randn(200, 2) * 5
y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0).astype(int)

X_transformed = transform_data(X)

X_train, X_test, y_train, y_test = train_test_split(X_transformed, y)

class SimplePerceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=100):
        self.weights = np.random.randn(input_size)
        self.bias = np.random.randn(1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias > 0

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, yi in zip(X, y):
                y_pred = self.predict(xi)
                self.weights += self.learning_rate * (yi - y_pred) * xi
                self.bias += self.learning_rate * (yi - y_pred)

model = SimplePerceptron(input_size=2)
model.train(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = np.mean(y_pred == y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")

plt.figure(figsize=(10, 8))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
plt.title('XOR Classification Results')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()