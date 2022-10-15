class student:

    def setDetails(self, name, age):
        self.name =name
        self.age=age

        # print("my name is "+ name1)
    def getdetails(self):
        return {self.name,self.age}



student1 = student()
student2 = student()
student1.setDetails("Jay", 18)
student2.setDetails("Aditya", 21)
print("First ", student1.getdetails(), " and second value ", student2.getdetails())

--------------------------------------------------------------------------------------------------------------------------
class collage():
     def __init__(self,branches,student,buses):
         self.branches=['ec',"cs","ft","csit"]
         self.student=2345
         self.buses=45

     def getvalue(self):
        return self.branches,self.student,self.buses

a=collage()



