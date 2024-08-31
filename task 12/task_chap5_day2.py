lst=[8,1,0,6,4,7,9,2,3,5]
def part(ar, low, high):
    pivot = ar[high]
    index = low - 1
    for i in range(low, high):
        if ar[i] <= pivot:
            index += 1
            ar[index], ar[i] = ar[i], ar[index]
    ar[index + 1], ar[high] = ar[high], ar[index + 1]
    return index + 1
        
def quck_so(a, s=0, e=len(lst)-1):
    #base case with also the recrusive fun
    if s < e:
        p = part(a, s, e)
        quck_so(a, s, p - 1)
        quck_so(a, p + 1, e)

quck_so(lst)
print(lst)


try:
    user = int(input("Enter the number you want to find: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    user = None


def search(a, l, k, r):
    # Base case
    if l > r:
        return -1
        
    #recrusion case
    m = l + (r - l) // 2
    
    if a[m] == k:
        return m
    elif a[m] > k:
        return search(a, l, k, m - 1)
    else:
        return search(a, m + 1, k, r)

if user is not None:
    ans = search(lst, 0, user, len(lst) - 1)
    if ans != -1:
        print(f"Number found at index {ans}.")
    else:
        print("Number not found in the list.")
        