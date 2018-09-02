class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self, data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(len(self.queue), data)
          return True
      return False

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop(0)
      return ("Queue Empty!")

  #Getting the size of the queue
  def get_size(self):
      return len(self.queue)

  #printing the elements of the queue
  def print_queue(self):
      return self.queue

  def get_head(self):
      return self.queue[0]

q_0 = Queue()
q_1 = Queue()

print("enqueue 5: ", q_0.enqueue(5)) #prints True
print("enqueue 6: ", q_0.enqueue(6)) #prints True
print("enqueue 9 : ", q_0.enqueue(9)) #prints True
print("enqueue a queue: "q_1.enqueue(q_0));

"""
print("enqueue 5: ", q_0.enqueue(5)) #prints False, bec duplicate
print("enqueue 3: ", q_0.enqueue(3), "\n\n") #prints True

print("size of queue is", q_0.get_size(), "\n\n")     #prints 4
print("dequeue: ",q_0.dequeue())  #prints 5

print("head now is: ", q_0.get_head()) #prints True
print("dequeue: ", q_0.dequeue())  #prints 6

print("head now is: ", q_0.get_head()) #prints True
print("dequeue: ", q_0.dequeue())  #prints 9

print("head now is: ", q_0.get_head()) #prints True
print("dequeue: ", q_0.dequeue())  #prints 3
print("size of queue is", q_0.get_size())     #prints 0
print("dequeue: ", q_0.dequeue())  #prints Queue Empty!
"""