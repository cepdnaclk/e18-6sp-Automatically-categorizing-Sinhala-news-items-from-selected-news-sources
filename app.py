from flask import Flask, render_template

app = Flask(__name__)

data = dict()
news = ['international', 'business', 'sports']
international = 1
business = 2
sports = 3

@app.route("/")
def index():
    data['news'] = news
    data['international'] = international
    data['business'] = business
    data['sports'] = sports

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()