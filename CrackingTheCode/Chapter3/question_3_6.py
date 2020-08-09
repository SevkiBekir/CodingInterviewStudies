from Utils.LinkedList import LinkedList
from Utils.Queue import Queue
import enum

class AnimalType(enum.Enum):
    Cat = 1
    Dog = 2

class AnimalNode:
    def __init__(self, name,date):
        self.name = name
        self.date = date

    def print(self):
        print("Printing AnimalNode")
        print(self.name)
        print(self.date)
        print("-----------")

class AnimalShelter:
    def __init__(self):
        self.dogList = LinkedList()
        self.catList = LinkedList()
        self.date = 0

    def enqueue(self,animalName,animalType):
        self.date += 1
        if animalType == AnimalType.Cat:
            node = AnimalNode(animalName,self.date)
            self.catList.insertTail(node)
        elif animalType == AnimalType.Dog:
            node = AnimalNode(animalName, self.date)
            self.dogList.insertTail(node)
        else:
            self.date -= 1

    def findOldestAnimal(self, linkedList):
        oldestAnimalNode = linkedList.head
        date = oldestAnimalNode.data.date
        traverseNode = linkedList.head
        while traverseNode.next is not None:
            if date > traverseNode.next.data.date:
                oldestAnimalNode = traverseNode.next

            traverseNode = traverseNode.next

        return oldestAnimalNode


    def dequeuDog(self):
        if self.dogList.isEmpty():
            print("Error: the list empty")
            return
        else:
            oldestNode = self.findOldestAnimal(self.dogList)
            self.dogList.removeNode(oldestNode.data)
            return oldestNode

    def dequeuCat(self):
        if self.catList.isEmpty():
            print("Error: the list empty")
            return
        else:
            oldestNode = self.findOldestAnimal(self.catList)
            self.catList.removeNode(oldestNode.data)
            return oldestNode

    def dequeueAny(self):
        oldestCatNode = None
        oldestDogNode = None

        if self.catList.isEmpty():
            print("Warning: cat the list empty")
        else:
            oldestCatNode = self.findOldestAnimal(self.catList)

        if self.dogList.isEmpty():
            print("Warning: dog list empty")
        else:
            oldestDogNode = self.findOldestAnimal(self.dogList)


        if oldestDogNode.data.date > oldestCatNode.data.date:
            self.catList.removeNode(oldestCatNode.data)
            return oldestCatNode
        else:
            self.dogList.removeNode(oldestDogNode.data)
            return oldestDogNode



    def printAll(self):
        print("Printing Dog")
        self.dogList.printList()


        print("Printing Cat")
        self.catList.printList()



if __name__ == '__main__':
    a = AnimalShelter()
    a.enqueue("ali",AnimalType.Dog)
    a.enqueue("veli",AnimalType.Dog)
    a.printAll()
    animal = a.dequeuDog()
    animal.data.print()

    a.enqueue("puppy",AnimalType.Cat)
    a.enqueue("kiraz",AnimalType.Cat)
    a.printAll()

    animal = a.dequeueAny()
    animal.data.print()

    a.enqueue("deli",AnimalType.Dog)
    a.printAll()

    animal = a.dequeueAny()
    animal.data.print()