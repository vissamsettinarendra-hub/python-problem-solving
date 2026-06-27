'''
what is polymorphism?
poly-->many
morphism->forms
same method/operators will behave differently

example:
print(5+3)#8
print("hello"+"world")  #helloworld
      same operator
         |
       but different behaviours
types of polymorphism
1.complie time 
2.run time

#complie time: metid overloading
#no method overloading in python

method overloading:

same method names
       +
diff parameters

# *args ----var len arguments

#java --->add(int,int)->add(int,int)
      --->add(int,int,int)

python approach:
class Calculator:
def add(self,a,b,c=0):
    print(a+b+c)
c1 = Calculator()
c1.add(10,20)
c1.add(10,20,30)          
'''
'''
#run time polymorphism:
# -->method overriding
'''
class Bird:
    def fly(self):
        print("Bird Flying")
class Eagle(Bird):
    def fly(self):
        print("eagle is flying")
e1 = Eagle()
#method is choosen during run time
e1.fly()

'''
#duck typing in python
#python focuses on
#behaviour not object type
'''
class Duck:
    def sound(self):
        print("Quack")
class Dog:
    def sound(self):
        print("bark")
def make_sound(obj):
    obj.sound()
d1=Duck()
d2=Dog()
make_sound(d1)
make_sound(d2)        
