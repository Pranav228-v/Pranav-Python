# Taking the total amount as input from the user
Amount =int(input("Please enter amount for withdraw: "))

# Calculating the number of notes of different dnominations
note_1 = Amount // 100
note_2 = (Amount%100) // 50
note_3 = ((Amount%100)%50) //10

print("notes of 100 rupee ", note_1)
print("notes of 50 rupee ", note_2)
print("notes of 10 rupee", note_3)