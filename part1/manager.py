from person import Person
class Manager(Person):
    def giveRaise(self,percent,bonus=0.1):
        self.pay*=(1.0+percent+bonus)
        Person.giveRaise(self,percent+bonus)
    def __init__(self,name,age,pay):
        Person.__init__(self,name,age,pay,'11111')

if __name__=='__main__':
    tom=Manager(name='Tom Doe',age=50,pay=50000)
    print(tom)
#    print(tom.laseName())
#   tom.giveRaise(0.20)
#    print(tom.pay)