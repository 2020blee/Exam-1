

#Defines a function
def grade_calc(arr):
    students = len(arr)

    #Sum starts at 0
    sum = 0
    #Adds up all the grades in the array
    for grade in arr:
        sum = sum + grade
    #Finds the average
    avg = sum / students
    #Checks where the average is and determines the donut count
    if avg >= 90:
        donuts = students
        print(donuts)

    elif avg >= 80:
        donuts = students / 2
        print(donuts)

    elif avg >= 70:
        donuts = students / 3
        print(donuts)

    else:
        donuts = students * -0.5
        print(donuts)

#The array of the grades
grades = [60, 70]

#Calling the function
grade_calc(grades)
