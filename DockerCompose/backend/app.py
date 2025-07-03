from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Juan",
        "lastname": "Patarroyo",
        "socialMedia":
        {
            "facebookUser": "OsumeP",
            "instagramUser": "OsumeP",
            "xUser": "OsumeP",
            "linkedin": "OsumeP",
            "githubUser": "OsumeP"
        },
        "blog": "No hay XD",
        "author": "Juan David Patarroyo"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)