#Input the value of terms_
n = int(input("Enter the value of terms: "))
print()

sum = 0 #intialize sum value
i = 1 #intialize i value

while i <=n: #loop will run from 1 to n
    sum = sum + i
    i = i + 1

print("Sum= ", sum)