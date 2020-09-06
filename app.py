from flask import Flask , request , jsonify
import requests
from textblob import TextBlob

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def API():
	query=request.get_json()
	newsTitleClasses={'classes':[]}
	for newsTitle in query['items']:
		analyzer=TextBlob(newsTitle)
		result=analyzer.sentiment.polarity
		if result<0:
			newsTitleClasses['classes'].append("Negative")
		elif result==0:
			newsTitleClasses['classes'].append("Neutral")
		elif result>0 and result<=1:
			newsTitleClasses['classes'].append("Positive")

	return jsonify(newsTitleClasses)

if __name__ == '__main__':
    app.run()
