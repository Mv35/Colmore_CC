import os
import json
from app import app as ClientApp
from flask import Flask, jsonify, request, redirect, render_template, url_for, session
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'
clientApp = ClientApp.ClientApp()

cors = CORS(app, resources={r"/search": {"origins": "http://localhost:port"},
                            r"/stats": {"origins": "http://localhost:port"},
                            r"/authenticate": {"origins": "http://localhost:port"},
                            r"/login": {"origins": "http://localhost:port"}})


@app.route('/stats', methods=['GET', 'POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def stats_form():
    symbol = request.form['search']
    data = session['data']
    stats = [x for x in data if symbol in x.values()]
    return render_template('stats.html', stats=stats[0])


@app.route('/authenticate', methods=['POST'])
def authenticate():
    if request.method == 'POST':
        if clientApp.authenticate(request.form['text']):
            session['authenticated'] = True
            return redirect(url_for('search_form'))
        return render_template('login.html')


@app.route('/login', methods=['GET'])
def login_form():
    if session.get('authenticated', None):
        return redirect(url_for('search_form'))
    return render_template('login.html')


@app.route('/')
def search_form():
    if clientApp._user:
        # if session.get('authenticated', None):
        return render_template('search.html')
    else:
        return render_template('login.html')


@ app.route('/search', methods=['GET', 'POST'])
@ cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def search():
    term = request.form['query']

    json_data = clientApp.symbol_search(term)
    # data = [entry['2. name'] for entry in json_data]
    data = json_data
    session['data'] = data
    resp = jsonify(data)

    resp.status_code = 200
    return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
