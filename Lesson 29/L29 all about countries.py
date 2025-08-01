class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("India may be a diverse country but it's national language is Hindi.")

    def type(self):
        print("India is a developing country.")

#Class 2
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
    
    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

#object creation
obj_ind = India()
obj_usa = USA()

#common interface
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
    print()