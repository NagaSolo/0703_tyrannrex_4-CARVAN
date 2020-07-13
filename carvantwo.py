""" Second try
    Calculations during input stage
"""

cars_w_max_speed = 1
test = int(input())
for t in range(test):
    number_of_cars = int(input())
    dynamic_input = [int(car_speed) for car_speed in input().split() if range(number_of_cars)]
    print(dynamic_input)