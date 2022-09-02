# print("hello Blackwins tech")

# name= ["Lavanya" , 'Raj Mohan', "Shankar"]
# m = len(name)
# print
# for i in name :
#     print("{} welcome to blackwins tech ".format(i))
    
#class and objects
class Human :
    def __init__ (self, name , age ):
        self.name = name
        self.age = age
    def methods (self):
        print ( " Hi . My name is "+ self.name )

h1 = Human ( " Sherlock " , 60 )
h1.methods()
h2 = Human ( " Shankar " , 26 )


h2.methods()