from flask import Flask, redirect, url_for, render_template, request
import json
from difflib import get_close_matches

app = Flask(__name__)


data = json.load(open("data.json"))
suggestions = []


@app.route('/')
def home():

    return render_template('index.html', translate=data, suggestions=suggestions)


@app.route('/find')
def translate():

    # I should set it in a way that, if the user input is a 100% match, check from the json file,
    # else filter the data, and display options for the user to choose from
    user_input = request.args.get('user_input')
    user_input = user_input.lower()

    # user_input = request.args.get('display'), suggestion1=suggestions[1], suggestion2=suggestions[2]

    suggestions = []
    if user_input in data:
        word = data[user_input]

    elif user_input.upper() in data:
        word = data[user_input.upper()]

    elif user_input.capitalize() in data:
        word = data[user_input.capitalize()]

    elif len(get_close_matches(user_input, data.keys())) > 0:
        suggestions = get_close_matches(user_input, data.keys())
        word = "Please select the correct word by clicking it, or check your spellings and search again!"

    else:
        word = "Word does not exist"

    return render_template('index.html',  str=str, list=list, type=type(word), word=word, user_input=user_input, suggestions=suggestions)


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5002, debug=True)
