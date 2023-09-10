from flask import Flask, render_template

app = Flask(__name__)

data = dict()
news = ['Good', 'bad', 'like']
international = 2
business = 1
sports = 1

@app.route("/")
def index():
    data['news'] = news
    data['international'] = international
    data['business'] = business
    data['sports'] = sports

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()