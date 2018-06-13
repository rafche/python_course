import csv


def read_csv(path):
    temp_list = []
    with open(path) as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            temp_list.append(row)
    return temp_list


def find_duplicates(list_1, list_2):
    temp_list = []
    for element in list_1:
        if element in list_2:
            temp_list.append(element)
    return temp_list


if __name__ == '__main__':
    csv_1 = read_csv('student.csv')
    csv_2 = read_csv('student_II.csv')
    duplicates = find_duplicates(csv_1, csv_2)

    for element in duplicates:
        print(element)
