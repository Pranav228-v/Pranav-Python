# Take input of number of units consumed from the user
units = int(input(" Please enter the Number of Units you Consumed: "))

# Check conditions of units consumed
# Then calculate amount and surcharge accordingly
# surcharge is the tax value

if(units < 50): # Check for units less than 50
    amount = units * 2.60
    surcharge = 25

elif(units <= 100): # Check for units less than 100
    amount = 130 + ((units - 50) * 5.26)
    surcharge = 35

elif(units <= 200): # Check for units less than or equal to 200
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 75

# Calculate and Display the total electricity bill
# total amount = amount + surcharge
total = amount + surcharge
print(f"Electricity Bill = {total}")