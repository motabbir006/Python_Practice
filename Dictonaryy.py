NBIU={
    "Motabbir": "He is a student of CSE department",#Key: Value  --- where Motabbir Key and He is student of CSE department is Value
    "Sourov":{ "Sarkar": "He innosent Boy in this class"}, #Key:Value(Subkey: Value)
    "Mahfuz": "Decent Boy in our class",
    'Saimin': "Best friend ever ",
    23: "Poor and ugly women", #Key name may any data type like a int
    'abir': [12,13,1,4,5,3,9],

}
print(NBIU["Motabbir"])# Print the value of Motabbir
print(NBIU ["Sourov"]["Sarkar"])# Print to subdirectorey at first call main then sub
print(NBIU['abir'])# print the list
#method(values,keys,update,get)

Vu={
    "Air": "BADLY NEEDED ",
    "rEsolution": "Higher Quality"
}

NBIU.update(Vu)# Update method
print(NBIU)
print("/n")

print(NBIU.keys())#Print only key values
print(list(NBIU.keys()))#Custing dic to list
print("/n")
print(NBIU.values())

print(NBIU.get(21))#When value is not present then show none
print(NBIU["21"])#Without get method When value is not present then show an error
