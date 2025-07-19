class Employee:
    #initializing constructor
    def __init__(self):
        print("Employee created")

    #calling destructor
    def __del__(self):
        print("Destruction called")

#function outside of the class
def Create_obj():
    print("Making Object...")
    obj = Employee()

    print("function end...")
    return obj

print("Calling Create_obj() function...")
object_1 = Create_obj()

print("Program End...")