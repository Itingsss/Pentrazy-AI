import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
data = pd.concat([
    pd.read_csv('training/dataset/programming.csv'),
    pd.read_csv('training/dataset/cybersecurity.csv')
])

# Preprocessing
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(data['question'])
sequences = tokenizer.texts_to_sequences(data['question'])
padded = pad_sequences(sequences, maxlen=20, truncating='post')

# Save tokenizer
with open('app/models/tokenizer.pkl', 'wb') as f:
    pickle.dump(tokenizer, f)

# Model architecture
model = Sequential([
    Embedding(5000, 64, input_length=20),
    LSTM(64),
    Dense(64, activation='relu'),
    Dense(len(data['answer'].unique()), activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])

model.fit(padded, data['answer'], epochs=10)
model.save('app/models/pentrazy_model.h5')