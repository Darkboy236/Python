#Input a word or sentence
string = input("Please Enter your own string : ")

string2 = ("")
#loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe Original String is : ", string)
print("\nThe Reversed String is : ", string2)