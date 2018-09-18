

class Step:
    def __init__(self, step, time):
        self.step = step
        self.time = time

    def time_step_decrement(self):
        self.time = self.time - 1

    def whats_da_step(self): #returns the step
        return self.step

    def whats_da_time(self):
    	return self.time

class Recipe:
    def __init__(self, name, time, priority, recipe):
        self.name = name
        self.time = time
        self.priority = priority
        self.recipe = []

    def add_step(self, name, time):
        k = Step("","")
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
    	#return self.recipe[0].whats_da_time()
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
        meal = Recipe("",0,0,[])
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

print(dishlist)
#input()

time = 0
stop = 0
arrived_dish = []
cook = [] 
ready = []
assistants = []

arrived = False
cooked_done = False
cook_empty = False
ready_empty = False
win = False
done_assistants = False

assistants_empty = False
remarks_dish_arrived = ""
done_cooking = ""
done_cooking1 = ""
assistants_done = []
done_assistants = []
donetasks_assistants = []
index = []
remarks_checker = []


f3 = open("output_REFER.html", "w")
f3.write("<html>")
f3.write("<head>")
f3.write("<style>")
f3.write("table, th, td {")
f3.write("  border: 1px solid black;")
f3.write("}")
f3.write("</style>")
f3.write("</head>")
f3.write("<body>")
f3.write("<table border=1>")
f3.write("<tr>")
f3.write("  <th>Time</th>")
f3.write("  <th>Cook</th>")
f3.write("  <th>Ready</th>")
f3.write("  <th>Assistant</th>")
f3.write("  <th>Remarks</th>")
f3.write("</tr>")

print(len(remarks_checker))
#print(len(cook) != 0) and (len(ready) != 0) and (len(assistants) != 0) and (len(remarks_checker) != 0)
for i in range(0,140):#while (True):  #for l in range(0, 30):
    time = time + 1

    if(len(dishlist)!=0):
    	if dishlist[0].time == time: 
            arrived = True
            remarks_checker.append(1)
            remarks_dish_arrived = dishlist[0]    #temp holder of the dish that arrived and also for printing purposes
            arrived_dish.append(dishlist[0])
            task = remarks_dish_arrived.dis_step_na()
            dishlist.pop(0) 
            #print(task)
    if (arrived == True) and (task == "cook"): #if (len(dishlist)!=0) and (task == "cook"):
	        if len(cook) == 0 and len(ready) == 0:  #as in walang dish na cino-cook and nagwaiwait para macook hehe so enter na agad sa 'Cook' column
	            cook.append(remarks_dish_arrived)
	        else: 
	            ready.append(remarks_dish_arrived) #will enter the ready queue since there might still be a dish in the 'cook'
    elif (arrived == True) and (task != "cook"): #elif (len(dishlist)!=0) and (task != "cook"):
	        assistants.append(remarks_dish_arrived)  #not 'cook' yung step so will enter the assistants

    #UPDATE/CHECK WHAT IS HAPPENING IN COOK COLUMN
    if len(cook) != 0: #may dish sa loob ni cook

        if cook[0].time_left_for_step() != 0:
            remaining_time = cook[0].time #cook[0].time_left_for_step() 
            print(remaining_time)
            if remaining_time == 0:
                #print("DONE COOKING")
                cooked_done = True
                remarks_checker.append(2)
                done_cooking = cook[0]
                cook[0].recipe.pop(0) #delete 'cook' in the recipe of the dish
                if len(cook[0].recipe) != 0: #may next step yung dish
                    #print("DONE COOKING 2")
                    #print("this task na = ", cook[0].dis_step_na())
                    if cook[0].dis_step_na() == "cook":
                        #print in Cook: {cook[0].name}(cook={cook[0].time_left_for_step})
                        cook[0].do_step()
                    elif cook[0].dis_step_na() != "cook":
                        #print("something task")
                        assistants.append(cook[0])
                        done_cooking = cook[0]
                    #cook[0].recipe.pop(0) #delete the dish in 'cook' since its cooked hehe
                cook.pop(0)

            else:
                cooked_done = False
        if cook[0].time_left_for_step() == 0:
            #print("Done Cooking!!!")
            cooked_done = True
            done_cooking = cook[0]
            cook[0].recipe.pop(0)
            if len(cook[0].recipe) != 0:
                #print("May step pa sa recipe!")
                #print("this task na = ", cook[0].dis_step_na())
                if cook[0].dis_step_na() == "cook":
                    cook[0].do_step()
                elif cook[0].dis_step_na() != "cook":
                    #print("something task")
                    #print(cook[0].dis_step_na())
                    assistants.append(cook[0])
                    done_cooking = cook[0]
            cook.pop(0)
        
    if len(cook) == 0 and len(ready) == 0: #wala ng icoo-cook
        cook_empty = True  #still part of the algo that checks what should be cooked next   

    if len(cook) == 0 and len(ready) != 0:
        #INSERT ALGO THAT GETS THE DISH WITH THE HIGHEST PRIORITY
        if len(ready) != 0:
            #print("Cook column is empty but there's dish waiting in the ready column!")
            win = True
            cook.append(ready[0])
            winner = ready[0]
            ready.pop(0)
            done_cooking1 = winner
            #print(done_cooking1.name, "[chosen]")
        elif len(ready) == 0:
            ready_empty = True
            #print("00000")
        

    #UPDATE/CHECK WHAT IS HAPPENING IN THE ASSISSTANT COLUMN
    if len(assistants) == 0:
	    assistants_empty = True

    for i in range(len(assistants)):
        #print("len of assistants =", len(assistants))
        if assistants[i].time_left_for_step() != 0:
            assistants_empty = False
        elif assistants[i].time_left_for_step() == 0:
            #print("Done na yung sa assistant")
            donetasks_assistants.append(assistants[i].dis_step_na())
            assistants[i].recipe.pop(0)
            #print("next task is", assistants[i].dis_step_na())
            done_assistants = True
            remarks_checker.append(3)
            assistants_done.append(assistants[i])
            if len(assistants[i].recipe) == 0:
                index.append(i) #assistants.pop(i)
            if len(assistants[i].recipe) != 0:
                if assistants[i].dis_step_na() == "cook":
                    if len(ready) == 0 and len(cook) == 0:
                        cook[0] = assistants[i]
                    elif len(cook) == 0 and len(ready) != 0: #is this condition possible???
                        ready.append(assistants[i])
                    elif len(cook) != 0:
                        ready.append(assistants[i])
                    index.append(i) #index = i #assistants.pop(i)
                else:
                    temp = assistants[i]
                    assistants.pop(i)
                    assistants.append(temp)
        if (len(assistants) == 0):
            break
	






    #REMARKS PRINTING
    f3.write("<tr>")
    output = " <td> bgcolor=\"gray\">" + str(time) + "</td>" #" <th>" + str(time) + "</th>"
    f3.write(output)
    #f3.write("  <th>")
    print("time = ", time)
    print()

    print("COOK COLUMN")
    if (cook_empty == True):
        cook_empty = False
        print("none")
        stop = stop + 1
        f3.write("  <th>none</th>")
    else:
        print(cook[0].name, "(cook=", cook[0].time_left_for_step(), ")") #print(cook[0].name, "(cook=", cook[0].recipe[0].time, ")")
        printthis = "   <th>" + cook[0].name + "(cook=" + str(cook[0].time_left_for_step()) + ")</th>" #####HEEEEEERE
        cook[0].do_step()
        f3.write(printthis)

    print()
    print("READY COLUMN")
    if len(ready) == 0:
        print("none")
        f3.write("  <th>none</th>")
        stop = stop + 1
    else:
        printthis = "   <th>"
        for m in range(len(ready)):
            print(ready[m].name, "(",ready[m].dis_step_na(),"=",ready[m].time_left_for_step(),")")
            printthis = printthis + ready[m].name + "(" + ready[m].dis_step_na() + "=" + str(ready[m].time_left_for_step()) + ") "
        printthis = printthis + "</th>"
        f3.write(printthis)

    print()
    print("ASSISSTANT COLUMN")
    #print("IIIIIN HEEEERE")
    if assistants_empty == True:
        print("none")
        f3.write("  <th>none</th>")
        stop = stop + 1 #assistants_empty, stop = False, stop + 1
    if done_assistants ==  True:
        for w in range(len(index)):
            #print(assistants)
            #print(index[w])
            #input()
            assistants[index[w]] = []
        assistants = [assistant for assistant in assistants if assistant != []]
        index = []

    printthis = "   <th>"
    for m in range(len(assistants)):
        print(assistants[m].name, "(", assistants[m].dis_step_na(), "=", assistants[m].time_left_for_step(), ")")
        printthis = printthis + assistants[m].name + "(" + assistants[m].dis_step_na() + "=" + str(assistants[m].time_left_for_step()) + ") "
        #print("doing the step")
        assistants[m].do_step()
        #print("NAGDECREMENT NA")
    printthis = printthis # + "</th>"
    if (len(assistants) == 0) and (assistants_empty == True): #assistants_empty == True:
        assistants_empty = False
        print("none")
        #h = input()
        printthis = "<th>none</th>"
        f3.write(printthis)
        #f3.write()
    elif assistants_empty == False:
        printthis = printthis + "</th>"
        f3.write(printthis)

    assistants_empty = False
    	

    print()
    print("REMARKS COLUMN")
    printthis = "   <th>"
    if(len(remarks_checker) == 0):
        print("none")
        printthis = printthis + "none"
        #3.write("  <th>none")
        stop = stop + 1

    if (arrived == True):
        arrived = False
        print(remarks_dish_arrived.name, "arrives")
        printthis = printthis + remarks_dish_arrived.name + "[arrives]. "
        #f3.write(printthis)
   
    if cooked_done == True:
        cooked_done = False
        print(done_cooking.name,"[cook done]")
        printthis = printthis + done_cooking.name + "[cook done]. "
        if win == True:
            win = False
            print(done_cooking1.name, "[chosen]")
            printthis = printthis + done_cooking1.name + "[chosen]. "
            #f3.write(printthis)

    if done_assistants == True:
    	done_assistants = False
    	for m in range(len(assistants_done)):
            print(assistants_done[m].name, "[", donetasks_assistants[m], "done ]")
            printthis = printthis + assistants_done[m].name + "[" + donetasks_assistants[m] + " done]. "
    	assistants_done, donetasks_assistants = [], []

    remarks_checker = []
    printthis = printthis + "</th>"
    f3.write(printthis)


    if stop == 4:
        f3.write("</tr>")
        break
    stop = 0
    f3.write("</tr>")



    print("------------------------------------------------------------------------------------------")

    #input()
    #break

f3.write("</table>")
f3.write("")
f3.write("</body>")
f3.write("</html>")
f3.close()
print("YAAAAAAAAY")