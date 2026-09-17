import tensorflow as tf
from tensorflow.keras import layers, models

# Load animal image dataset
train = tf.keras.utils.image_dataset_from_directory(
    "animals",
    image_size=(128, 128),
    batch_size=32,
    validation_split=0.2,
    subset="training",
    seed=1
)

test = tf.keras.utils.image_dataset_from_directory(
    "animals",
    image_size=(128, 128),
    batch_size=32,
    validation_split=0.2,
    subset="validation",
    seed=1
)

# Create CNN
model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(128,128,3)),

    layers.Conv2D(32, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D((2,2)),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(train.class_names), activation='softmax')
])

# Compile
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
model.fit(train, epochs=5)

# Test
loss, accuracy = model.evaluate(test)
print("Accuracy:", accuracy)

# Classes
print("Animal Classes:", train.class_names)