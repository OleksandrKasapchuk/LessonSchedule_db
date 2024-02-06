from django_setup import *
from schedule_management.models import *

answered = True

while True:
    if answered:
        action = int(input("Choose the action, 1 - get information, 2 - add information, 3 - delete information "))
    if action == 1:
        choice = int(input("Which list do u want to look at? (1-grades,2-subjects,3-teachers,4-students) "))
        if choice == 1:
            data_list = Grade.objects.all()
        if choice == 2:
            data_list = Subject.objects.all()
        if choice == 3:
            data_list = Teacher.objects.all()
        if choice == 4:
            data_list = Student.objects.all()
        print("Here is the data list from the chosen table:")
        i = 0
        if len(data_list) > 0:
            for object in data_list: 
                i+=1
                print(f"{i}. {object}")
        else:
            print("No data is added yet")
    elif action == 2:
        answer = int(input("Enter a number, 1 - add grade, 2 - add subject, 3 - add teacher, 4 - add student "))
        answered = False
        if answer == 1:
            grade = Grade(name=input("Name of the grade: "))
            grade.save()
            answered = True
            print("The grade was added successfully")
        elif answer == 2:
            subject = Subject(name=input("Name of the subject: "))
            subject.save()
            answered = True
            print("The subject was added successfully")
        elif answer == 3:
            name=input("Name of the teacher: ")
            surname=input("Surname of the teacher: ")
            subject=input("His/her subject: ")
            try:
                get_subject = Subject.objects.get(name=subject)
                teacher = Teacher(name=name,surname=surname,subject=get_subject)
                teacher.save()
                answered = True
                print("The teacher was added successfully")
            except:
                print("There is no subject like that!!!")
        elif answer == 4:
            name=input("Name of the student: ")
            surname=input("Surname of the student: ")
            grade=input("His/her grade: ")
            try:
                get_grade = Grade.objects.get(name=grade)
                student = Student(name=name,surname=surname,grade=get_grade)
                student.save()
                answered = True
                print("The student was added successfully")
            except:
                print("There is no grade like that!!!")
        else:
            answered = True
    elif action == 3:
        choice = int(input("From which table do u want to delete information? (1-grades,2-subjects,3-teachers,4-students) "))
        if choice == 1:
            table = Grade
            needed_info = 1
        if choice == 2:
            table = Subject
            needed_info = 1
        if choice == 3:
            table = Teacher
            needed_info = 2
        if choice == 4:
            table = Student
            needed_info = 2
        if needed_info == 1:
            name = input("Name: ")
            object_to_delete = table.objects.filter(name=name).delete()
            if len(object_to_delete) > 0:
                print("Information was deleted successfully")
            else:
                print("Information does not exist")
        else:
            name = input("Name: ")
            surname = input("Surname: ")
            object_to_delete = table.objects.filter(name=name,surname=surname)
            if len(object_to_delete) > 0:
                object_to_delete.delete()
                print("Information was deleted successfully") 
            else:
                print("Information does not exist")
        answered = True
    else:
        break 