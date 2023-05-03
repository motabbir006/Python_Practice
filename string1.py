text="Hello "
new="world"
print( text + new)# string Concetetion

print(text[3]) #Show index value

#Slicing
print(new[0:3])
#skip
print(new[0::2])#skip 4index

#Few string function

print(len(text)) #length of text
print(new.endswith("d"))# check end string
print(text.count("H")) # count how many same text there
print(new.capitalize()) # capatalize the word
print(new.find("d")) #find the index of d
print(new.replace("o","a"))# replace the index value