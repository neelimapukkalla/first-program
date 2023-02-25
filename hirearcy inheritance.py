class father:
    def method1(self):             #parent
        print("im the father")
        
class son1(father):
    def method2(self):           #child1
        print("im the son1")
        
class son2(father):
    def method3(self):           #child2
        
        print("im the son2")
    
obj1=son1()          #create objects for the child1 and 2
obj2=son2()
obj1.method2()      # accessing methods
obj2.method3()

    