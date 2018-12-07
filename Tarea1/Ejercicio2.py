class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

 	def getElemento(self):
   		return self.data

class Queue:
	def __init__(self):
		self.length = 0
		self.head = None
       		self.last = None
    
	def is_empty(self):
		return self.length == 0
    
	def enqueue(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
		else:
			self.last.next = node
		self.last=node
		self.length += 1

	def dequeue(self):
		if self.head is not None:
			aux = self.head
			self.head = self.head.next
			return aux

class Stack:
	def __init__(self):
        	self.head = None
        	self.count = 0
    
	def push(self, value):
        	new_node = Node(value)
        	self.count += 1
        	if self.head is not None:
           		new_node.next = self.head
        	self.head = new_node
    
	def is_empty(self):
        	if self.head is None:
        		return True
        	else:
        		return False
	def pop(self):
		if self.head is not None:
			aux = self.head
			self.head = self.head.next
			return aux

def NotacionPolaca(string):
	length = len(string)
	operators = Stack()
	numbers = Queue()
	for i in range(length):
		if string [i] == + or string [i] == * or string [i] == -:
			operators.push(string [i])

		elif (string [i] is not None):
			numbers.push(string [i])
	
	print (operators.pop() " ")
	while numbers.is_empty() == false:
		if numbers.head == (:
			print( operators.pop() " ")
		elif numbers.head.next =! (:
			print( operators.pop() " ")
		else:
			print( numbers.dequeue() " ")
	print( "Es igual a: " int(string))

def NotacionPolacaInversa(string):
	length = len(string)
	operators = Queue()
	numbers = Queue()
	for i in range(length):
		if string [i] == + or string [i] == * or string [i] == -:
			operators.push(string [i])

		elif (string [i] is not None):
			numbers.push(string [i])
	
	while numbers.is_empty() == false:
		if numbers.head == (:
			numbers.dequeue()
		elif numbers.head.next =! ):
			print( numbers.dequeue() " ")
		elif numbers.head == (:
			print( operators.dequeue() " ")
	print( "Es igual a: " int(string))
	