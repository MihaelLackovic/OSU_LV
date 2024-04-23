import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix


# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# train i test podaci
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# prikaz karakteristika train i test podataka
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))

# TODO: prikazi nekoliko slika iz train skupa
plt.imshow(x_train[2])
plt.show()
plt.imshow(x_train[4])
plt.show()
plt.imshow(x_train[7])
plt.show()


# skaliranje slike na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# slike trebaju biti (28, 28, 1)
x_train_s = np.expand_dims(x_train_s, -1)
x_test_s = np.expand_dims(x_test_s, -1)

print("x_train shape:", x_train_s.shape)
print(x_train_s.shape[0], "train samples")
print(x_test_s.shape[0], "test samples")


# pretvori labele
y_train_s = keras.utils.to_categorical(y_train, num_classes)
y_test_s = keras.utils.to_categorical(y_test, num_classes)


# TODO: kreiraj model pomocu keras.Sequential(); prikazi njegovu strukturu
model = keras . Sequential ()
model . add ( layers . Input (shape =(2 , ) ))
model . add ( layers . Dense (4,activation ="relu") )
model . add ( layers . Dense (2,activation ="sigmoid") )
model . summary ()


# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model . compile ( loss =" categorical_crossentropy " ,
optimizer =" adam ",
metrics = [" accuracy " ,])

# TODO: provedi ucenje mreze
batch_size = 128
epochs = 10
model.fit(x_train_s, y_train_s, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# Evaluacija modela na testnom skupu
test_loss, test_acc = model.evaluate(x_test_s, y_test_s)
print("Test accuracy:", test_acc)

# Predikcija mreze za testni skup podataka
y_pred = model.predict(x_test_s)
y_pred_classes = np.argmax(y_pred, axis=1)
conf_matrix = confusion_matrix(y_test, y_pred_classes)
print("Confusion Matrix:")
print(conf_matrix)

# Spremanje modela
model.save("savee.h5")
