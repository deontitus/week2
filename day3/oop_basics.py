class Course:
    def __init__(self, name, price, seats):
        self.name = name
        self.price = price
        self.seats = seats

    # Display course info
    def display_info(self):
        print(f"Course: {self.name} costs ₹{self.price}")

    # Enroll student (reduce seats)
    def enroll_student(self):
        if self.seats > 0:
            self.seats -= 1
            print(f"Enrolled in {self.name}. Seats left: {self.seats}")
        else:
            print(f"No seats available in {self.name}")

    # Check status
    def check_status(self):
        if self.seats > 0:
            return "ACTIVE"
        else:
            return "FULL"


#Create Objects
course1 = Course("Full Stack Masterclass", 5000, 2)
course2 = Course("Generative AI & LLMs", 7000, 1)
course3 = Course("Advanced System Design", 10000, 0)

#Display Info
course1.display_info()
course2.display_info()
course3.display_info()

print()

#Enroll students
course1.enroll_student()
course1.enroll_student()
course1.enroll_student()  # extra to show full

print()

#Check status
print(f"{course1.name} Status:", course1.check_status())
print(f"{course2.name} Status:", course2.check_status())
print(f"{course3.name} Status:", course3.check_status())