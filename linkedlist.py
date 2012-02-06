class LinkedList(object):
	class Node(object):
		def __init__(self,data=0):
			self.__data = data
			self.__next = None
			
		def setData(self,data):
			self.__data = data
		
		def getData(self):
			return self.__data
		
		def getNext(self):
			return self.__next
	
	def __init__(self):
		self.__headNode = LinkedList.Node(-1)
		self.__headNode.__next=None

		
	def getSize(self):
		n = 0
		node = self.__headNode
		while True:
			if node.__next == None:
				break
			else:
				node = node.__next
				n = n + 1
		
		return n

	def addIndexNode( self,nIndex,addNode ):
		node = self.__headNode
		n = 0
		while n < nIndex:
			n += 1
			node = node.__next
		
		node2 = node.__next
		node.__next = addNode
		addNode.__next = node2
		return 0

	def addNode(self,addNode):
		n = self.getSize()
		self.addIndexNode(n,addNode)

	def viewData(self):
		print "View Data"
		node = self.__headNode
		while True:
			if node == None:
				break
			else:
				print node.getData()
				node = node.__next
		print "end!"

if __name__ == "__main__":
	listA = LinkedList()
	nodeA = LinkedList.Node(1)
	print "nodeA=", nodeA.getData()
	listA.addIndexNode(0,nodeA)
	print listA.getSize()
	nodeB = LinkedList.Node(2)
	print "nodeB=", nodeB.getData()
	listA.addIndexNode(1,nodeB)
	print listA.getSize()
	listA.viewData()