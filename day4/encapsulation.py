class Student:
    school_name = "Lealabs Academy"

    def __init__(self, name, id_number):
        self.name = name                 # Public attribute
        self.id_number = id_number    # Private attribute

    # Getter method
    def get_id(self):
        return self.id_number

    # Setter method
    def set_id(self, new_id):
        if str(new_id).isdigit() and len(str(new_id)) == 4:
            self.id_number = new_id
            print("ID updated successfully.")
        else:
            print("Invalid ID! Must be a 4-digit number.")

    # Instance method
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

    # Class method
    @classmethod
    def school_info(cls):
        print(f"School Name: {cls.school_name}")


#Create object
student1 = Student("Deon", 1262)

#Public attribute access
print("Student Name:", student1.name)

#Try accessing private attribute directly
try:
    print(student1.id_number)
except AttributeError as e:
    print("Error:", e)

#Getter method
print("Student ID:", student1.get_id())

#Setter method (valid update)
student1.set_id(5678)
print("Updated ID:", student1.get_id())

#Setter method (invalid update)
student1.set_id(99)

#Instance method
student1.study("Python")

#Class method
Student.school_info()