from flask import Flask, render_template
from datetime import datetime
import requests, os, json, random

app = Flask(__name__)

def get_headline():
    filename = datetime.today().strftime('%Y-%m-%d') + '.json'
    try:
        with open(filename, 'r') as file:
            response = file.read()
            response = json.loads(response)
    except:
        url = 'https://api.newscatcherapi.com/v2/search'
        querystring = {"q":"\"Elon Musk\" AND (twitter OR Tesla OR SpaceX OR OpenAI OR Paypal)", "countries": "US, CA, UK", "lang":"en","sort_by":"relevancy","page":"1", "from": "two days ago"}
        API_KEY = os.getenv('NEWS_API_KEY')

        headers = {
            "x-api-key": API_KEY
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        with open(filename, 'w') as file:
            file.write(response.text)
        response = json.loads(response.text)

    if len(response['articles']) > 10:
        return response['articles'][random.randint(0, 9)]
    else:
        return response['articles'][random.randint(0, len(response['articles']-1))]

@app.route('/')
def home():
    response = get_headline()
    headline = response['title']
    source = response['clean_url']
    link = response['link']
    return render_template('home.html', headline = headline, source = source, link = link)