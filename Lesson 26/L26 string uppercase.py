class IOString():
    #constructor to set default value
    def __init__(self):
        self.str1 = ""

        #method to get input from user
        def get_String(self):
            self.str1 = input("Enter String: ")

        #method to print the string in upper case
        def print_String(self):
            print("Result is :", self.str1.upper())

#object creation
str_obj = IOString()

#call method
str_obj.get_String()
str_obj.print_String()