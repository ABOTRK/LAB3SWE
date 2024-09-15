def readStudents(stdList):
    
    for student in stdList:
        print(student + "  ")


def createGroup(stdList, sizeOfGroups = 2):
    
    numberOfGroups = round((len(stdList) / sizeOfGroups))

    for k in range(numberOfGroups):

        print(f"Group ({k + 1}): ")

        for i in range(1,3):
            if(len(stdList) > 0):
                print(f"{i}. {stdList.pop()}") 

def studentCheck(stdLIst,studentName):
    for st in stdLIst:
        if(st == studentName) :
            return True
        else:
            return False


listTem = ["A", "B", "C", "D"]

createGroup(listTem)