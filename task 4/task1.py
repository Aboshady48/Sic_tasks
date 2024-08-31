import json

file=open(r"C:\Users\abosh\Desktop\SIC\tasks\task 4\data.json","r")
db_list=json.load(file)
file.close()
#adding show
title=input("Enter the Show title: ")
year=input("Enter the relase year: ")
desc=input("Enter a show description: ")
show={
    "title":title,
    "years":year,
    "desc":desc
}
db_list.append(show)
print("show added successfully! ")
#saving with the newly added show
file=open(r"C:\Users\abosh\Desktop\SIC\tasks\task 4\data.json","w")
json.dump(db_list,file,indent=2)
file.close()
print("json data has been written to",r"C:\Users\abosh\Desktop\SIC\tasks\task 4\data.json")

#our new edditons
search=input("Search for your move: ")

if search in title:#here the search method to search in the db
        print("this is your move",search)
elif search not in title:
        print("your move hasn't found")
    
view=input("do you want to see our database, yes/no: ")
if view=="yes":#this view method to view the db
    
    for key,value in show.items():#this for loop for looping in all the json file and print it
        print("key: ")
        print(key,value)
        
elif view=="no":
    print("okay thanks")
else:
    print("you had typed yes or no wrong")

menu=input("If you want to , add show/remove show/search for a show: ")

remove=input("Enter name of the move that you need to remove: ")
key_to_remove="key to remove item"#this method to remove the item by it's title
if key_to_remove in title:
        remove=title.pop(key_to_remove)
    
    
#the menu method
if menu == "add show":
    print(title,year,desc)
    
elif menu == "remove show":
    print(key_to_remove)
    
elif menu == "search for a show":
    print(search)