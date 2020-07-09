# T (testcases) are between 1 to 100
# T = range(1, 100)

# first N (number of cars entering the line) are between 1 to 10_000
# second N (speed of each cars specified in first line) separated by space
# N = range(1,10_000)

def get_test_validity(test):
    T = range(1, 100)
    if test == any(T):
        return T
    else:
        exit()

def get_speed_validity(cars_number):
    N = range(1, 10_000)
    if cars_number == any(N):
        return cars_number

# def get_n_speeds()

# test = int(input())
# get_test_validity(test)

# for testcases in range(test):
#     n_speed_list = list(map(int, input().split()))

# t_input = int(input())
# if ((t_input in T) == True):
#     for test in range(t_input):
#         n_input = int(input())
#         answer = 1
#         if (n_input in N):
#             for n_speed in range(n_input):
#                 n_speed = list(map(int, input().split())) # accept input in a line
                # for speed in range(len(n_speed)):
                #     if (n_speed[speed+1]>n_speed[speed]):
                #         n_speed[speed+1]=n_speed[speed]
                #     else:
                #         answer += answer
                    # print(n_input, answer)
                print(n_speed)
        else:
            break