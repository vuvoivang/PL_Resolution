import os
import fnmatch

numConvert = ord('A') - 1

# count the amount of input file (txt)


def countTxtFileInput(dir):
    return (len(fnmatch.filter(os.listdir(dir), '*.txt')))


def convertLiteralToNumber(literal):
    if(len(literal) == 1):
        return (ord(literal[0]) - numConvert)
    else:
        return -(ord(literal[1]) - numConvert)


def convertNumberToLiteral(num):
    if(num < 0):
        return '-' + chr(-num + numConvert)
    else:
        return chr(num + numConvert)


def keyAbs(a):
    return abs(a)


def convertClauseToLiteralArr(clause, splitBy):
    arr = []
    for c in clause.split(splitBy):
        # convert to number to resolve easily
        # example: A => 1 and -A => -1. Then negative(A) =  -(1) = -1 and A + (-A) = 1 + (-1) =0
        arr.append(convertLiteralToNumber(c.strip()))
    arr.sort(key=keyAbs)
    return arr


def isTrue(clause):
    for x in clause:
        if(-x in clause):
            return True
    return False


def isExist(clause, clauseList):
    if(clause in clauseList):
        return True
    else:
        return False


def isExistIn2DList(clause, arrayNew):
    for new in arrayNew:
        if(isExist(clause, new)):
            return True
    return False
