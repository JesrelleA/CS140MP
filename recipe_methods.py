class Recipe:
    #Constructor creates a list
    def __init__(self):
        self.queue = list()

    #Adding elements to queue
    def add_step(self, step, time):
        step_node = []
        step_node.append(step)
        step_node.append(time)
        #Checking to avoid duplicate entry (not mandatory)
        
        self.queue.append(step_node)
        return True


    #Removing the last element from the queue
    def complete_step(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return ("Queue Empty!")

    #Getting the size of the queue
    def count_steps(self):
        return len(self.queue)

    #printing the elements of the queue
    def print_recipe(self):
        return self.queue

    def get_next_step(self):
        return self.queue[0]


    def __del__(self):
        return True
        print ("deleted")

    def __repr__(self):
        return str(self.queue)

class Recipe_lineup:
    def __init__(self):
            self.queue = []

    def add_recipe(self, data):
        #Checking to avoid duplicate entry (not mandatory)
        if data not in self.queue:
            self.queue.append(data)
            return True
        return False

    def print_recipe_list(self):
        return self

    def get_next_step(self):
        return self.queue[0].get_next_step()

    def __repr__(self):
        return str(self.queue)
"""


q_0 = Recipe()
q_1 = Recipe()

p_0 = Recipe_lineup()

print("enqueue 3 to q_0: ", q_0.add_step("cook", 5) ) #prints False, bec duplicate
print("enqueue 5 to q_0: ", q_0.add_step("stew", 5) ) #prints True
print("enqueue 7 to q_0: ", q_0.add_step("cook", 7), "\n\n") #prints True

print("enqueue 1 to q_1: ", q_1.add_step("cook", 1) ) #prints False, bec duplicate
print("enqueue 2 to q_1: ", q_1.add_step("cook", 2) ) #prints True
print("enqueue 4 to q_1: ", q_1.add_step("cook", 4), "\n\n") #prints True

print("enqueue 4 to p_0: ", p_0.add_recipe(q_0), "\n\n") #prints True
print("enqueue 4 to p_0: ", p_0.add_recipe(q_1), "\n\n") #prints True


print(str(p_0.print_recipe_list()))
#print("enqueue 5: ", p_1.str(add_recipe(q_0) ) ) 

#print(q_1.print_recipe_list())
"""
