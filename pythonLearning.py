import random
import sys
import select
import tty
import termios


DECENDING = 0
ASCENDING = 1

def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
old_settings = termios.tcgetattr(sys.stdin)

print(int(str("000")))
exit()

def swap(x,y):
    # return y,x
    '''
       This is a test description
    '''
    x,y = y,x
    return x,y

print(swap(8,9))

def printList(a):
    for i,val in enumerate(a):
        print(str(i) + " " + str(val))
    print(dict.fromkeys(a))
    print(dict(enumerate(a)))

printList(["a", "b", "hello",123])
exit()

def reverseString(x):
    # return x[-1:-(len(x)+1):-1]
    return x[::-1]

def matrixMultiplication():
    print("This is matrixMultiplication ")

def binarySearchTree():
    print("This is Binary Search Tree")

def primeGenerator():
    print("This is primeGenerator ")
    print ("using list comprehension generate prime upto 100, using user input and output")

def bubbleSort(unsortedList,order):
    # order = 0 indicates assending, order = 1 indicates descending
    arraySize = len(unsortedList)
    print("arraySize " + str(arraySize) + "Unsorted List" + str(unsortedList))
    for i in range(0,arraySize-1):
        for j in range(0, arraySize-1):
            if (order == DECENDING):
                if (unsortedList[j] > unsortedList [j+1]):
                    temp = unsortedList [j+1]
                    unsortedList [j+1] = unsortedList[j]
                    unsortedList[j] = temp
            else:
                if (order == ASCENDING):
                    if (unsortedList[j] < unsortedList [j+1]):
                        temp = unsortedList [j+1]
                        unsortedList [j+1] = unsortedList[j]
                        unsortedList[j] = temp
    print("Sorted List" + str(unsortedList))

def bubbleSortAutoTest():
    print("This is bubble sort")
    unsortedList = []
    for i in range(100):
        unsortedList.append(random.randint(0,999))
    # order = DECENDING
    order = ASCENDING
    bubbleSort(unsortedList,order)

def binarySearch(sortedList, startIndex, endIndex, searchValue):
    print("Function Binary Search")
    printNotFound = "SerachValue {} not found"
    printFound = "SerachValue {} not found"
    printFound = "Found SearchValue {} at index {}"
    printStartEnd = "Start {} end {}"
    start = startIndex
    end = endIndex
    searchIndex = -1
    for i in range(start, end, 1):
        if start > end:
            # print("SerachValue " + str(searchValue) + "not found")
            print(printNotFound.format(searchValue))
            print(printStartEnd.format(start, end))
            # print("Start " + str(start) + "end" + str(end))
            exit()
        mid = (start + end)/2
        mid = int(mid)
        # print("Start " + str(start) + " end " + str(end) + "mid " + str(mid))
        if sortedList[mid] == searchValue:
            searchIndex = mid
            break
        elif sortedList[mid] < searchValue:
            start = mid + 1
        else:
            end = mid - 1
        print(printStartEnd.format(start, end))
        # print("Start " + str(start) + " end " + str(end))
    if searchIndex > -1:
        print(printStartEnd.format(start, end))
        # print("Start " + str(start) + "end" + str(end))
        print(printFound.format(searchValue,searchIndex))
        # print("Found SearchValue" + str(searchValue) + "at index" + str(searchIndex))
    else:
        # print("Start " + str(start) + "end" + str(end))
        print(printNotFound.format(searchValue))
        # print("SearchValue " + str(searchValue) + "not found")

def binarySearchAutoTest():
    print("BinarySearchProgramTest started")
    startVal = 1
    endVal = 100000
    sortedList = [1 * x for x in range (startVal,endVal+1)]
    startIndex = 0
    endIndex = endVal-1
    try:
        tty.setcbreak(sys.stdin.fileno())

        for x in range(startVal, endVal):
            # serachValue = 200
            # binarySearch(sortedList, startIndex, endIndex, serachValue)
            binarySearch(sortedList, startIndex, endIndex, x)

            if isData():
                c = sys.stdin.read(1)
                if c == '\x1b':         # x1b is ESC
                    break
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class llist:
    def __init__(self):
        self.next = None
    
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.next
        self.next = newNode

    def printList(self):
        tempNode = self.next
        while (tempNode):
            print(tempNode.data)
            tempNode = tempNode.next
        print("Print over")

    def reverseList(self):
        Prev = None
        Curr = self.next
        while (Curr):
            Next = Curr.next
            Curr.next = Prev
            Prev = Curr
            Curr = Next
        self.next = Prev
            
print("Python Learning Started")

mylist = llist()
mylist.push(10)
mylist.push(20)
mylist.push(30)
mylist.push(40)
mylist.printList()
mylist.reverseList()
mylist.printList()

print("Python Learning Started")
# binarySearchAutoTest()
# bubbleSortAutoTest()
print(reverseString("eraH eraH amaR amaR amaR eraH amaR eraH \n eraH eraH anhsirK anhsirK anhsirK eraH anhsirK eraH"))
exit()



