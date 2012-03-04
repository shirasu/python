class BinaryTree(object):

	class Node(object):
		def __init__(self,data=0):
			self.__data = None
			self.__left = None
			self.__right = None
			
		def setData(self,data):
			self.__data = data
		
		def getData(self):
			return self.__data
			
	def __init__(self):
		self.__rootNode = BinaryTree.Node()
		
	def setData( self, data ):
		nodeBuff = self.__root
		if nodeBuff.__data==None:
			nodeBuff.__data = data
			return 0
		else:
			while nodeBuff != None:
				if nodeBuff.__data == data:
					return -1
				elif nodeBuff.__data > data:
					nodeBuff = nodeBugg.__left
				else:
					nodeBuff = nodeBugg.__right
		
			
							
			
if __name__ == "__main__":

	tree = BinaryTree()	