from flask import Flask
from flask_restful import Api

from resources.timetable import Timetable

app = Flask(__name__)

api = Api(app)

api.add_resource(Timetable, '/timetable')

if __name__ == '__main__':
    app.run(debug=True)
