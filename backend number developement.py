# todo - user evaluation of answer
# check distance for scoring otheriwse
# timer for 30 seconds displayed - somehow
# implement into tkinter
# print all solutions nicely
# print most optimal solution


import random
from random import randint
from random import sample


def making():
    big_options = [25, 50, 75, 100]
    small_options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_of_big = int(input("How many big numbers: "))
    lob = random.sample(big_options, number_of_big)  # length of big
    los = random.sample(small_options, (6 - number_of_big))  # length of low
    nums = [*los, *lob]
    target = randint(100, 999)
    print(f"The aim is to make {target} using {nums}")

    solutions = list()
    solve(target, nums, list(), solutions)
    unique = list()
    final = list()
    for s in solutions:
        a = ''.join(sorted(s))
        if not a in unique:
            unique.append(a)
            final.append(s)
    for s in final:  # print them out
        print(s)
    print(f"There are a total of {len(final)} solutions.")


def solve(target, nums, path, solutions):
    if len(nums) == 1:
        return
    distinct = sorted(list(set(nums)), reverse=True)
    remainder = list(distinct)
    for n1 in distinct:  # reduce list by combining a pair
        remainder.remove(n1)
        for n2 in remainder:
            rem2 = list(
                nums)  # in case of duplicates we need to start with full list and take out the n1,n2 pair of elements
            rem2.remove(n1)
            rem2.remove(n2)
            combine(target, solutions, path, rem2, n1, n2, '+')
            combine(target, solutions, path, rem2, n1, n2, '-')
            if n2 > 1:
                combine(target, solutions, path, rem2, n1, n2, '*')
                if not n1 % n2:
                    combine(target, solutions, path, rem2, n1, n2, '//')


def combine(target, solutions, path, rem2, n1, n2, symb):
    lst = list(rem2)
    ans = eval("{0}{2}{1}".format(n1, n2, symb))
    newpath = path + ["{0}{3}{1}={2}".format(n1, n2, ans, symb[0])]
    if ans == target:
        solutions += [newpath]
    else:
        lst.append(ans)
        solve(target, lst, newpath, solutions)


if __name__ == "__main__":
    making()
