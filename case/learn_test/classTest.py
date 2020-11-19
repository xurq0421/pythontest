from collections import OrderedDict
from random import randint

class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.num_served = 0
    def describe_restaurant(self):
        print('餐馆名称：' + self.restaurant_name)
        print('餐饮类型：' + self.cuisine_type)
    def open_restaurant(self):
        print('餐馆正常营业！')
    def update_num_served(self,nums):
        self.num_served = nums
    def num_served_read(self):
        print('totle nums is :' + str(self.num_served))
    def increment_num_reverd(self,increment_nums):
        self.increment_nums_served = increment_nums + self.num_served
        print('today increment nums is :' + str(self.increment_nums_served))

restaunt = Restaurant('金百味','湘菜')
# print(restaunt.restaurant_name + '-----' + restaunt.cuisine_type)
# restaunt.describe_restaurant()
# restaunt.open_restaurant()
# restaunt.update_num_served(60)
# restaunt.num_served_read()
# restaunt.increment_num_reverd(70)



class Die():
    def __init__(self):
        self.sides = 6
    def roll_die(self):
        for i in range(10):
            print(randint(1,20))

die = Die()
die.roll_die()





