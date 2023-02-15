from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from flask_sqlalchemy import SQLAlchemy

from flask_cors import CORS

from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import OperationalError

from baxtableep import Baxtableep 

import os
import uuid

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "responses.db"))

app = Flask(__name__, static_url_path='')
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

baxter = Baxtableep()

CORS(app)

db: SQLAlchemy = SQLAlchemy(app)

class Entry(db.Model):
    result = db.Column(db.Integer, nullable=False)
    probability = db.Column(db.Float, nullable=False)
    text = db.Column(db.String(240), primary_key=True)

with app.app_context():
    db.create_all()
    
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        text = request.form['body']
    except KeyError:
        return 'Invalid Request From, Must Contain Body', 400

    if not text or len(text) > 240:
        return 'Invalid Request, Body Cannot Be Empty Or Over 240 Charachters', 400

    probs: float = baxter.predict_probs([text])[0]
    result: int = baxter.predict([text])[0]

    try: 
        # Write to database
        entry = Entry(result=int(result), probability=float(probs), text=text)
        db.session.add(entry)
        db.session.commit()
    except OperationalError:
        # Database isnt working
        return 'Unable to write to database, please report this', 500
    except IntegrityError:
        # If duplicate text is given do not overwrite entry
        pass

    return jsonify({
        "body": text,
        "probability": float(probs),
        "isProfane": int(result),
    }), 200
    

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="0.0.0.0")