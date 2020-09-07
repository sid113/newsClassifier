from flask import Flask , request , jsonify
import requests
from textblob import TextBlob

app = Flask(__name__)
@app.route('/',methods=['POST'])
def API():
	query=request.get_json()
	newsTitleClasses={"classes":[]}
	for newsTitle in query['items']:
		temp={}
		analyzer=TextBlob(newsTitle)
		result=analyzer.sentiment.polarity
		if result<0:
			temp[newsTitle]="Negative"
		elif result==0:
			temp[newsTitle]="Neutral"
		elif result>0 and result<=1:
			temp[newsTitle]="Positive"
		newsTitleClasses['classes'].append(temp)	
	return jsonify(newsTitleClasses)

if __name__ == '__main__':
    app.run()
