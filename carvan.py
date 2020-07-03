# T (testcases) are between 1 to 100
T = range(1, 100)

# first N (number of cars entering the line) are between 1 to 10_000
# second N (speed of each cars specified in first line) separated by space
N = range(1,10_000)

t_input = int(input())
while t_input in T:
    n_input = int(input())
    while n_input in N == True:
        for i in range(n_input):
            n_speed = int(input().split())