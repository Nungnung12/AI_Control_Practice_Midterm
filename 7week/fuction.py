# # Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print (str)
#    return

# # Now you can call printme function
# printme("This is first call to the user defined function!")
# printme("Again second call to the same function")





# def printinfo( name, age ):
#     "This prints a passed info into this function"
#     print ("Name: ", name)
#     print ("Age ", age)
#     return

# printinfo( age = 50, name = "miki" )


# def printinfo( name, age = 35 ):
#    "This prints a passed info into this function"
#    print ("Name: ", name)
#    print ("Age ", age)
#    return

# printinfo( age = 50, name = "miki" )
# printinfo( name = "miki" )




# import support

# support.print_func("Zara")


# import math
# math.cos(math.pi/4)

# import time

# localtime = time.time.now
# print ("Local current time :", localtime)


# class Employee:
#    'Common base class for all employees'
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print ("Total Employee %d" % Employee.empCount)

#    def displayEmployee(self):
#       print ("Name : ", self.name,  ", Salary: ", self.salary)


# #This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
# #This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print ("Total Employee %d" % Employee.empCount)


class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

















