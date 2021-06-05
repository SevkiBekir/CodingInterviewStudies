stackSizeInArray = 3

def createStacksInArray(size):
    if size < 0:
        print("Error!")
        return

    stackSizeInArray = globals().get("stackSizeInArray")

    stackSize = int(size / stackSizeInArray)
    array = [None] * (stackSize * stackSizeInArray)
    return array

def getInitialIndex(stackNo, inArray):
    stackSizeInArray = globals().get("stackSizeInArray")
    arraySize = len(inArray)
    initialIndex = int((stackNo - 1) * (arraySize / stackSizeInArray))
    return initialIndex

def getFinalIndex(stackNo, inArray):
    stackSizeInArray = globals().get("stackSizeInArray")
    arraySize = len(inArray)
    initialIndex = int(stackNo * (arraySize/stackSizeInArray))
    return initialIndex

def getStackFor(stackNo,inArray):

    if stackNo < 1:
        print("Error!")
        return

    initialIndex = getInitialIndex(stackNo,inArray)
    finalIndex = getFinalIndex(stackNo, inArray)

    return inArray[initialIndex:finalIndex]

def findEmptyIndexFor(stack):

    for i in range(len(stack)):
        if stack[i] is None:
            return i

    return None

def moveStackToArray(stack, stackNo, inArray):
    initialIndex = getInitialIndex(stackNo,inArray)
    finalIndex = getFinalIndex(stackNo, inArray)

    stackIndex = 0
    for i in range(initialIndex,finalIndex):
        if stack[stackIndex] is not inArray[i]:
            inArray[i] = stack[stackIndex]

        stackIndex += 1

def isEmptySpaceIn(stack):
    return None in stack

def extendAllStacks(inArray):
    arraySize = len(inArray)
    newArray = createStacksInArray(arraySize * 2)

    stackSizeInArray = globals().get("stackSizeInArray")

    for stackNo in range(stackSizeInArray):

        initialIndexForNewArray = getInitialIndex(stackNo+1, newArray)

        stack = getStackFor(stackNo+1,inArray)


        for i in range(len(stack)):
            newArray[initialIndexForNewArray+i] = stack[i]

    return newArray



def pushItemOn(data,stackNo, inArray):
    stack = getStackFor(stackNo,inArray)
    # check emptySpace
    if not isEmptySpaceIn(stack):
        inArray = extendAllStacks(inArray)
        stack = getStackFor(stackNo, inArray)

    # push item on related stack
    stack.insert(0,data)

    moveStackToArray(stack,stackNo,inArray)
    print("Item pushed on stack #" + str(stackNo))

def popItemOn(stackNo, inArray):
    stack = getStackFor(stackNo,inArray)

    data = stack.pop(0)
    stack.append(None)
    moveStackToArray(stack,stackNo,inArray)


    return data

def printStackFor(stackNo,inArray):
    stack = getStackFor(stackNo,inArray)
    print("Printing Stack #" + str(stackNo))
    print(stack)

def printAllStacks(inArray):
    for stackNo in range(stackSizeInArray):
        printStackFor(stackNo + 1,inArray)

if __name__ == '__main__':
    print("Question 3.1")

    # array = createThreeStackInArray(100)
    # stack = getStackFor(1,array)
    # print(stack)
    # stack[0] = 10
    # print(array)
    # print(stack)
    #
    #
    #
    # coefficent = 0
    #
    # for i in range(33):
    #     array[coefficent*33 + i] = coefficent*33 + 1
    #
    # coefficent = 1
    #
    # for i in range(33):
    #     array[coefficent*33 + i] = coefficent*33 + 1
    #
    # print(getStackFor(1,array))
    # stack = getStackFor(1,array)
    # stack[5] = 5
    # moveStackToArray(stack,1,array)
    # print(array)
    # print(len(array))
    #
    # array = extendAllStacks(array)
    # print(array)
    # print(len(array))


    #
    # coefficent = 1
    #
    # array[coefficent * 33 + 0] = coefficent * 33 + 1
    # array[coefficent * 33 + 1] = coefficent * 33 + 2
    # array[coefficent * 33 + 2] = coefficent * 33 + 3
    # array[coefficent * 33 + 32] = coefficent * 33 + 33
    # print(getStackFor(2, array))
    #
    # coefficent = 2
    #
    # array[coefficent*33 + 0] = coefficent*33 + 1
    # array[coefficent*33 + 1] = coefficent*33 + 2
    # array[coefficent*33 + 2] = coefficent*33 + 3
    # array[coefficent*33 + 32] = coefficent*33 + 33
    # print(getStackFor(3,array))

    array = createStacksInArray(100)
    pushItemOn(4,1,array)
    printAllStacks(array)

    pushItemOn(6,2,array)
    printAllStacks(array)

    pushItemOn(8,3,array)
    pushItemOn(10,3,array)
    pushItemOn(81,3,array)
    pushItemOn(82,3,array)
    printAllStacks(array)

    popElement = popItemOn(3,array)
    print(popElement)
    printAllStacks(array)



