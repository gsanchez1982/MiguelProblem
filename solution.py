# Problem:

# Consider the set of all the 7 digit numbers that can be obtained using, for each number,
# all the digits 1, 2, 3,..., 7.
# List the numbers of the set in increasing order and split the list exactly at the middle
# into two part of the same size. What is the last number of the first half?


# ANSWER BELOW:
# By Guillermo Sánchez Estrada
# Of Monterrey, Mexico

# First, we make a list of all numbers that matches the characteristics:
# ALL 7 digit numbers with the digits 1 to 7 in each digit.

n_set = []

for a in range(1,8):
    for b in range(1,8):
        for c in range(1,8):
            for d in range(1,8):
                for e in range(1,8):
                    for f in range(1,8):
                        for g in range(1,8):
                            n_set.append(int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)))

# Then we count them.

n_len = len(n_set)

# Then we divide the count by two and print the number in the middle.

n_mid = n_len / 2

print(n_set[n_mid])
