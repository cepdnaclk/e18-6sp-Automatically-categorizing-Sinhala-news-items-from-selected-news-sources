from flask import Flask, render_template, request, redirect
from helper import preprocessing, vectorizer, get_prediction
from logger import logging

app = Flask(__name__)

logging.info('...Flask server started...')

data = dict()
news = []
predictions = []
displayTexts = []
international = 0
business = 0
sports = 0



@app.route("/")
def index():
    data['news'] = news
    data['predictions'] = predictions
    data['displayTexts'] = displayTexts
    data['international'] = international
    data['business'] = business
    data['sports'] = sports
    logging.info('...Open Home Page...')
    return render_template('index.html', data=data)

@app.route("/", methods = ['post'])
def my_post():
    text = request.form['text']
    if text =="":
        return redirect(request.url)
    
    logging.info(f'Text : {text}')

    preprocessed_txt = preprocessing(text)
    logging.info(f'Preprocessed Text : {preprocessed_txt}')

    vectorized_txt = vectorizer(preprocessed_txt)
    logging.info(f'Vectorized Text : {vectorized_txt}')

    prediction = get_prediction(vectorized_txt)
    logging.info(f'Prediction : {prediction}')

    if prediction == 'International':
        global international
        international += 1
    elif prediction == 'Sport':
        global sports
        sports += 1
    else:
        global business
        business += 1
    
    splitText = text.split()
    first_five_words = ' '.join(splitText[:5])
    finalText = first_five_words + " = " + prediction

    news.insert(0, text)
    displayTexts.insert(0, finalText)
    predictions.insert(0, prediction)
    return redirect(request.url)

# @app.route('/', methods=['GET'])
# def get_pred

if __name__ == "__main__":
    app.run()