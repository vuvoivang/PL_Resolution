import helpers
import copy


def readFileInput(indexFile):
    iFile = open("./Input/input" + str(indexFile) + ".txt", "r")

    # is empty file
    firstLine = iFile.readline()
    if(firstLine == ""):
        return [], []

    alpha = helpers.convertClauseToLiteralArr(firstLine, "OR")

    amount = int(iFile.readline())

    # is amount < 0
    if(amount < 0):
        return [], []

    KB = []
    for i in range(1, amount + 1):
        clause = helpers.convertClauseToLiteralArr(iFile.readline(), "OR")
        KB.append(clause)
    iFile.close()
    return KB, alpha


def PL_Resolve(Ci, Cj):
    cloneCi = copy.deepcopy(Ci)
    cloneCj = copy.deepcopy(Cj)
    isResolve = False
    for x in cloneCi:
        if(-x in cloneCj):
            isResolve = True
            cloneCi.remove(x)
            cloneCj.remove(-x)
            break

    if(isResolve):
        cloneCi.extend(cloneCj)
        return sorted(set(cloneCi), key=helpers.keyAbs)

    else:
        return "nothing"


def PL_Resolution(KB, alpha):

    clauses = copy.deepcopy(KB)
    for literal in alpha:
        # because it's negative of number (the way we store it), append negative of each literal in form array
        clauses.append([-literal])

    # consists of KB and negative alpha
    originalClauses = copy.deepcopy(clauses)
    newClauses = []
    # Start loop
    while True:
        new = []
        for Ci in clauses:
            for Cj in clauses:
                if(Ci == Cj):
                    continue
                resolvents = PL_Resolve(Ci, Cj)
                if(resolvents != "nothing"   # is resolved and drived into 1 clause
                   # is True Clause
                   and not helpers.isTrue(resolvents)
                   # is not exist in this loop
                   and not helpers.isExist(resolvents, new)
                   # is not exist in original KB and negative alpha
                   and not helpers.isExist(resolvents, originalClauses)
                   # is not exist in many loops before
                   and not helpers.isExistIn2DList(resolvents, newClauses)):
                    new.append(resolvents)

        # first, add new even if it's empty or contains [] to show the result
        newClauses.append(new)
        # then check
        if([] in new):
            return True, newClauses
        if(len(new) == 0):
            return False, newClauses
        clauses.extend(new)


def writeOutputFile(indexFile, newClauses, isEntailed):
    oFile = open("./Output/output" + str(indexFile) + ".txt", "w")
    for new in newClauses:
        oFile.write(str(len(new)) + "\n")
        for clause in new:
            if(clause == []):
                oFile.write("{}" + "\n")
                # still show all generated clause in the last loop => don't break
            else:
                cloneClause = [helpers.convertNumberToLiteral(
                    literal) for literal in clause]
                oFile.write(" OR ".join(cloneClause) + "\n")

    if(isEntailed):
        oFile.write("YES")

    else:
        oFile.write("NO")

    oFile.close()


def result(isEntailed):
    if(isEntailed):
        return "entail"
    else:
        return "not entail"


def resolveAnInputFile(indexFile):
    KB, alpha = readFileInput(indexFile)
    if(len(KB) == 0 or len(alpha) == 0):
        return
    isEntailed, newClauses = PL_Resolution(KB, alpha)
    writeOutputFile(indexFile, newClauses, isEntailed)
    print("Resolving file input" + str(indexFile) +
          ".txt. The result is: " + result(isEntailed))


def main():

    numInputFile = helpers.countTxtFileInput("./Input/")
    initialIndexFile = 1  # initial value
    for indexFile in range(initialIndexFile, numInputFile+1):
        resolveAnInputFile(indexFile)


# run main
main()
