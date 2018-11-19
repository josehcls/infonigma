from flask import Flask, Response, request, render_template
import json
from v1.enigma import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hi'

@app.route('/v1/enigma')
def enigma():
    return render_template('index.html')


@app.route('/v1/enigma/group/<int:group>/lock/<int:lock>/passw/<passw>', methods=['GET'])
def unlock(group, lock, passw):
    print(group, lock, passw)
    status = get_lock_status(group, lock, passw)
    result = {"lock":lock, "passw": passw, "group": group, "status": "unlocked" if status else "locked"}
    return app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)
