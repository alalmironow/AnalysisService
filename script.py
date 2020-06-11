from flask import Flask, request, abort, jsonify
from learn_neural_network import lemma_message
import pymorphy2
import pickle

app = Flask(__name__)

VECT_FILE = open("vect_dump.object", "rb")
VECT = pickle.load(VECT_FILE)
VECT_FILE.close()

CLASSIFIER_FILE = open("classifier_dump.object", "rb")
CLASSIFIER = pickle.load(CLASSIFIER_FILE)
CLASSIFIER_FILE.close()

MORPH = pymorphy2.MorphAnalyzer()

@app.route('/api/analysis-sentiment', methods=['POST'])
def define_sentiment():
	"""
	Определение тональности текста через кдассификатор

	Returns (json): 1 - позитивное, 0 - негативное
	""" 
	if not (request.json and request.json['message'] and request.json['message'].strip()):
		abort(404)
	message = request.json['message']
	lemma = lemma_message(message, morph = MORPH)
	vector = VECT.transform([lemma])[0]
	sentiment = CLASSIFIER.predict(vector)
	return jsonify(str(sentiment[0]))

app.run()