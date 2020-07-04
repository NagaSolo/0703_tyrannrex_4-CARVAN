# T (testcases) are between 1 to 100
T = range(1, 100)

# first N (number of cars entering the line) are between 1 to 10_000
# second N (speed of each cars specified in first line) separated by space
N = range(1,10_000)

t_input = int(input())
if (t_input in T):
    for test in range(t_input):
        n_input = int(input())
        if (n_input in N):
            for speed in range(n_input):
                n_speed = map(int, input().split())
                print(n_speed)