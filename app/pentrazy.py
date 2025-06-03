import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Pentrazy:
    def __init__(self):
        self.model = load_model('app/models/pentrazy_model.h5')
        with open('app/models/tokenizer.pkl', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        
        self.special_responses = {
            "siapa kamu": "Saya Sebuah AI yang dibuat khusus oleh SukaLebok06 untuk membantu anda tentang cybersecurity dan pentester, dapat juga membantu menyelesaikan permasalahan pada kodingan anda.",
            "who are you": "I am an AI created by SukaLebok06 to assist with cybersecurity and programming."
        }

    def get_response(self, question):
        lower_question = question.lower()
        
        # Check special questions
        for key in self.special_responses:
            if key in lower_question:
                return self.special_responses[key]
        
        # Process normal question
        sequence = self.tokenizer.texts_to_sequences([question])
        padded = pad_sequences(sequence, maxlen=20, truncating='post')
        prediction = self.model.predict(padded)
        predicted_index = np.argmax(prediction)
        
        # Load answers (in real implementation, map index to answer)
        return "Saya bisa membantu dengan pertanyaan programming dan cybersecurity. Berikan detail lebih spesifik."