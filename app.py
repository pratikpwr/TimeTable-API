from flask import Flask
from flask_restful import Api
from db import db
import os
from resources.timetable import Timetable
from resources.upload_csv import Upload

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'farCry'

api.add_resource(Timetable, '/timetable/<string:college>/<string:branch>/<string:std>/<string:div>')
api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run()
