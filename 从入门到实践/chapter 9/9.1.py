class Restaurant():
    def __init__(self,restaurant_name,cuisine_type,people,number_served=0):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=number_served
        self.people=people

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def set_number_served(self,number_served):
        self.number_served=number_served

    def open_restauant(self):
        print('The restaurant is open now.')

    def increment_number_served(self,people):
        self.number_served+=people

restaurant=Restaurant('帅王思的餐厅','红烧孟头','4')
print(restaurant.restaurant_name,restaurant.cuisine_type,restaurant.number_served)
restaurant.describe_restaurant()
restaurant.open_restauant()
restaurant.set_number_served(4)
restaurant.increment_number_served(12)