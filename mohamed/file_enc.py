class Student:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age 
    def get_name(self,):
        return self.__name
    
    def set_name(self,name):
        self.__name = name   

    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
    
    def geat_all_info(self):
        return f"Name: {self.__name}, Age - {self.__age}"  
    
std1 = Student("Alice", 20)
print(std1.geat_all_info())


std1 = Student("Alice", 20)
print(std1.get_name())
print(std1.get_age())
std1.set_age(21)
print(std1.get_age())
std1 = Student("Alice", 20)
std_name = std1.get_name()
print(std_name)
std1.set_name("Bob")
print(std1.get_name()) 
std1.set_name("Bob")
print(std1.get_name())










#class Car:
    #  def __init__(self, make, model):
     #   self.__make = make
      #  self.__model = model

   # def get_make(self):
    #    return self.__make

    #def set_make(self, make):
     #   self.__make = make

#    def get_model(self):
 #       return self.__model

  #  def set_model(self, model):
   #     self.__model = model
        
#my_car = Car("Toyota", "Corolla")
#print(my_car.get_make())
#print(my_car.get_model())
#my_car.set_make("Honda")
#my_car.set_model("Civic")
#print(my_car.get_make())
#print(my_car.get_model())