def count(l):
    #base case
    if not l:
        return 0
    #recursive case
    else:
        return 1 + count(l[1:])

my_list = [1, 2, 3, 4, 5]
summ = count(my_list)
print(summ)
