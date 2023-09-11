from flask import Flask, render_template, request, redirect
from helper import preprocessing, vectorizer, get_prediction
from logger import logging

app = Flask(__name__)

logging.info("============Flask server started============")

data = dict()
news = []
international = 0
business = 0
sports = 0

@app.route("/")
def index():
    data['news'] = news
    data['international'] = international
    data['business'] = business
    data['sports'] = sports

    logging.info("============Home page opened============")

    return render_template('index.html', data=data)

@app.route("/", methods = ['post'])
def my_post():
    text = request.form['text']
    logging.info(f'Entered Text: {text}')

    preprocessed_txt = preprocessing(text)
    logging.info(f'Preprocessed Text: {preprocessed_txt}')

    vectorized_txt = vectorizer(preprocessed_txt)

    prediction = get_prediction(vectorized_txt)
    logging.info(f'Prediction: {prediction}')


    if prediction == 'International':
        global international
        international += 1
    elif prediction == 'Sport':
        global sports
        sports += 1
    else:
        global business
        business += 1

    news.insert(0, text)
    return redirect(request.url)

if __name__ == "__main__":
    app.run()