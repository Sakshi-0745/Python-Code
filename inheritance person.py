class person(object):
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number
    def display(self):
        print(f"my name is{self.name},and my idnumber is {self.id_number}")
class employee(person):
    def __init__(self,id_number,name,salary,post):
        self.id_number=id_number
        self.name=name
        self.salary=salary
        self.post=post
        person.__init__(self,name,id_number)
    def display(self):
        print(f"my name is {self.name}")
        print(f"My id_number is {self.id_number},and my salary is {self.salary}")
        print(f"my post is {self.post}")
# class post(person):
#     def __init__(self,post):
#         self.post = post
#     def display(self):
#         print(f"My post is {self.post}") 
p1 = employee("mike",25412,8710235,"PR manager")
p1.display()

# print(p1.display)
# print(p2.display)
# print(p3.display)
