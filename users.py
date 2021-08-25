# Users: make a class called User. create two attributes called first_name and last_name and then create several
# other attributes that are stored in a user profile. Make a method called describe_user that prints a summary of the
# user's info. Make another method called greet_user that prints a personalized greeting.

# Login Attempts: add an attribute login_attempts to the User class. write a method called increment_login_attempts
# that increments the value by 1. Write another method called reset_login_attempts that resets the value of
# login_attempts to 0.
# make an instance of the User class and call increment_login_attempt several times. print the value of login_attempts
# to make sure it was incremented properly and then call reset_login_attempts. Print login_attempts again to make sure
# it was reset to 0

# Administrator: an admin is a special kind of user. write a class called Admin that inherits from User. add an
# attribute privileges that stores a list of strings. write a method show_privileges that lists the administrator's
# set of privileges. create an instance of Admin and call the method

# Privileges: write a separate Privileges class. The class should have one attribute, privileges that stores a list of
# strings. Move the show_privileges method to this class and make a Privileges instance as an attribute in the Admin
# class. Create a new instance of Admin and use your method to show the privileges.

class User:
    """Representation of a user"""
    def __init__(self, first_name, last_name, age, location):
        """Defining the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        """Printing the attributes"""
        print(f"\nThe user {self.first_name} {self.last_name} is {self.age} years old and lives in {self.location}.")

    def greet_user(self):
        """Printing a personalized greeting"""
        print(f"Hello {self.first_name} {self.last_name}! Welcome to our club!")

    def increment_login_attempts(self):
        """Method to increment the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Method to reset the login attempts to 0"""
        self.login_attempts = 0


class Admin(User):
    """Representation of an admin"""
    def __init__(self, first_name, last_name, age, location):
        """Defining the attributes"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


class Privileges:
    """Representation of the privileges class"""
    def __init__(self):
        """Defining the attributes"""
        self.privileges = ['can add post', 'can delete post', 'can add user', 'can ban user']

    def show_privileges(self):
        """Method to print the privileges"""
        print(f"\nAn admin has the following privileges: {self.privileges}")


user = User('John', 'McDonald', 44, 'New York')
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"\n{user.login_attempts} login attempts until now!")
user.reset_login_attempts()
print(f"{user.login_attempts} login attempts. Reset done!")

admin = Admin('Andrew', 'Melvin', 40, 'Prague')
admin.privileges.show_privileges()
