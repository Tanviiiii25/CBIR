import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Load the pre-trained VGG16 model without the top (fully connected) layers
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the pre-trained layers
for layer in base_model.layers:
    layer.trainable = False

# Add custom top layers for your specific task
x = Flatten()(base_model.output)
x = Dense(4096, activation='relu')(x)
x = Dense(4096, activation='relu')(x)
output = Dense(15, activation='softmax')(x)  # num_classes is the number of classes in your dataset

# Create the custom model
model = Model(inputs=base_model.input, outputs=output)

# Compile the model
model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Data augmentation for training
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
# Load and augment the training data
train_generator = train_datagen.flow_from_directory(
    r'E:\PILLAI ENGINEERING\Major Project\finalcode1\kashish\kashish practtt - Copy\static\training_set',  # Path to your training data
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

num_epochs = 5

# Training the model
history = model.fit(
    train_generator,
    steps_per_epoch=len(train_generator),
    epochs=num_epochs
)

# Save the trained model....E:\PILLAI ENGINEERING\Major Project\finalcode1\kashish\kashish practtt - Copy\2ndtrain
model.save(r'E:\PILLAI ENGINEERING\Major Project\finalcode1\kashish\kashish practtt - Copy\2ndtrain\vgg16_trained_model.h5')

# Plot training & validation accuracy values
plt.plot(history.history['accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train'], loc='upper left')
plt.show()

# For evaluation, you need to define and load your test data into test_generator
# Assuming you have a test data directory similar to training data
test_datagen = ImageDataGenerator(rescale=1.0 / 255)

test_generator = test_datagen.flow_from_directory(
    r'E:\PILLAI ENGINEERING\Major Project\finalcode1\kashish\kashish practtt - Copy\static\test_set',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# Evaluating the model
test_loss, test_accuracy = model.evaluate(test_generator, steps=len(test_generator))
print(f"Test accuracy: {test_accuracy}")
