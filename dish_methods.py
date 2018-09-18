class Step: # individual tasks for a dish
    def __init__(self, step, time):
        self.step = step # eg. cook
        self.time = time # eg 1, 2

     #def is_done():


class Recipe: 
    def __init__(self, name, time, priority):
        self.name     = name
        self.time     = time
        self.priority = priority
        self.recipe   = [Step(0, 0)]

    def add_step(step):
        self.recipe.append(step)

    def do_step():
        if self.recipe[0].time > 0:
            self.recipe[0].time = self.recipe[0].time - 1
        else:
        	self.recipe.pop(0)

    def print_step(self):
    	print(self.recipe)

x = Recipe("adobo", 1, 1)

print(x.name)
print(x.time)
x.print_step()

