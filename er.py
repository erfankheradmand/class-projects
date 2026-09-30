courses = []
total_unit = 0

while total_unit < 17 :
    teacher = input("Enter teacher name: ")
    title = input("Enter course title: ")
    unit = int(input("Enter unit: "))

    duration = int(input("Enter duration: "))
    course = {"title": title,"teacher" : teacher,"unit": unit,"duration": duration}
    courses.append(course)
    print("saved")
    total_unit += unit
    if total_unit + unit > 17 :
        print("Total unit is greater than 17")
        break
    else:

        for course in courses:
            print(f"{course['title']:10} by {course['teacher']:20} -- {course['unit']}")


