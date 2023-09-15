from flask import Flask, render_template, request, redirect
from helper import preprocessing, vectorizer, get_prediction
from logger import logging

app = Flask(__name__)

logging.info('...Flask server started...')

data = dict()
news = []
message = ""
actualCategory = []
actualInternational = 0
actualBusiness = 0
actualSports = 0
predictions = []
displayTexts = []
international = 0
business = 0
sports = 0



@app.route("/")
def index():
    data['news'] = news
    data['predictions'] = predictions
    data['message'] = message
    data['displayTexts'] = displayTexts
    data['actualCategory'] = actualCategory
    data['international'] = international
    data['business'] = business
    data['sports'] = sports
    data['actualInternational'] = actualInternational
    data['actualBusiness'] = actualBusiness
    data['actualSports'] = actualSports
    logging.info('...Open Home Page...')
    return render_template('index.html', data=data, message=message)

@app.route("/", methods = ['post'])
def my_post():
    text = request.form['text']
    category = request.form['category']

    if text =="" or category=="":
        return redirect(request.url)
    
    logging.info(f'Text : {text}')

    preprocessed_txt = preprocessing(text)
    logging.info(f'Preprocessed Text : {preprocessed_txt}')

    vectorized_txt = vectorizer(preprocessed_txt)
    logging.info(f'Vectorized Text : {vectorized_txt}')

    prediction = get_prediction(vectorized_txt)
    logging.info(f'Prediction : {prediction}')

    if category == 'International':
        global actualInternational
        actualInternational += 1
    elif category == 'Business':
        global actualBusiness
        actualBusiness += 1
    else:
        global actualSports
        actualSports += 1

    if prediction == category:
        global message
        message = "Predicted Correctly"
    else:
        message = "Unsuccessful Prediction"

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
    actualCategory.insert(0,category)
    displayTexts.insert(0, finalText)
    predictions.insert(0, prediction)
    return redirect(request.url)

@app.route('/moredetails')
def get_moreDetails():
    logging.info('...Open More Details Page...')
    return render_template('moreDetails.html', data=data)

@app.route('/clear_message')
def clear_message():
    global message
    message = ""
    return '', 204  # Return a response with no content


if __name__ == "__main__":
    app.run()