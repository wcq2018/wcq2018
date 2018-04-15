a=1
b=1
c=a+b
d=a-b
def add(x,y):
    #print(x+y)
    return x+y
res=add(2,4)
t=add(res,3)
print(t)

class employee:
    #创建一个类变量
    pay_raist_amount=1.2
    #__是代表私有变量
    __weight=40
    #创建一个构造器
    def __init__(self,frist,last,pay,domain="fanmao.com"):
        self.frist=frist
        self.last=last
        self.pay=pay
        self.email=frist+last+"@"+domain

    #创建一个方法
    def fullname(self):
        return self.frist+self.last
        #return '{}-{}-{}'.format(self.first, self.last, self.pay)
    def new_pay0(self):
        return self.pay * self.pay_raist_amount
    def new_pay1(self):
        return  self.pay * employee.pay_raist_amount
#创建一个类的实例
emp1=employee("sfd","sgs",400)
emp2=employee("sfd","rty",7000,"qq.com")
employee.pay_raist_amount = 1.4
print(emp1.new_pay0())
print(emp1.new_pay1())
print(emp2.new_pay0())
print(emp2.new_pay1())
emp1.pay_raist_amount = 1.5
print("emp1. raise, emp1.newpay0()",emp1.new_pay0())
print(emp1.new_pay1())
print(emp2.new_pay0())
print(emp2.new_pay1())
emp2.pay_raist_amount = 1.6
print(emp1.new_pay0())
print(emp1.new_pay1())
print("emp２. raise, emp1.newpay0()",emp2.new_pay0())
print(emp2.new_pay1())
#调用类的方法
print(emp1.frist,emp1.last,emp1.pay,emp1.email)
print(emp2.frist,emp2.last,emp2.pay,emp2.email)
