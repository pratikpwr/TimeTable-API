from flask_restful import Resource, reqparse

from models.time_model import TimeModel


class Timetable(Resource):

    # gets data of user like class and div _/
    # search for specific data in DB
    # extract Db data to be return
    # return timetable in json format _/
    @staticmethod
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument('college', type=str, help="provide correct college name")
        parser.add_argument('branch', type=str, help="provide correct branch name")
        parser.add_argument('std', type=str, help="provide correct class name")
        parser.add_argument('div', type=str, help="provide correct division name")
        data = parser.parse_args()

        file_name = "{}_{}_{}_{}.csv".format(data['college'], data['branch'], data['std'],
                                             data['div'])

        csv_path = './assets/csv_files/{}'.format(file_name)
        my_dict = TimeModel.csv_to_json(csv_path)

        final_dict = {
            "college": data['college'],
            "branch": data['branch'],
            "std": data['std'],
            "div": data['div'],
            "timetable": my_dict
        }
        return final_dict
