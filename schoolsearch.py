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


def filter_student(student_data, student_name, print_bus):
    for student in student_data:
        if student['StLastName'] == student_name:
            if print_bus:
                print(f'Last Name: {student["StLastName"]}\n '
                      f'First Name: {student["StFirstName"]}\n '
                      f'Bus Route: {student["Bus"]}\n')
            else:
                print(f'Last Name: {student["StLastName"]}\n '
                      f'First Name: {student["StFirstName"]}\n '
                      f'Grade: {student["Grade"]}\n '
                      f'Classroom: {student["Classroom"]}\n')


def filter_teacher(student_data, teacher_name):
    for student in student_data:
        if teacher_name == student['TLastName']:
            print(f'Last Name: {student["StLastName"]}\n '
                  f'First Name: {student["StFirstName"]}\n ')


def filter_grade(student_data, grade):
    for student in student_data:
        if grade == student['Grade']:
            print(f'Last Name: {student["StLastName"]}\n '
                  f'First Name: {student["StFirstName"]}\n ')


def filter_bus(student_data, bus):
    for student in student_data:
        if bus == student['Bus']:
            print(f'Last Name: {student["StLastName"]}\n '
                  f'First Name: {student["StFirstName"]}\n '
                  f'Grade: {student["Grade"]}\n '
                  f'Classroom: {student["Classroom"]}\n')


def compute_average(student_data, grade):
    # Add error checking if no students are found
    average = 0

    print(f'Average GPA for students with a grade of {grade}: {average}')

def filter_student():
    pass
def filter_teacher():
    pass
def filter_bus():
    pass
def filter_grade(High,num):
    pass
def filter_avg():
    pass

if __name__ == '__main__':
    students_data = parse_data()    
    while True:
        user_input = input("Enter a command: ")
        arr = user_input.split(' ')
        print(arr)
        if(arr[0][0] == "S"):
            filter_student()
        elif(arr[0][0] == "T"):
            filter_teacher()
        elif(arr[0][0] == "B"):
            filter_bus()
        elif(arr[0][0] == "G"):
            filter_grade()
        elif(arr[0][0] == "A"):
            filter_avg()
        elif(arr[0][0] == "I"):
            print("S[tudent]: <lastname> [B[us]]\nT[eacher]: <lastname>\nB[us]: <number>\nG[rade]: <number> [H[igh]|L[ow]]\nA[verage]: <number>\nI[nfo]\nQ[uit]\n")
        if arr[0][0] == 'Q':
            break
