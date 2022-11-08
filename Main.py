class Student:
    def __init__(self, name, last, ID, next=None):
        self.name = name
        self.last = last
        self.ID = ID
        self.next = next
#---------------------------------------------
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, name, last, ID):
        newStudent = Student(name, last, ID)
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
            if Student == current.name:
                return True
            else:
                return False
            current = current.next
            
    def getListNum(self):
        num = 0
        current = self.head
        while current:
            num+=1
            current = current.next
        print("there are", num, "objects in the linked list")
            
            
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
                
            
    #def List
#-----------------------------------------------
StudentLine = LinkedList()
StudentLine.insert("Lily", "lasname", 456987)
StudentLine.insert("Kevin", "Salasar", 123987)
StudentLine.insert("Sebastian", "Hernandez", 987456)
StudentLine.insert("Brandon", "Sandoval", 321890)
StudentLine.insert("Eli", "Earlix", 654789)
StudentLine.insert("Kyle", "Kubaska", 796805)


StudentLine.PrintList()
StudentLine.getListNum()
print(StudentLine.TakeNumber())
