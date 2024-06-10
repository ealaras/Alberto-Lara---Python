import tensorflow as tf
from tensorflow.keras import layers, models

# Cargar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# Normalizar las imágenes a valores de punto flotante entre 0 y 1
train_images = train_images / 255.0
test_images = test_images / 255.0

# Construir el modelo de red neuronal
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Convertir cada imagen de 28x28 en un vector de 784 elementos
    layers.Dense(128, activation='relu'),  # Capa completamente conectada con 128 unidades y activación ReLU
    layers.Dense(10, activation='softmax')  # Capa de salida con 10 unidades (una por clase) y activación softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=5)

# Evaluar el modelo
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'\nTest accuracy: {test_acc}')
