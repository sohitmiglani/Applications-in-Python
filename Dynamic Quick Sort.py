# This algorithm is an adaptation of the recursive quick sort function to eliminate reiterations and use a memoized dynamic programming approach to reduce overlapping problems. 


import timeit
import random

eps = 1e-16
N = 10000
locations = [0.0, 0.5, 1.0 - eps]


def median(x1, x2, x3):
    for a in range(7):
        if x1 <= x2 <= x3:
            return x2
        # Every loop I'm shufflin
        (x1, x2, x3) = (x2, x1, x3)
        if a % 2:
            (x1, x2, x3) = (x3, x1, x2)


def qsort(lst):
    indices = [(0, len(lst))]

    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        partition = lst[0]

        # Split into lists:
        lower = [a for a in lst[frm:to] if a <= partition]
        upper = [a for a in lst[frm:to] if a > partition]

        ind1 = frm + len(lower)

        # Push back into correct place:
        lst[frm:ind1] = lower
        lst[ind1+1:to] = upper

        # Enqueue other locations
        indices.append((frm, ind1))
        indices.append((ind1, to))
    return lst


def randomized_quicksort():
    lst = range(N)
    random.shuffle(lst)
    return qsort(lst)


def test_quicksort():
    lst = randomized_quicksort()
    assert (lst == range(N))


# Is our algorithm correct
test_quicksort()

# How fast is our algorithm
print timeit.timeit(randomized_quicksort, number=1)
