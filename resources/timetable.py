from flask_restful import Resource

from models.time_model import TimeModel


class Timetable(Resource):

    # gets data of user like class and div _/
    # search for specific data in DB
    # extract Db data to be return
    # return timetable in json format _/
    @staticmethod
    def get(college, branch, std, div):
        file_name = "{}_{}_{}_{}.csv".format(college, branch, std, div)
        csv_path = './assets/csv_files/{}'.format(file_name)
        my_dict = TimeModel.csv_to_json(csv_path)

        final_dict = {
            "college": college,
            "branch": branch,
            "std": std,
            "div": div,
            "timetable": my_dict
        }
        return final_dict
