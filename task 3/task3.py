my_tuple = (3, 7, 1, 9, 18)

print("The tuple is : ",my_tuple)
K = 2# this val for set the total of the lagre number
my_result = []#here i made array to put on it the largest value
my_tuple = list(my_tuple)
temp = sorted(my_tuple)#here sorting the tuple befor looping
for idx, val in enumerate(temp):
   if idx > K or idx >= len(temp) - K:
      my_result.append(val)
my_result = tuple(my_result)
print("The result is : ",my_result)