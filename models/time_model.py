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
            row1 = next(reader)
            for row in reader:
                new = {}
                count = 1
                while count < len(row):
                    new.update({row1[count]: row[count]})
                    count += 1
                my_dict.setdefault(row[0], new)

        return my_dict
