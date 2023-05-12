#Add the imported libraries here!
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from dotenv import load_dotenv
load_dotenv()
import requests, os, uuid, json
from flask import Flask, redirect, url_for, request, render_template, session
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

app = Flask(__name__)

#Getting Azure Credentials!
language_key = os.getenv("LANGUAGE_KEY")
language_endpoint = os.getenv("LANGUAGE_ENDPOINT")

subscription_key = os.getenv("SUBSCRIPTION_KEY")
endpoint = os.getenv("ENDPOINT")
credentials1 = CognitiveServicesCredentials(subscription_key)
client1 = ComputerVisionClient(endpoint, credentials1)


def authenticate_client():
    ta_credential = AzureKeyCredential(language_key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=language_endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

# Index page
@app.route('/')
def index():
    return render_template('index.html')

# Function 1
@app.route('/sentimentanalysis', methods=['GET', 'POST'])
def function1():
    if request.method == 'POST':

        original_text = request.form['text']
        documents = [original_text]

        result = client.analyze_sentiment(documents, show_opinion_mining=True)
        doc_result = [doc for doc in result if not doc.is_error]

        positive_reviews = [doc for doc in doc_result if doc.sentiment == "positive"]
        negative_reviews = [doc for doc in doc_result if doc.sentiment == "negative"]

        positive_mined_opinions = []
        mixed_mined_opinions = []
        negative_mined_opinions = []

        for document in doc_result:
            sentiment = document.sentiment
            positive_confidence_scores = document.confidence_scores.positive
            negative_confidence_scores = document.confidence_scores.negative
            neutral_confidence_scores = document.confidence_scores.neutral
        return render_template(
            'function1.html', 
            sentiment = sentiment, 
            positive_confidence_scores = positive_confidence_scores,
            negative_confidence_scores = negative_confidence_scores,
            neutral_confidence_scores = neutral_confidence_scores
            )
    return render_template('function1.html')

# Function 2
@app.route('/keyphraseextration', methods=['GET', 'POST'])
def function2():
    if request.method == 'POST':
        # Get user input
        #text = request.form['text']

        # Perform function 2 on the input
        #result = function2_logic(text)

        original_text = request.form['text']
        documents = [original_text]
        for n in range(0, len(documents)):
            response = client.extract_key_phrases(documents)[n]
        for phrase in response.key_phrases:
            phrase = phrase
        return render_template(
            'function2.html', 
            documents = documents,
            phrase = phrase
            )

        #return render_template('function2.html', result=result)
    return render_template('function2.html')

# Function 3
@app.route('/imageanalysis', methods=['GET', 'POST'])
def function3():
    if request.method == 'POST':
        # Get user input
        image_url = request.form.get('image_url')


        # Call the Azure Cognitive Vision API to analyze the image
        result = client1.analyze_image(image_url, visual_features=['Categories', 'Description'])

        # Process the result as per your application's needs
        categories = result.categories
        description = result.description

        return render_template('function3.html', 
                               categories=categories, 
                               description=description
                               )

    return render_template('function3.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
