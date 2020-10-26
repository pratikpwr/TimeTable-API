import csv

lst = []
my_dict = dict()
dic = {
    'monday': {
        't1-t2': 'ADS'
    }
}
with open("D:\\MyProjects\\FlaskProjects\\timetable\\assets\\sitrc_comp_se_b.csv") as file:
    reader = csv.reader(file)
    row1 = next(reader)
    print(row1)
    for row in reader:
        # print(row)
        new = {}
        count = 0
        for i in row1:
            new.update({row1[count]: row[count]})
            count += 1
        my_dict.setdefault(row[0], new)


print(my_dict)
