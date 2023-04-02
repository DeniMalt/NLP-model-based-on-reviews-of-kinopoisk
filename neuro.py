import json
from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from numpy.lib.npyio import load
with open("Путь к файлу с отзывами", "r") as rfile:
  ld = json.load(rfile)
 
reviews = []
reviews += ld[0]['positive']
reviews += ld[1]['negative']
reviews += ld[2]['neutral']
 
labels = [1 for i in range(73469)] + [-1 for i in range(7653)] + [0 for i in range(10245)]
 
max_len = 1000
training_samples = 5000
max_words = 10000
tokenizer = Tokenizer(max_words)
tokenizer.fit_on_texts(reviews)
 
sequences = tokenizer.texts_to_sequences(reviews)
word_index = tokenizer.word_index
data = pad_sequences(sequences, maxlen=max_len)
 
labels = np.asarray(labels)
def to_one_hot(labels, dimension=3):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label] = 1
    return results
 
labels = to_one_hot(labels)
indices = np.arange(30000)
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
 
X_train = data[:training_samples]
y_train = labels[:training_samples]
X_test = data[training_samples:]
y_test = labels[training_samples:]
 
from keras.models import Sequential
from keras.layers import Embedding, Flatten, Dense
 
model = Sequential()
model.add(Embedding(max_words, 500, input_length=max_len))
model.add(Flatten())
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.summary()
 
model.compile(optimizer='rmsprop',
                     loss='categorical_crossentropy',
                     metrics=['acc'])
model_history = model.fit(X_train, y_train,
                                        epochs=10,
                                        batch_size=32,
                                        validation_split=0.2)
 
import matplotlib.pyplot as plt
 
loss = model_history.history['loss']
val_loss = model_history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'bo', label='Потери при обучении')
plt.plot(epochs, val_loss, 'b', label='Потери при проверке')
plt.title('Потери при обучении и проверке',  fontsize=18)
plt.xlabel('Итерации',  fontsize=16)
plt.ylabel('Потери',  fontsize=16)
plt.legend()
plt.show()
 
plt.clf()
acc = model_history.history['acc']
val_acc = model_history.history['val_acc']
plt.plot(epochs, acc, 'bo', label='Точность при обучении')
plt.plot(epochs, val_acc, 'b', label='Точность при проверке')
plt.title('Точность при обучении и проверке',  fontsize=18)
plt.xlabel('Итерации',  fontsize=16)
plt.ylabel('Точность',  fontsize=16)
plt.legend()
plt.show()
 
model.evaluate(X_train, y_train)
