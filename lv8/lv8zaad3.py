import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import load_model

data_df = pd.read_csv("cars.csv")
data_df = data_df.dropna()

X = data_df.drop(columns=['diesel'][][]).to_numpy()
y = data_df['diesel'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=5)

sc = MinMaxScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

model = keras.Sequential([
    layers.Input(shape=(X_train.shape[1],)),
    layers.Dense(units=12, activation="relu"),
    layers.Dense(units=8, activation="relu"),
    layers.Dense(units=4, activation="relu"),
    layers.Dense(units=1, activation="sigmoid")
])
model.summary()

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

history = model.fit(X_train, y_train, batch_size=5, epochs=100, validation_split=0.1)

model.save('Model/')

model = load_model('Model/')
score = model.evaluate(X_test, y_test, verbose=0)
print("Evaluacija mreže na testnom skupu podataka:")
for i in range(len(model.metrics_names)):
    print(f'{model.metrics_names[i]} = {score[i]}')

y_predictions = model.predict(X_test)
y_predictions = np.around(y_predictions).astype(np.int32)
cm = confusion_matrix(y_test, y_predictions)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.show()