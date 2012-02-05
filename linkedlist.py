class LinkedList(object):
	class Node(object):
		def __init__(self,data):
			self.__data = data
			self.__next = None
			
		def setData(self,data):
			self.__data = data
		
		def getData(self):
			return self.__data
		
		def getNext(self):
			return self.__next
	
	def __init__(self):
		self.__headNode = LinkedList.Node(self)
		self.__headNode.__next=None
		self.__headNode.__data="haed2"
		
		print self.__headNode.__data
		
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
		
	def addNode(self,addNode):
		Node = self.__headNode
		while Node != None:
			Node = Node.__next
			
		Node.__next = addNode
	
	def addIndexNode( self,nIndex,addNode ):
		if nIndex > getSize(self):
			return 1
		Node = self.__headNode
		for n in nIndex:
			 n +=1
			 Node=Node.__next
			 
		Node2 = Node.__next
		Node.__next=addNode
		addNode.__next = Node2
		
		return 0
		
	def viewData(self):
		Node = self.__headNode
		while Node != None:
			print Node.__data
