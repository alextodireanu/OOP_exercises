# Restaurant: make a class called Restaurant. The init method should store 2 attributes: restaurant_name and
# cuisine_type. Make a method called describe_restaurant that prints these two pieces of info and a method
# called open_restaurant that print a message indicating that the restaurant is open.
# make an instance called restaurant from your class, print the 2 attributes and then call both methods

# Number served: use the Restaurant class and add an attribute called number_served with a default value of 0.
# Create an instance called restaurant and print the number of customers served and then change the value and
# print again. Add a method called set_number_served that lets you set the number of customers that have been served.
# Call this method with a new number and print the value again. Add a method called increment_number_served that lets
# you increment with any number you like.

# Ice cream stand: write a class that inherits from the Restaurant class. add an attribute called flavors that stores
# a list of ice cream flavors. write a method that displays these flavors. create an instance of ice cream stand and
# call this method

class Restaurant:
    """Representing a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing attributes to describe a restaurant"""
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Printing the 2 attributes"""
        print(self.name)
        print(self.cuisine)

    def open_restaurant(self):
        """Showing that the restaurant is open"""
        print(f"The restaurant {self.name} is now open! Please come in :)")

    def set_number_served(self, customers_served):
        """Method that allows to set the number of customers served"""
        if customers_served >= self.number_served:
            self.number_served = customers_served
        else:
            print("You can't have served less customers than before")

    def increment_number_served(self, customers_served):
        """Method that allows to increment the number of customers served"""
        self.number_served += customers_served


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f'The flavors you chose are: {self.flavors}')


restaurant = Restaurant('BellaCiao', 'Italian')
print(restaurant.name)
print(restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('Big Belly Burger', 'American')
print(f"\n{restaurant.number_served} customers served :(")
restaurant.number_served = 25
print(f"{restaurant.number_served} customers served :)")
restaurant.set_number_served(44)
print(f"{restaurant.number_served} customers served :)")
restaurant.increment_number_served(2)
print(f"{restaurant.number_served} customers served :)")

ice_cream_shop = IceCreamStand('Gelato', 'Italian', 'strawberry, chocolate, vanilla')
ice_cream_shop.display_flavors()
