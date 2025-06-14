try:
    num1, num2 = eval(input("Enter two numbers seperated by comma: "))
    result = num1/num2
    print("Result is: ", result)
    print("Result is: ", result2) #this is error

except ZeroDivisionError:
    print("Division by zero is not allowed")

except SyntaxError:
    print("comma is missing. Enter numbers with seperated commas like this: 1, 2")

except ValueError:
    print("Please enter numerical value")

except NameError as ex:
    print("The exception is ",ex)

except:
    print("Some error has occurred")

else:
    print("no exception or no error")

finally:
    print("I will execute no matter what happens")