#output.html : https://mail-attachment.googleusercontent.com/attachment/u/0/?ui=2&ik=bb97680506&attid=0.2&permmsgid=msg-f:1610556590187403599&th=1659d8af88c8d94f&view=att&disp=inline&realattid=f_jllqu7gs2&saddbat=ANGjdJ8GWd3aDhwv-sXuHjfIL3eX-Qnxj_0peVK0BfKZ5qW_4LH6wv62BxqIRl8Jeu7Q_Dh1O7AoCa2CFY-KkOmicgHLGevHp9MaXIACsuiaRGGVu92CQlrqSM67m1V5xY2hjTbF67f9MplZTXhnlLR4s495eWXxut5btVLZwXHgXUu0XMA5WeRUI6fFbQpaGtfpYEX3sbS50tWT3J3vPIK5hxpKJw3x4E9w42wHuXeuLtSC2Pb_CshR6Crth7W7v2vYEzKwS5dR0J1e2DN7-a66kCZmOLdro8tCKhaxt-pJsEW3xV8uVpaGpdcz1Q9ECTM_PH8R0dOiDE_LCLNGDKgOCy1ysSWeYPFC2vHpj9xKIQHvaceeYu2kKkt29zLohCQ4T8Wjc6ezzgze9Sm7iVqorXHfG6WGiZV-kKH7Ygs885GJH444fWJCGKNERX5dXECzTx_8RknCH6Lj3MmITb6_TMi62yAE20DT62JlY9OZdXfm0HcTtH0iuyEx2EzEZln9GzaJcup9BcdlLBq5t3jCcTrfGSTwyJO0SabuszTf0nOY87nAokqjPIQKxJBt1SPsivqnGCyMWg1je3gx-oWBcGI9O4MpU74cdEcrpUegIJ4Ujm4Xbig5V3RJKKQslqql9IERxO1JIAkQQlxO


class Step:
	def _init_(self, step, time):
		self.step = step
		self.time = time

	def time_step_decrement():
		self.time = self.time - 1

	def whats_da_step(): #returns the step
		return self.step



class Recipe:
	def _init_(self, name, time, priority):
		self.name = name
		self.time = time
		self.priority = priority
		self.recipe = []

	def add_step(name, time):
        self.recipe.append(Step(name, time))

    def do_step():
    	if self.recipe[0].time > 0:
    		self.recipe[0].time_step_decrement()
    	else:
    		self.recipe.pop(0)

    def dis_step_na(): #returns the current (yung head/first sa recipe) of the dish
    	return self.recipe[0].whats_da_step()

   	def time_left_for_step():
   		return self.recipe[0].time


dishlist = []
#INPUT FORMATTING??? Reading input file and creating it to class
while True: #adds recipe to the dishlist
	x = Recipe(name, time, priority) #from Recipe
		while True: #adds the steps to the recipe
			x.add_step(name, time)


#option 1 
time = 1
arrived_dish = [] #contains the dishes inside the scheduler (dishes that already arrived)
cook = [] #or maybe not an array
ready = []
assistants = []

while True: #becomes False if all the tasks are done
	if dishlist[0].time == time: #checks if the dish will enter the scheduler
		current = dishlist[0] 	 #temp holder of the dish that arrived
		arrived_dish.append(dishlist[0])
		dishlist.pop(0) #deletes the dish in the dishlist since it has entered the scheduler
		#print in Remarks: {current.name} arrives
		task = dishlist.dis_step_na() #gets the task

		if task == "cook":
			if len(cook) == 0 && len(ready) == 0:  #as in walang dish na cino-cook and nagwaiwait para macook hehe so enter na agad sa 'Cook' column
				cook[0] = current
			else: #if len(cook) == 0 && len(ready) != 0: 
				ready.append(current) #will enter the ready queue since there might still be a dish in the 'cook'
		else:
			assistants.append(current)  #not 'cook' yung step so will enter the assistants

		#PRINT THE CURRENT TIME IN HTML FORMAT
		time = time - 1

		#UPDATE/CHECK WHAT IS HAPPENING IN COOK COLUMN
		if len(cook) != 0: #may dish sa loob ni cook
			if cook[0].time_left_for_step != 0:
				#print in Cook: {cook[0].name}(cook={cook[0].time_left_for_step})
				cook[0].do_step()
			else:
				#print in Remarks: {cook[0].name}[cook done]
				cook[0].recipe.pop(0) #delete 'cook' in the recipe of the dish
				if len(cook[0].recipe) != 0: #may next step yung dish
					if cook[0].recipe[0] == "cook":
						#print in Cook: {cook[0].name}(cook={cook[0].time_left_for_step})
						cook[0].do_step()
					else:
						ready.append(cook[0])
						cook[0].pop(0) #delete the dish in 'cook' since its cooked hehe
		

		if len(cook) == 0 && len(ready) == 0: #wala ng icoo-cook
			#print in Cook: none

		if len(cook) == 0 && len(ready) != 0:
			#INSERT ALGO THAT GETS THE DISH WITH THE HIGHEST PRIORITY
			winner = #gets the dish with the highest priority to be cooked
			#delete the dish winner in the ready queue
			#print in Remarks: {winner.name}[chosen]
			cook[0] = winner
			#print in Cook: {cook[0].name}(cook={cook[0].time_left_for_step})
			cook[0].do_step()


		#UPDATE/CHECK WHAT IS HAPPENING IN READY COLUMN
		if len(ready) != 0: #may dish sa loob ni ready
			#print lahat ng laman ni ready[]
		else: #walang laman na dish si ready[]
			#print 'none'


		#UPDATE/CHECK WHAT IS HAPPENING IN THE ASSISSTANT COLUMN
		if len(assistants) == 0:
			#print in Assistants: none
		i = 0
		for i in range(len(assistants)):
			if assistants[i].time_left_for_step() != 0:
				#print [assistants[i].name]([assistant[i].dis_step_na()]=assistants[i].time_left_for_step())
				assistants[i].do_step();
			else:
				#print in remarks {assistant[i].name} {assistant[i].whats_da_step()} done'
				assistants[i].recipe.pop(0) #delete the task since its done
				if len(assistants[i].recipe) != 0:
					if assistants[i].recipe.dis_step_na() == "cook":
						if len(ready) == 0 && len(cook) == 0:
							cook[0] = assistants[i]
						else if len(cook) == 0 && len(ready) != 0: #Is this condition possible???
							#append assistants[i] to the ready queue and get the winner and put it to cook
						else if len(cook) != 0:
							ready.append(assistants[i])
					else: 
						#temp = assistants[i]
						#assistants.pop(i)
						#assistants.append(temp)
						#print [assistants[i].name]([assistant[i].dis_step_na()]=assistants[i].time_left_for_step())
						assistants[i].do_step()
				else:
					assistants.pop(i)

				

			















			






		














