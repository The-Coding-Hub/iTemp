from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        location = request.form['location']
        to_search = f"temperature in {location}"
        url = f"https://www.google.com/search?q={to_search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        result = f"Current Temperature in {location} is {temp}"
        with open('result.txt', 'w') as file:
            file.write(location + "\n" + temp + "\n" + result)
        with open('result.txt', 'r') as file:
            result = file.readlines()
    else:
        with open('result.txt', 'r') as file:
            result = file.readlines()
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
