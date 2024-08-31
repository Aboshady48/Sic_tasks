import operator
dicts={'mohamed' : 1, 'age' : 18, 'aboshady' : 80}
print("our dictionary is: ",str(dicts))

result=dict()
first=list(dicts.values())
secound=list(set(first))

for i in secound:
    result[i]=operator.countOf(first,secound)
    
print("The frequency dictionary : " + str(result))