from flask import Flask
from flask_restful import Api

from resources.timetable import Timetable
from resources.upload_csv import Upload

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "D:/MyProjects/FlaskProjects/timetable/assets"
api = Api(app)

api.add_resource(Timetable, '/timetable')
api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
