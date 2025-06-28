student = {
       "fname":"Gauri",
       "lname" : "Bhandigare",
       "age": 18,
       "hobby":"swimming",
       "address":"Grapes",
       "Grades":"A"
}
# print(student)
# print(student["hobby"])
# print(student["lname"])

# student["age"]=21  #change
# print(student)

# print(student.update({"Grade":"B"}))
# print(student) # using update

# print(student.pop("Grades"))
# print(student)        #pop

# print(student.popitem())
# print(student)     #popitem

# print(student.clear())
# print(student)      #clear

# for i in student:     #for loop
#     print(i,student[i])

# for i in student.keys():  #only key print
#     print(i)

# for i in student.values():
#     print(i)        #print only values


# for i in student.items():
#     print(i)       #show both val,key

# i= 0 
# while i<len(student):
#     print(i)             #while loop show only index values
#     i+=1 

# print(student.copy())
# print(student)        #copy

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# print(myfamily["child1"])
# print(myfamily["child1"]["year"])

for i,data in myfamily.items():
    print(i)
    for j in data:
        print(data,data[j])
         
