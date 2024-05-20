from datetime import datetime

def generateRegisterNumberOfStudent(id_student):
    date = datetime.now()
    first3Numbers = str(date.year)[2:] + '1'
    numbersOfZeros = 7 - len(first3Numbers)
    registerNumber = first3Numbers + str(id_student).zfill(numbersOfZeros)
    
    return registerNumber
    
    
    
    