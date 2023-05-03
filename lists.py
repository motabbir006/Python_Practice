Id=[6,87,54,89,56,21,23]
print(Id)
Id.sort()#Print assending order 
print(Id)
Id.reverse()#Print reverse site
print(Id)
Id.append(234)# Add the number in last index
print(Id)

Id.pop(4)# Delete the value of index 4
print(Id)

Id.insert(2,120) #Inser 120 in index number 2
print(Id)

Id.remove(120)
print(Id)


# create different item in list

Differ=["Abir", True, 100, 12.34]
print(Differ)

print(Id[2]) #Print the value of index number 2
#index always start with zero


#Possible too change index value in list 

Id[3]= 456 # Change the value of index number 3
print(Id)

#list Slicing
print(Id[1:4])