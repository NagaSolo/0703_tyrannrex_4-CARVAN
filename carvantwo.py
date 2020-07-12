""" Second try
    Calculations during input stage
"""

cars_w_max_speed = 1
test = int(input())
for t in range(test):
    number_of_cars = int(input())
    for n in range(number_of_cars):
        first_input = int(input())
        next_input = int(input())
        if next_input >= first_input:
            cars_w_max_speed += 1
    print(cars_w_max_speed)