
class Student():
    def __init__(self):
        self.students = []
    def user_login(self):
        print("================== Student Management System ====================")
        o_username = "admin"
        o_password = 1234
        attempts = 0
        while attempts < 3:
            user = input("Enter Username: ")
            passw = int(input("Enter Password: "))
            if o_username == user and o_password ==passw:
                print("Login Successfully!")
                self.main_menu()
                return
            else:
                print('Oops, Try Again!')
                attempts+=1
                print(f"{3-attempts} attempts left")
                if attempts == 3:
                    print("You cannot access Portal")

    def add_student(self):
        print("=================== Add Student Details =========================")

        dict =  {
            'stu_id' : input("Enter Student Id: "),
            'name' : input("Enter Student Name: "),
            "age" : int(input("Enter Student Age: ")),
            "dept" : input('Enter Student Department: '),
            "percent": input("Enter Student Percentage: "),
            "city" :input("Enter Student City: "),
            "fees" :input("Fees Payed (Y/N): ")
        }
        self.students.append(dict)

    def  view_students(self):
        for i in range(len(self.students)):
            print("============================================================")
            print(f"Student ID: {self.students[i]['stu_id']}")
            print(f"Name: {self.students[i]['name']}")
            print(f"Age: {self.students[i]['age']}")
            print(f"Department: {self.students[i]['dept']}")
            print(f"Percentage: {self.students[i]['percent']}")
            print(f"City: {self.students[i]['city']}")
            print(f"Fees Status: {self.students[i]['fees']}")
            print("============================================================")
        print("No of students: ", len(self.students))
        print("============================================================")


    def search_students(self):
        search_id = input("Enter Student ID: ")
        for student in range(len(self.students)):
            if self.students[student]['stu_id'] == search_id:
                print("============================================================")
                print(f"Student ID: {self.students[student]['stu_id']}")
                print(f"Name: {self.students[student]['name']}")
                print(f"Age: {self.students[student]['age']}")
                print(f"Department: {self.students[student]['dept']}")
                print(f"Percentage: {self.students[student]['percent']}")
                print(f"City: {self.students[student]['city']}")
                print(f"Fees Status: {self.students[student]['fees']}")
                print("============================================================")
                break
            else:
                print("Student Id Doesn't Exists")

    def update_student(self):
        search_id = input("Enter Student id: ")
        for student in self.students:
            if student['stu_id'] == search_id:
                print("============================================================")
                print("1. Student Id")
                print("2. Name")
                print("3. Age")
                print("4. Department")
                print("5. Percentage")
                print("6. City")
                print("7. Fees")

                choice = int(input("Enter Number to Update: "))
                if choice == 1:
                    student['stu_id'] = input("Update Student Id: ")
                elif choice == 2:
                    student['name'] = input("Update Name: ")
                elif choice == 3:
                    student['age'] = int(input("Update Age: "))
                elif choice == 4:
                    student['dept'] = input("Update Department: ")
                elif choice == 5:
                    student['percent'] = input("Update Percentage: ")
                elif choice == 6:
                    student['city'] = input('Update City: ')
                elif choice == 7:
                    student['fees'] = input("Update Fees Status")
                else:
                    print("Invalid")
                print("Updated Successfully")
                print("============================================================")

    def delete_student(self):
        print("============================================================")
        search_id = input("Enter Student ID to Delete: ")
        for student in self.students:
            if student['stu_id'] == search_id:
                self.students.remove(student)
                print("student Deleted Successfully")
            else:
                print("Student Id not found")
        print("============================================================")

    def main_menu(self):
        is_flow = True
        while is_flow:
            print(f"1. Add Student")
            print(f"2. View Student")
            print(f"3. Search Students")
            print(f"4. Update students")
            print(f"5. Delete student")
            print(f"6. Exit")

            num = int(input("Enter Input to do what you want: "))
            if num == 1:
                self.add_student()
            elif num == 2:
                self.view_students()
            elif num == 3:
                self.search_students()
            elif num == 4:
                self.update_student()
            elif num == 5:
                self.delete_student()
            else:
                break
s1 = Student()
s1.user_login()
class Student():
    def __init__(self):
        self.students = []
    def user_login(self):
        print("================== Student Management System ====================")
        o_username = "admin"
        o_password = 1234
        attempts = 0
        while attempts < 3:
            user = input("Enter Username: ")
            passw = int(input("Enter Password: "))
            if o_username == user and o_password ==passw:
                print("Login Successfully!")
                self.main_menu()
                return
            else:
                print('Oops, Try Again!')
                attempts+=1
                print(f"{3-attempts} attempts left")
                if attempts == 3:
                    print("You cannot access Portal")

    def add_student(self):
        print("=================== Add Student Details =========================")

        dict =  {
            'stu_id' : input("Enter Student Id: "),
            'name' : input("Enter Student Name: "),
            "age" : int(input("Enter Student Age: ")),
            "dept" : input('Enter Student Department: '),
            "percent": input("Enter Student Percentage: "),
            "city" :input("Enter Student City: "),
            "fees" :input("Fees Payed (Y/N): ")
        }
        self.students.append(dict)

    def  view_students(self):
        for i in range(len(self.students)):
            print("============================================================")
            print(f"Student ID: {self.students[i]['stu_id']}")
            print(f"Name: {self.students[i]['name']}")
            print(f"Age: {self.students[i]['age']}")
            print(f"Department: {self.students[i]['dept']}")
            print(f"Percentage: {self.students[i]['percent']}")
            print(f"City: {self.students[i]['city']}")
            print(f"Fees Status: {self.students[i]['fees']}")
            print("============================================================")
        print("No of students: ", len(self.students))
        print("============================================================")


    def search_students(self):
        search_id = input("Enter Student ID: ")
        for student in range(len(self.students)):
            if self.students[student]['stu_id'] == search_id:
                print("============================================================")
                print(f"Student ID: {self.students[student]['stu_id']}")
                print(f"Name: {self.students[student]['name']}")
                print(f"Age: {self.students[student]['age']}")
                print(f"Department: {self.students[student]['dept']}")
                print(f"Percentage: {self.students[student]['percent']}")
                print(f"City: {self.students[student]['city']}")
                print(f"Fees Status: {self.students[student]['fees']}")
                print("============================================================")
                break
            else:
                print("Student Id Doesn't Exists")

    def update_student(self):
        search_id = input("Enter Student id: ")
        for student in self.students:
            if student['stu_id'] == search_id:
                print("============================================================")
                print("1. Student Id")
                print("2. Name")
                print("3. Age")
                print("4. Department")
                print("5. Percentage")
                print("6. City")
                print("7. Fees")

                choice = int(input("Enter Number to Update: "))
                if choice == 1:
                    student['stu_id'] = input("Update Student Id: ")
                elif choice == 2:
                    student['name'] = input("Update Name: ")
                elif choice == 3:
                    student['age'] = int(input("Update Age: "))
                elif choice == 4:
                    student['dept'] = input("Update Department: ")
                elif choice == 5:
                    student['percent'] = input("Update Percentage: ")
                elif choice == 6:
                    student['city'] = input('Update City: ')
                elif choice == 7:
                    student['fees'] = input("Update Fees Status")
                else:
                    print("Invalid")
                print("Updated Successfully")
                print("============================================================")

    def delete_student(self):
        print("============================================================")
        search_id = input("Enter Student ID to Delete: ")
        for student in self.students:
            if student['stu_id'] == search_id:
                self.students.remove(student)
                print("student Deleted Successfully")
            else:
                print("Student Id not found")
        print("============================================================")

    def main_menu(self):
        is_flow = True
        while is_flow:
            print(f"1. Add Student")
            print(f"2. View Student")
            print(f"3. Search Students")
            print(f"4. Update students")
            print(f"5. Delete student")
            print(f"6. Exit")

            num = int(input("Enter Input to do what you want: "))
            if num == 1:
                self.add_student()
            elif num == 2:
                self.view_students()
            elif num == 3:
                self.search_students()
            elif num == 4:
                self.update_student()
            elif num == 5:
                self.delete_student()
            else:
                break
s1 = Student()
s1.user_login()
