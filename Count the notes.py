# Taking total amount as input from user
Amount = int(input("Please Enter amount for withdraw : "))

# Calculating the number of notes of different denominations
note_1 = Amount // 100
note_2 = (Amount % 100) // 50
note_3 = ((Amount % 100) % 50) // 10

print("Number of 100 rupee" , note_1)
print("Number of 50 rupee" , note_2)
print("Number of 10 rupee" , note_3)