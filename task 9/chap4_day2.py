import random

def lin_search(height):
    start_floor=random.randint(1,height)
    print(f"this is the hight of the built: {height}")
    return start_floor

def bin_search(height):
    left,right= 1, height
    
    while left < right:
        mid=(left+right)//2
        
        if mid==0:
            return mid
        elif mid > 0:
            left=mid+1
        else:
            right=mid-1
        return mid
    
build_hgiht=int(input("Enter the heghit: "))
lin_user_floor=lin_search(build_hgiht)
bin_user_floor=bin_search(build_hgiht)

print(f"liner search: chosen floor={lin_user_floor}")
print(f"binary search: chosen floor={bin_user_floor}")