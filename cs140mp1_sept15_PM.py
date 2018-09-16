#nakaformat to class na yung mga inputs pero di pa nahahandle yung pagsame yung name
#working na yung pagpasok on time nung dish
#nakakapagcook na pero yung sa first dish palang... huhu ayaw magpop pag cook == 0. Idk why medj sabaw na huhu


class Step:
    def __init__(self, step, time):
        self.step = step
        self.time = time

    def __repr__(self):
        return(str(self.step))

    def time_step_decrement(self):
        self.time = self.time - 1

    def whats_da_step(self): #returns the step
        return self.step

class Recipe:
    def __init__(self, name, time, priority, recipe):
        self.name = name
        self.time = time
        self.priority = priority
        self.recipe = []

    def __repr__(self):
        return(str(self.name))

    def add_step(self, name, time):
        k = Step()
        k.step = name
        k.time = time
        self.recipe.append(k)

    def do_step(self):
        if self.recipe[0].time > 0:
            self.recipe[0].time_step_decrement()
        else:
            self.recipe.pop(0)

    def dis_step_na(self): #returns the current (yung head/first sa recipe) of the dish
        return self.recipe[0].whats_da_step()

    def time_left_for_step(self):
        return self.recipe[0].time

dishlist = []

f = open("Tasklist.txt", "r") #open file
with open('Tasklist.txt') as f:
    c = [word for line in f for word in line.split()]
f.close()


p = 1
i = 0

for i in range(len(c)):
    if i % 2 == 0:
        meal = Recipe()
        meal.name = c[i]
    elif i % 2 != 0:
        meal.time = int(c[i])
        meal.priority = p
        meal.recipe = []
        p = p + 1
        dishlist.append(meal)

for i in range(len(dishlist)):
    a = dishlist[i].name + ".txt"
    f = open(a, "r")
    with open(a) as f:
        b = [word for line in f for word in line.split()]
    for j in range(len(b)):
        if j % 2 == 0:
            task = b[j]
        elif j % 2 != 0:
            duration = int(b[j])
            dishlist[i].add_step(task, duration)
    f.close()

time = 0
arrived_dish = []
cook = [] 
ready = []
assistants = []

arrived = False
cooked_done = False
cook_empty = False
win = True
remarks_dish_arrived = ""
done_cooking = ""

for l in range(0, 30):
    time = time + 1

    if(len(dishlist)!=0):
        if dishlist[0].time == time: 
            arrived = True
            remarks_dish_arrived = dishlist[0]    #temp holder of the dish that arrived and also for printing purposes
            arrived_dish.append(dishlist[0])
            task = remarks_dish_arrived.dis_step_na()
            dishlist.pop(0) 
            print(task)
    if (len(dishlist)!=0) and (task == "cook"):
            if len(cook) == 0 and len(ready) == 0:  #as in walang dish na cino-cook and nagwaiwait para macook hehe so enter na agad sa 'Cook' column
                cook.append(remarks_dish_arrived)
            else: 
                ready.append(remarks_dish_arrived) #will enter the ready queue since there might still be a dish in the 'cook'
    else:
            assistants.append(remarks_dish_arrived)  #not 'cook' yung step so will enter the assistants

    #UPDATE/CHECK WHAT IS HAPPENING IN COOK COLUMN
    if len(cook) != 0: #may dish sa loob ni cook
        if cook[0].time_left_for_step != 0:
            remaining_time = cook[0].time_left_for_step() 
            print(remaining_time)
            if remaining_time == 0:
                print("DONE COOKING")
                cooked_done = True
                done_cooking = cook[0]
                
                cook[0].recipe.pop(0) #delete 'cook' in the recipe of the dish
                if len(cook[0].recipe) != 0: #may next step yung dish
                    print("DONE COOKING 2")
                    if cook[0].recipe[0] == "cook":
                        #print in Cook: {cook[0].name}(cook={cook[0].time_left_for_step})
                        cook[0].do_step()
                    else:
                        assistants.append(cook[0])
                        print("APPENDED SOMETHING TO COOKING") # ri added
                        print("the thing appended was ", cook[0].recipe[0])
                        done_cooking = cook[0]
                    cook[0].recipe.pop(0) #delete the dish in 'cook' since its cooked hehe
                cook.pop(0)

            else:
                cooked_done = False
        
    if len(cook) == 0 and len(ready) == 0: # wala ng icoo-cook
        cook_empty = True

    if len(cook) == 0 and len(ready) != 0:
        # INSERT ALGO THAT GETS THE DISH WITH THE HIGHEST PRIORITY
        print("Cook column is empty but \nthere's dish waiting in the ready column!")
        var = 100
        h = 0
        for d in range(len(ready)):
            compare = ready[d].priority
            if (compare < var):
                var = compare
                winner = ready[d]
                h = d
            #winner = #gets the dish with the highest priority to be cooked
            #delete the dish winner in the ready queue
            
            #print in Remarks: {winner.name}[chosen]
        ready.pop(h)
        cook.append(winner)
        #ready.pop(h)

    #REMARKS PRINTING
    print("time = ", time)

    print("\n\nCOOK COLUMN")
    if (cook_empty == True):
        cook_empty = False
    else:
        print(cook[0].name, "(cook=", cook[0].recipe[0].time, ")")
        cook[0].do_step()

    print("\n\nREADY COLUMN")
    for m in range(len(ready)):
        print(ready[m].name, "(",ready[m].dis_step_na(),"=",ready[m].time_left_for_step(),")")
        
    
    print("\n\nASSISTANTS COLUMN")
    for m in range(len(assistants)):
        print(assistants[m].name, "(",assistants[m].dis_step_na(),"=",assistants[m].time_left_for_step(),")")
        # assistants[0].do_step()
        """
        print(assistants[m].name, "(",assistants[m].dis_step_na(),"=",assistants[m].time_left_for_step(),")")
        """
    

    """
    for m in range(len(ready)):
        ready[m].do_step()
        print("did step\n")
        print(ready[m].name, "(",ready[m].dis_step_na(),"=",ready[m].time_left_for_step(),")")
    """

    print("\n\nREMARKS COLUMN")
    if (arrived == True):
        arrived = False
        print(remarks_dish_arrived.name, "arrives")
   
    if cooked_done == True:
        cooked_done = False
        print(done_cooking.name,"[cook done]")

    print("-----------------")

    #break


print("YAAAAAAAAY")