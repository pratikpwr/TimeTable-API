import csv


class TimeModel:
    def __init__(self, college, branch, std, div):
        self.college = college
        self.branch = branch
        self.std = std
        self.div = div

    # temporary method
    @staticmethod
    def csv_to_json(csv_loc):

        my_dict = {}
        with open(csv_loc) as file:
            reader = csv.reader(file)
            first_row = next(reader)
            for row in reader:
                new_day_list = []
                count = 1
                while count < len(row):
                    new_period = {}

                    new_period.setdefault('course', row[count])
                    # new_period.setdefault('time', first_row[count])
                    new_period.setdefault('timeFrom', first_row[count].split('-')[0])
                    new_period.setdefault('timeTo', first_row[count].split('-')[1])

                    count += 1
                    new_day_list.append(new_period)
                    my_dict.setdefault(row[0], new_day_list)

        return my_dict
