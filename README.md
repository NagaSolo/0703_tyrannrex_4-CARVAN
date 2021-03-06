### Overview
- repo: github.com/NagaSolo/0703_tyrannrex_4-CARVAN
- July 3rd, 2020 craft
- count maximum number of cars in a race with maximum speed at straight line

### Problem Summary
- One segment of the circuit in a race was a long straight road. 
- It was impossible for a car to overtake other cars on this segment.
- Therefore, a car had to lower down its speed if there was a slower car in front of it.
- How many cars were moving at their maximum speed.

- Formally, you're given the maximum speed of N cars in the order they entered the long straight segment of the circuit.
- Each car prefers to move at its maximum speed.
- If that's not possible because of the front car being slow, it might have to lower its speed.
- It still moves at the fastest possible speed while avoiding any collisions.
- For the purpose of this problem, you can assume that the straight segment is infinitely long.

- Count the number of cars which were moving at their maximum speed on the straight segment.

### Input
- The first line of the input contains a single integer T denoting the number of test cases to follow.
- Description of each test case contains 2 lines.
- The first of these lines contain a single integer N, the number of cars.
- The second line contains N space separated integers, denoting the maximum speed of the cars in the order they entered the long straight segment.

### Output
- For each test case, output a single line containing the number of cars which were moving at their maximum speed on the segment.

### Example

##### Sample Input:
3
1
10
3
8 3 6
5
4 5 1 2 3

##### Sample Output:
1
2
2

##### Constraints
1 ≤ T ≤ 100
1 ≤ N ≤ 10,000
All speeds are distinct positive integers that fit in a 32 bit signed integer.
Each input file will not be larger than 4 MB (4,000,000,000 bytes) in size.

##### WARNING! The input files are very large. Use faster I/O.