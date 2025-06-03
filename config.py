import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pentrazy-secret-key-2023'