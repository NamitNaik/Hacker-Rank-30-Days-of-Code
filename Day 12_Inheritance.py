class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
    def calculate(self):
        n = len(self.scores)
        s = 0
        for i in self.scores:
            s = s + int(i)
        avg = int(s/n)  
        
        if avg>=90:
            return('O')
        elif avg>=80:
            return('E')
        elif avg>=70:
            return('A')
        elif avg>=55:
            return('P')
        elif avg>=40:
            return('D')
        else:
            return('T')                    

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())