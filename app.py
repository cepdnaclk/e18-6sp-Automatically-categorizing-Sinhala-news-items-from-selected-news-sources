from flask import Flask, render_template, request, redirect
from helper import preprocessing, vectorizer, get_prediction

app = Flask(__name__)

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
    return render_template('index.html', data=data)

@app.route("/", methods = ['post'])
def my_post():
    text = request.form['text']
    preprocessed_txt = preprocessing(text)
    vectorized_txt = vectorizer(preprocessed_txt)
    prediction = get_prediction(vectorized_txt)

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