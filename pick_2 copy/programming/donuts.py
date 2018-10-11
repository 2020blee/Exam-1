


def grade_calc(arr):
    students = len(arr)

    sum = 0
    for grade in arr:
        sum = sum + grade

    avg = sum / students

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

grades = [60, 70]

grade_calc(grades)
