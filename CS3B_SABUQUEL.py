import random	#import the module to pick a random number

#Value for userGuess and computerGuess
userGuess = 0
computerGuess = 0

def guesses():	#Function to get guesses
    global userGuess	#Access global variable userGuess
    userGuess = input("There are 10 Students, how many do you guess passed? ")   #Get the user's guess
    global computerGuess	#Access global variable computerGuess
    computerGuess = random.randint(1, 10)	#Variable computerGuess will pick a random number between 1 to 10
    print(f"Your Guess is {userGuess}")	#print the user's Guess
    print(f"The Computer Guess is {computerGuess}")	#print the computer's Guess
    continueProgram = input("Continue the evaluation? (Yes/YES) ")	#Ask if the user wants to continue, and the only choice is yes

guesses()

# Student List
studentList = {
	"studentOne" : {
    "studentName": "Ricardo P",	#1
    "studentGrade": 85,
    "classSubject": "DSA"
    }, 
    "studentTwo": {
    "studentName": "Anagracia A",  #2
    "studentGrade": 82,
    "classSubject": "DSA"
    }, 
    "studentThree": {
    "studentName": "Anastacia D",  #3
    "studentGrade": 75,
    "classSubject": "DSA"
    }, 
    "studentFour": {
    "studentName": "Gregorio D",  #4
    "studentGrade": 74,
    "classSubject": "DSA"
    }, 
    "studentFive" : {
    "studentName": "Alegro",  #5
    "studentGrade": 95,
    "classSubject": "DSA"
    }, 
    "studentSix" :  {
    "studentName": "Maria Juana",  #6
    "studentGrade": 90,
    "classSubject": "DSA"
    }, 
    "studentSeven" : {
    "studentName": "Shantal T",   #7
    "studentGrade": 83,
    "classSubject": "OS"
    }, 
    "studentEight" :{
    "studentName": "Mariano J",   #8
    "studentGrade": 91,
    "classSubject": "OS"
    }, 
    "studentNine" : {
    "studentName": "Josefa G",   #9
    "studentGrade": 73,
    "classSubject": "OS"
    }, 
    "studentTen" : {
    "studentName": "Eliseo S",   #10
    "studentGrade": 75,
    "classSubject": "OS"
    }
}

sizeClass = len(studentList)	#Count the number of students
passStudents = []	#List to store passed students
failedStudents = []	#List to store failed students
pStudentCounter = 0	#Passed student counter
fStudentCounter = 0	#Passed student counter

def counterPass():	#Counter for passed students
    global pStudentCounter	#Access global variable pStudentCounter
    pStudentCounter += 1	#Add 1 to pStudentCounter

def counterFail():	#Counter for failed students
    global fStudentCounter	#Access global variable fStudentCounter
    fStudentCounter += 1	#Add 1 to fStudentCounter
    
def testGrade(name, grade, subject):	#Function to check if student passed or failed
    if grade >= 75:	#If grade is 75 or higher, add to the passStudents list
        passStudents.append([name, grade, subject])
        counterPass()
    else:	#Else, Add to the failedStudents list
        failedStudents.append([name, grade, subject])
        counterFail()

def guessedNear():	#Function to compare the guesses
    global userGuess, computerGuess, pStudentCounter	#Access global variables
    nearUGuess = abs(pStudentCounter - int(userGuess))	#Subtract the pStudentCounter with the converted datatype of userGuess
    nearCGuess = abs(pStudentCounter - computerGuess)	#Subtract the pStudentCounter with the converted datatype of userGuess

    if nearUGuess < nearCGuess:	#If the user guessed closer
        print("")
        print("User Guess is nearer!", ({nearUGuess}))
    elif nearUGuess == nearCGuess:	#If both have the same guess
        print("")
        print("User and Computer Guesses are the same")
    else:	#If computer guessed closer
        print("")
        print("Computer Guess is nearer", ({nearCGuess}))

def printList():	#Function to display pass and fail lists
    print("")
    print("----------- List of Students who has a Passing Mark --------------------")
    print(passStudents)	#Print the list of passStudent
    print(f"Total no. of Passed Students: {pStudentCounter}")	#Print the total no. of passed students
    print("")
    print("------------ List of Students who has a Faily Mark ---------------------")
    print(failedStudents)	#print the list of failedStudent
    print(f"Total no. of Failed Students: {fStudentCounter}")	#Print the total no. of failed students

print(f"The following are the List of Students.\nTotal of {sizeClass}")	#Print the total number of students
print("----------------------------------------------------")

for x, obj in studentList.items():	#Loop to extract the items content
    print(f"{obj.get('studentName')} is enrolled in {obj.get('classSubject')}")	#Print student info
for x, obj in studentList.items():
    testGrade(obj.get("studentName"), obj.get("studentGrade"), obj.get("classSubject"))	#Check student grades
    
printList()	#call the printList()
guessedNear()	 #call the guessedNear()