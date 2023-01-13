PROPERTIES = ['StLastName', 'StFirstName', 'Grade', 'Classroom', 'Bus', 'GPA', 'TLastName', 'TFirstName']


def parse_data():
    file_data = []
    with open('students.txt', 'r') as file:
        for line in file:
            student_data = {}
            arr = line[:-1].split(',')
            for i, val in enumerate(arr):
                student_data[PROPERTIES[i]] = val
            file_data.append(student_data)
    return file_data


def filter_data():
    pass


if __name__ == '__main__':
    students_data = parse_data()
    while True:
        user_input = input("Enter a command: ")
        arr = user_input.split(' ')
        if arr[0][0] == 'Q':
            break
