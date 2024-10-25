from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

apiurl = 'http://127.0.0.1:8000'
@app.route('/')
def get_data():
    response = requests.get('{}/items'.format(apiurl))
    data = response.json()
    return render_template('index.html', data=data) 

if __name__ == '__main__':
    app.run(debug=True)