from flask import jsonify, request, render_template
from app import app, pentrazy_ai

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    response = pentrazy_ai.get_response(question)
    return jsonify({'response': response})