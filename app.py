from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
load_dotenv()
import requests, os, uuid, json
from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)

language_key = os.getenv("LANGUAGE_KEY")
language_endpoint = os.getenv("LANGUAGE_ENDPOINT")
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
@app.route('/function1', methods=['GET', 'POST'])
def function1():
    if request.method == 'POST':
        # Get user input
        text = request.form['text']

        # Perform function 1 on the input
        result = function1_logic(text)

        return render_template('function1.html', result=result)
    return render_template('function1.html')

# Function 2
@app.route('/function2', methods=['GET', 'POST'])
def function2():
    if request.method == 'POST':
        # Get user input
        text = request.form['text']

        # Perform function 2 on the input
        result = function2_logic(text)

        return render_template('function2.html', result=result)
    return render_template('function2.html')

# Function 3
@app.route('/function3', methods=['GET', 'POST'])
def function3():
    if request.method == 'POST':
        # Get user input
        text = request.form['text']

        # Perform function 3 on the input
        result = function3_logic(text)

        return render_template('function3.html', result=result)
    return render_template('function3.html')

# Function 4
@app.route('/function4', methods=['GET', 'POST'])
def function4():
    if request.method == 'POST':
        # Get user input
        text = request.form['text']

        # Perform function 4 on the input
        result = function4_logic(text)

        return render_template('function4.html', result=result)
    return render_template('function4.html')

# Function 1 logic
def function1_logic(text):
    # Perform function 1 operations on the text
    # Replace this with your actual function logic
    result = text.upper()
    return result

# Function 2 logic
def function2_logic(text):
    # Perform function 2 operations on the text
    # Replace this with your actual function logic
    result = text.lower()
    return result

# Function 3 logic
def function3_logic(text):
    # Perform function 3 operations on the text
    # Replace this with your actual function logic
    result = text[::-1]  # Reverse the text
    return result

# Function 4 logic
def function4_logic(text):
    # Perform function 4 operations on the text
    # Replace this with your actual function logic
    result = text + '!'
    return result

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
