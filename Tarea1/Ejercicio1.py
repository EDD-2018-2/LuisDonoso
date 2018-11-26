class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None
		self.value = 0

 	def getElemento(self):
   		return self.data

class CircularLinkedList:
	
	def __init__(self):
		self.head = None
		self.counter = 0
	
	def push(self, data):
		ptr1 = Node(data)
		temp = self.head
		ptr1.next = self.head
		if self.head is not None:
			while(temp.next != self.head):
				temp = temp.next
			temp.next = ptr1
			self.counter += 1
		else:
			ptr1.next = ptr1 
			self.head = ptr1 
			self.counter += 1
	
	def sortedInsert(self, new_node):
		
		current = self.head
		if current is None:
			new_node.next = new_node 
			self.head = new_node
			self.counter += 1
		elif (current.value >= new_node.value):
			while current.next != self.head :
				current = current.next
			current.next = new_node
			new_node.next = self.head
			self.head = new_node
			self.counter += 1		 
		else:
			while (current.next != self.head and
				current.next.value < new_node.value):
				current = current.next

			new_node.next = current.next
			current.next = new_node
			self.counter += 1

	def deleteNode(self, data):
		aux = self.head 
		if self.head is None or dele is None:
			return
		for i in self: 
			if aux.data == dele:
				prev = aux.prev
				aux = aux.next
				aux.prev = prev
				self.counter -= 1
			else:
				aux = aux.next
	def reOrder(self):
		aux = self.head 
   		for passnum in self.counter:
      			for i in range(passnum):
            			if aux < aux.next:
                			temp = aux
                			aux = aux.next
                			aux.next = temp

				aux = aux.next
		

	def Search(self, data):
		aux = self.head 
		if self.head is None or data is None:
			return
		for i in self.counter: 
			if aux.data == data:
				aux.value +=1
				reOrder(self)
				return aux
			else:
				aux = aux.next


