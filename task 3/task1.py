user=input("enter 5 word for a list: ")
user = user.split()#here i split the words in a list
lengthh_arr=len(user[0])#this var will take the len of the main array from the first index
for i in range (1,len(user)):#this for loop iterate from 1 to the end of the list
    if len(user[i])<lengthh_arr:#this condition show the shortest length of the word in the list
        lengthh_arr=len(user[i])
print("Length of minimum string is : " + str(lengthh_arr))
print("----------------")
print("the multple word in the array: ")
unique_List = []
duplicate_List = []
for k in user:#this loop iterate in the main array
    if i not in unique_List:#here i used logic gates for the if condtion
        unique_List.append(i)#here i put every element in the user array i put it in this array
    elif i not in duplicate_List:
        duplicate_List.append(i)
print(duplicate_List)