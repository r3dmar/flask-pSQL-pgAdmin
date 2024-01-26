from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import random

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{os.environ.get('DIALECT')}://{os.environ.get('USERNAME')}:{os.environ.get('PASSWORD')}@{os.environ.get('HOST')}:{os.environ.get('PORT')}/{os.environ.get('DATABASE')}"
db = SQLAlchemy(app)

class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(80))

    def __repr__(self):
        return f'<ExampleModel {self.id}>'


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/add_random_data', methods=['POST'])
def add_random_data():
    random_data = ExampleModel(data=str(random.randint(1, 1000)))
    db.session.add(random_data)
    db.session.commit()
    return f"Added: {random_data}"


@app.route('/delete_all_data', methods=['DELETE'])
def delete_all_data():
    db.session.query(ExampleModel).delete()
    db.session.commit()
    return "All data deleted"


if __name__ == '__main__':
    app.run(debug=True, port=5000)

