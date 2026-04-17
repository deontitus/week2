#Parent Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"User {self.username} logged in.")


#Child Class (Inheritance)
class Admin(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions

    # Method Overriding
    def login(self):
        print(f"Admin {self.username} logged in with full access.")

    # Specialized Method
    def delete_user(self):
        print(f"Admin {self.username} can delete users.")


#Create Objects
user1 = User("user", "user@email.com")
admin1 = Admin("admin", "admin@email.com", "all")

#Polymorphism
users = [user1, admin1]

for u in users:
    u.login()

print()

#Admin specific method
admin1.delete_user()

#This will cause error if uncommented (User cannot access admin method)
#user1.delete_user()