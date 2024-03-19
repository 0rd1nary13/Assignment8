def readData(filename, studentList):
    with open(filename, 'r') as file:
        for line in file:
            studentList.append(line.strip().split(','))
    return studentList


def checkGrade(num):
    if num >= 90:
        return 'A'
    elif num >= 80:
        return 'B'
    elif num >= 70:
        return 'C'
    elif num >= 60:
        return 'D'
    else:
        return 'F'


def displayData(studentList):
    print('Student ID\tName \t Midterm \t Final \t Average \t Grade')
    print('-------------------------------------------------------------')
    for student in studentList:
        average = (int(student[2]) + int(student[3])) / 2
        print(student[0], '\t', student[1], '\t', student[2], '\t', student[3], '\t', average, '\t',
              checkGrade(average))


def showMenu():
    print('1. Read data from file')
    print('2. Display data')
    print('3. Save data to file')
    print('4. Search data')
    print('5. Delete data')
    print('6. Update data')
    print('7. Quit')


def getData(studentList):
    studentID = input('Enter name: ')
    studentMajor = input('Enter major: ')
    while True:
        midterm = int(input('Enter midterm score: '))
        if 0 <= midterm <= 100:
            break
        else:
            print('Invalid score. Please enter a score between 0 and 100')


def saveData(studentList):
    with open("Data.txt", 'w') as file:
        for student in studentList:
            file.write(','.join(student) + '\n')


def main():
    students = []

    readData('data1.txt', students)

    displayData(students)

    choice = showMenu()

    while choice != 'Q':
        getData(students)

        displayData(students)

        choice = showMenu()

    saveData(students)


main()
