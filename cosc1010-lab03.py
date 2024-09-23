# Jake Huggins
# UWYO COSC 1010
# 09/23/2024
# Lab 03 
# Lab Section: 14 
# Sources, people worked with, help given to: None

# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 

print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list

state_list = ["Wyoming", "Colorado", "Montana"]

#print the entire list
print(state_list)

#now print the first element in the list
print(state_list[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(state_list[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{state_list[1].upper()} is south of {state_list[0].upper()}")

print("\nPart Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
state_list.append("Washington")
state_list.append("Oregon")
state_list.append("California")

print("\n")
print(state_list)

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
state_list[-2] = "Maine"

print("\n")
print(state_list)

#Insert the state Texas to be the third element in the list, again printing your list
state_list.insert(2, "Texas")

print("\n")
print(state_list)

#Using the `del` statement remove the fourth item from the list, print your list 
del state_list[3]

print("\n")
print(state_list)

#Remove Texas using its value, print the list
state_list.remove("Texas")

print("\n")
print(state_list)

print("\nPart Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print("Sorted:\n")
print(sorted(state_list))

print("Unsorted:\n")
print(state_list)

#Permanently sort your list in reverse order, printing it out
print("\n")
state_list.sort(reverse = True)
print(state_list)

#Using the reverse method reverse the list and print it
print("\n")
state_list.reverse()
print(state_list)
