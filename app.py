from flask import Flask , request , jsonify
import requests
from textblob import TextBlob

app = Flask(__name__)
@app.route('/',methods=['POST'])
def API():
	query=request.get_json()
	newsTitleClasses={}
	for newsTitle in query['items']:
		analyzer=TextBlob(newsTitle)
		result=analyzer.sentiment.polarity
		if result<0:
			newsTitleClasses[newsTitle]="Negative"
		elif result==0:
			newsTitleClasses[newsTitle]="Neutral"
		elif result>0 and result<=1:
			newsTitleClasses[newsTitle]="Positive"

	return jsonify(newsTitleClasses)

if __name__ == '__main__':
    app.run()
