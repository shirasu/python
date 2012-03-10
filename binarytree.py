# -*- coding:utf-8 -*-

#ノードクラス
class Node(object):
	def __init__(self,data):
		self.__data = data
		self.__left = None
		self.__right = None
	
	def setData(self,data):
		self.__data = data
	
	def getData(self):
		return self.__data
		
	def getLeft(self):
		return self.__left
		
	def setLeft(self,node):
		self.__left = node
		
	def getRight(self):
		return self.__right
		
	def setRight(self,node):
		self.__right = node

#データ挿入
def add( node, data ):
	if node is None:
		return Node(data)
	elif data == node.getData():
		return node
	elif data < node.getData():
		node.setLeft( add( node.getLeft(), data ) )
	else:
		node.setRight( add( node.getRight(), data ) )
	return node

#探索
def search( node, data ):
	while node:
		if node.getData() == data:
			return True
		if data < node.getData():
			node = node.getLeft()
		else:
			node = node.getRight()
	
	return False

#データ巡回
def traverse_h( node ):
	if node:
		traverse_h(node.getLeft())
		print node.getData()
		traverse_h(node.getRight())

# ジェネレータバージョン
def traverse(node):
	if node:
		for x in traverse(node.getLeft()):
			yield x
		yield node.getData()
		for x in traverse(node.getRight()):
			yield x

#最小値探索
def search_min(node):
	if node.getLeft() is None:
		return node.getData()
	return search_min(node.getLeft())

#最小値削除
def delete_min(node):
	if node.getLeft() is None:
		return node.getRight()
	node.setLeft( delete_min(node.getLeft()) )
	return node

#削除
def delete(node, data):
	if node:
		if data == node.getData():
			if node.getLeft() is None:
				return node.getRight()
			elif node.getRight() is None:
				return node.getLeft()
			else:
				node.setData( search_min(node.getRight() ) )
				node.setRight( delete_min(node.getRight() ) )
		elif data < node.getData():
			node.setLeft( delete(node.getLeft(), data ) )
		else:
			node.setRight( delete( node.getRight(), data ) )
	return node
		
#二分木クラス
class BinaryTree(object):

	def __init__(self):
		self.__rootNode =None

	#探索
	def search( self, data ):
		return search(self.__rootNode, data )
	
	#挿入
	def add( self, data ):
		self.__rootNode = add(self.__rootNode, data )
	
	#巡回
	def traverse(self):
		for x in node.traverse(self.root):
			yield x

	#表示
	def __str__(self):
		if self.__rootNode is None: return 'BinaryTree()'
		buff = 'BinaryTree('
		for x in traverse(self.__rootNode):
			buff += '%s, ' % x
		buff = buff.rstrip(',  ')
		buff += ')'
		return buff

	#削除
	def delete( self, data ):
		self.__rootNode ==delete( self.__rootNode, data )

if __name__ == "__main__":
	import random
	#テスト
	tree = BinaryTree()	
	data = [random.randint(0,100) for x in range(10)]
	print data
	for x in data:
		tree.add(x)
	print tree
	
	for x in data:
		print 'search', x, tree.search(x)
		print 'delete', x
		tree.delete(x)
		print 'search', x, tree.search(x)
		print tree