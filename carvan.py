# T (testcases) are between 1 to 100
# T = range(1, 100)

# first N (number of cars entering the line) are between 1 to 10_000
# second N (speed of each cars specified in first line) separated by space
# N = range(1,10_000)

def test_validitor(test):
    # T = range(1, 100)
    if test >= 1 & test <=100:
        return test
    else:
        exit()

def cars_counter_validitor(numbers):
    # N = range(1, 10_000)
    if int(numbers) >= 1 & int(numbers) <= 10_000:
        return numbers
    else:
        exit()

def get_n_speeds(test, numbers):
    test_validitor(test)
    cars_counter_validitor(numbers)
    [[map(int, input().split(numbers)) in range(numbers)] for t in range(test)]

test = int(input())
numbers = input()
