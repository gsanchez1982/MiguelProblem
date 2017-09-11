# Problem:

# Consider the set of all the 7 digit numbers that can be obtained using, for each number,
# all the digits 1, 2, 3,..., 7.
# List the numbers of the set in increasing order and split the list exactly at the middle
# into two part of the same size. What is the last number of the first half?


# ANSWER BELOW:
# By Guillermo Sanchez Estrada
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

# Then, we remove all items from the list that contain repeated digits.

i = '1234567'

x = []

n_len = len(n_set)

while n_len > 0:
    n_len = n_len - 1
    for n in i:
        count = str(n_set[n_len]).count(n)
        if count > 1:
            x.append(n_len)

x = list(set(x))

x = sorted(x, reverse=True)

for i in x:
    del n_set[i]


# Then we count all numbers in the new list.

n_len = len(n_set)


# Then we divide the count by two and divide into two sets of equal parts.

n_mid = int(n_len / 2)

h1 = n_mid - 1
h2 = (n_mid * 2) - 1

n1_set = n_set[0:h1]
n2_set = n_set[n_mid:h2]

# Finally, we print out the last number of the first half.

print(n1_set[-1])

# Answer printed out: 4376512
