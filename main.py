class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail.value = new_node.value
        self.tail = new_node
        self.tail.value = None

    def appendToStart(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def showAll(self):
        node = self.head.next
        while node.next is not None:
            print(node.value, end=' ')
            node = node.next
        print()


def getNum(list):
    k = 0
    cur = list.head.next
    num = 0
    while cur != list.tail:
        num += cur.value * 10 ** k
        k += 1
        cur = cur.next
    return num


def sumOfLinkedLists(l1, l2):
    num1 = getNum(l1)
    num2 = getNum(l2)
    print(num1, num2)
    sumNum = num1 + num2
    print(sumNum)
    resList = LinkedList()
    while sumNum != 0:
        resList.append(sumNum % 10)
        sumNum //= 10
    resList.showAll()


def getNodeValue(curNode, l):
    return curNode.value if curNode is not l.tail else 0


def sumOfLinkedListsInMind(l1, l2):
    curOne = l1.head.next
    curTwo = l2.head.next
    resList = LinkedList()
    inMind = 0
    while not (curOne is l1.tail and curTwo is l2.tail):
        if curOne is not l1.tail:
            num1 = curOne.value
            curOne = curOne.next
        else:
            num1 = 0

        if curTwo is not l2.tail:
            num2 = curTwo.value
            curTwo = curTwo.next
        else:
            num2 = 0

        resList.append((num1 + num2 + inMind) % 10)
        inMind = (num1 + num2) // 10

    resList.showAll()


linkedListOne = LinkedList()
linkedListTwo = LinkedList()

linkedListOne.append(2)
linkedListOne.append(4)
linkedListOne.append(7)
linkedListOne.append(1)
linkedListOne.showAll()

linkedListTwo.append(9)
linkedListTwo.append(4)
linkedListTwo.append(5)
linkedListTwo.showAll()
#
# sumOfLinkedLists(linkedListOne, linkedListTwo)
sumOfLinkedListsInMind(linkedListOne, linkedListTwo)
