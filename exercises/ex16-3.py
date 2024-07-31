import tensorflow as tf

# Load the MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the input image so that each pixel value is between 0 to 1.
def normalize_img(image, label):
    return tf.cast(image, tf.float32) / 255., label

# Create a training pipeline
train_ds = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_ds = train_ds.map(normalize_img)
train_ds = train_ds.cache()
train_ds = train_ds.shuffle(60000)
train_ds = train_ds.batch(128)
train_ds = train_ds.prefetch(tf.data.AUTOTUNE)

# Create an evaluation pipeline
test_ds = tf.data.Dataset.from_tensor_slices((x_test, y_test))
test_ds = test_ds.map(normalize_img)
test_ds = test_ds.batch(128)
test_ds = test_ds.cache()
test_ds = test_ds.prefetch(tf.data.AUTOTUNE)

# Create and train the model
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(10)
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()],
)

model.fit(
    train_ds,
    epochs=6,
    validation_data=test_ds,
)

history = model.fit(
    train_ds,
    epochs=6,
    validation_data=test_ds,
)

test_loss, test_accuracy = model.evaluate(test_ds)

print(f"Overall test accuracy: {test_accuracy:.4f}")