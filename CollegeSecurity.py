import numpy as np
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Flatten, Dense

# Load face dataset
data = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

X = data.images
y = data.target

# Reshape and normalize
X = X.reshape(-1, X.shape[1], X.shape[2], 1) / 255.0

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build CNN
model = Sequential([
    Conv2D(32, (3,3), activation='relu',
           input_shape=X.shape[1:]),
    MaxPooling2D((2,2)),

    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),

    Flatten(),

    Dense(128, activation='relu'),
    Dense(len(data.target_names), activation='softmax')
])

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(
    X_train, y_train,
    epochs=5,
    validation_data=(X_test, y_test)
)

# Test
loss, accuracy = model.evaluate(X_test, y_test)

print("Accuracy:", accuracy)

# Prediction
prediction = model.predict(X_test[:1])
print("Predicted:", data.target_names[np.argmax(prediction)])
print("Actual:", data.target_names[y_test[0]])