class Student:
    def __init__(self, name, ID, next=None):
        self.name = name
        self.ID = ID
        self.next = next
#---------------------------------------------
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, name, ID):
        newStudent = Student(name, ID)
        if self.head:
            current = self.head        
            while current.next:
                current = current.next
            current.next = newStudent
        else:
            self.head = newStudent
    
    def PrintList(self):
        current = self.head
        while current:
            print("student name:", current.name, ", ID:", current.ID)
            current = current.next
            
    def TakeNumber(self):
        print("enter student name: ")
        Student = input()
        num = 0
        current = self.head
        while current:
            if Student == current.name:
                return True
            else:
                num += 1
                current = current.next
            
#-----------------------------------------------
StudentLine = LinkedList()
StudentLine.insert("Lily", 456987)
StudentLine.insert("Kevin", 123987)
StudentLine.insert("Sebastian", 4)
StudentLine.insert("Brandon", 456987)
StudentLine.insert("Eli", 123987)
StudentLine.insert("Jacob", 4)

StudentLine.PrintList()
print(StudentLine.TakeNumber())
