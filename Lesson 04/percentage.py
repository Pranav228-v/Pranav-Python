# Takes marks as input from the user
print("Enter the marks obtained in 3 subjects:")

math = int(input("maths: "))
english = int(input("english: "))
science = int(input("science: "))

# Let's calulate the percentage of marks
sum = math + english + science
print("Sum of math, english and science")

perc = (sum/300)*100

print(f"Percentage mark = {perc}")