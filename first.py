class AttendanceTracker:

    def __init__(self):
        self.present_students = []

    def mark_present(self, student_name: str):
       
        if student_name not in self.present_students:
            self.present_students.append(student_name)
            print(f"{student_name} marked as present.")
        else:
            print(f"{student_name} is already marked as present.")

    def remove_student(self, student_name: str):
       
        if student_name in self.present_students:
            self.present_students.remove(student_name)
            print(f"{student_name} removed from attendance list.")
        else:
            print(f"{student_name} is not in the attendance list.")

    def is_present(self, student_name:str) -> bool:

        return student_name in self.present_students

    def display_attendance(self):
   
        if self.present_students:
            print("Current attendance list:")
            for student in self.present_students:
                print(f"{student}")
        else:
            print("No students are present.")


t = AttendanceTracker()


n=int(input("enter the number of student"))

for i in range(2):


    a=input("enter the student name")
    t.mark_present({a})






t.display_attendance()


print("Is anshul present?", t.is_present("anshul"))


t.remove_student("vishwash")


t.display_attendance()


print("Is vishwash present?", t.is_present("vishwash"))

        
t.present_students = []





