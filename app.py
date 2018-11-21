from flask import Flask, request, Response, render_template, send_from_directory
import os
import json
from v1.enigma import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Vá para /v1/enigma/group/{número do seu grupo}'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/v1/enigma/group/<int:group>')
def enigma(group):
    if group not in [0, 1, 2, 3, 4, 5]:
        raise Exception('Grupo Indisponível')
    return render_template('index.html', group=group)

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
    # app.run(debug=True)
    app.run(host='0.0.0.0')
