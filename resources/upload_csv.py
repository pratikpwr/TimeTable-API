from flask_restful import Resource
from flask import request
from models.time_model import TimeModel
import os


# noinspection PyBroadException
class Upload(Resource):

    @staticmethod
    def post():

        college = request.form.get('college')
        branch = request.form.get('branch')
        std = request.form.get('std')
        div = request.form.get('div')

        file_name = '{}_{}_{}_{}.csv'.format(college, branch, std, div)

        if request.files:
            csv_file = request.files['csv_file']
            try:
                file_end = csv_file.filename.rsplit('.')[1]
            except:
                return {'message': 'Upload Correct file'}

            if file_end not in ['csv', 'CSV']:
                return {'message': 'Upload Correct file'}

            try:
                csv_file.save(os.path.join("./assets/csv_files/", file_name))
            except:
                return {'message': 'Internal Error in saving File'}

            final_dict = TimeModel.csv_to_json('./assets/csv_files/{}'.format(file_name))
            return final_dict
