class student:
    def __init__(self , name , roll_no ,  grade):
        self.name = name
        self.roll_no = roll_no
        self.grade = grade

    def __repr__(self):
        return f"Student(name={self.name}, roll_no = {self.roll_no} , grade is {self.grade})"
    

s = student("yushi" , "0346" , "A")
print(s)


# -----------Using DAtaclass

from dataclasses import dataclass

@dataclass

class stu:
    name:str
    rollno:int
    grade:str

s2 = stu("Ayushsingh" , 15 , "A")
print(s2)