studentMarks = {
        "A":80, "B":85, "C":60, "D":99, "E":60, "F":61, "G":62, "H":63
        }

def getStudentMark(studentName):
    if(studentName in studentMarks):
        return studentMarks[studentName]
    else:
        return "Invalid search"

studentName = input("Enter student name to get mark : ")
mark = getStudentMark(studentName)
print(f"{studentName}'s mark : {mark}")

