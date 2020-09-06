from flask import Flask , request , jsonify
import requests
from textblob import TextBlob

app = Flask(__name__)
@app.route('/',methods=['GET'])
def API():
	query=request.args['Query']

	analyzer=TextBlob(query)
	result=analyzer.sentiment.polarity
	if result<0:
		return jsonify("Negative")
	elif result==0:
		return jsonify("Neutral")
	elif result>0 and result<=1:
		return jsonify("Positive")



if __name__ == '__main__':
    app.run()




