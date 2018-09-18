def format_cell(string):
    return "<td>{}</td>".format(string)

class Step:
    def __init__(self, step, time):
        self.step = step
        self.time = time

    def __repr__(self):
        return self.step

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

    def __repr__(self):
        return self.name

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

cooking_str    = ""
ready_str      = ""
assistants_str = ""
remarks_str = ""

headers = ["Time", "Cook", "Ready", "Assistants", "Remarks"]
clock = 1;

# formats header
html = "<html><table border=\"1\">"     
for state in headers:
    html += "<td>{}</td>".format(state)
html += "</tr>"



# html += str(len(remarks_checker))
# html += str(len(cook) != 0) and (len(ready) != 0) and (len(assistants) != 0) and (len(remarks_checker) != 0)
for i in range(0,140):#while (True):  #for l in range(0, 30):
    time = time + 1

    if(len(dishlist)!=0):
    	if dishlist[0].time == time: 
            arrived = True
            remarks_checker.append(1)
            remarks_dish_arrived = dishlist[0]    #temp holder of the dish that arrived and also for html += string purposes
            arrived_dish.append(dishlist[0])
            task = remarks_dish_arrived.dis_step_na()
            dishlist.pop(0) 
            # html += str(task)
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
            html += format_cell(str(remaining_time))
            if remaining_time == 0:
                #html += str("DONE COOKING")
                cooked_done = True
                remarks_checker.append(2)
                done_cooking = cook[0]
                cook[0].recipe.pop(0) #delete 'cook' in the recipe of the dish
                if len(cook[0].recipe) != 0: #may next step yung dish
                    #html += str("DONE COOKING 2")
                    #html += str("this task na = ", cook[0].dis_step_na())
                    if cook[0].dis_step_na() == "cook":
                        #html += str in Cook: {cook[0].name}(cook={cook[0].time_left_for_step})
                        cook[0].do_step()
                    elif cook[0].dis_step_na() != "cook":
                        #html += str("something task")
                        assistants.append(cook[0])
                        done_cooking = cook[0]
                    #cook[0].recipe.pop(0) #delete the dish in 'cook' since its cooked hehe
                cook.pop(0)

            else:
                cooked_done = False
        if cook[0].time_left_for_step() == 0:
            #html += str("Done Cooking!!!")
            cooked_done = True
            done_cooking = cook[0]
            cook[0].recipe.pop(0)
            if len(cook[0].recipe) != 0:
                #html += str("May step pa sa recipe!")
                #html += str("this task na = ", cook[0].dis_step_na())
                if cook[0].dis_step_na() == "cook":
                    cook[0].do_step()
                elif cook[0].dis_step_na() != "cook":
                    #html += str("something task")
                    #html += str(cook[0].dis_step_na())
                    assistants.append(cook[0])
                    done_cooking = cook[0]
            cook.pop(0)
        
    if len(cook) == 0 and len(ready) == 0: #wala ng icoo-cook
        cook_empty = True  #still part of the algo that checks what should be cooked next   

    if len(cook) == 0 and len(ready) != 0:
        #INSERT ALGO THAT GETS THE DISH WITH THE HIGHEST PRIORITY
        if len(ready) != 0:
            #html += str("Cook column is empty but there's dish waiting in the ready column!")
            cook.append(ready[0])
            winner = ready[0]
            ready.pop(0)
            done_cooking1 = winner
            #html += str(done_cooking1.name, "[chosen]")
        elif len(ready) == 0:
            ready_empty = True
            #html += str("00000")
        

    #UPDATE/CHECK WHAT IS HAPPENING IN THE ASSISSTANT COLUMN
    if len(assistants) == 0:
	    assistants_empty = True

    for i in range(len(assistants)):
        #html += str("len of assistants =", len(assistants))
        if assistants[i].time_left_for_step() != 0:
            assistants_empty = False
        elif assistants[i].time_left_for_step() == 0:
            #html += str("Done na yung sa assistant")
            donetasks_assistants.append(assistants[i].dis_step_na())
            assistants[i].recipe.pop(0)
            #html += str("next task is", assistants[i].dis_step_na())
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
    # html += str("COOK COLUMN")
    if (cook_empty == True):
        cook_empty = False
        cooking_str += str("none")
        stop = stop + 1
    else:
        html += str(cook[0].name) + "(cook=" + str(cook[0].time_left_for_step())+ ")" #html += str(cook[0].name, "(cook=", cook[0].recipe[0].time, ")")
        cook[0].do_step()

    # html += str("READY COLUMN")
    if len(ready) == 0:
        ready_str += str("none")
        stop = stop + 1
    else:
        for m in range(len(ready)):
            assistants_str += str(ready[m].name)+"("+str(ready[m].dis_step_na())+"="+str(ready[m].time_left_for_step())+")"
    # html += str("ASSISSTANT COLUMN")
    #html += str("IIIIIN HEEEERE")
    if assistants_empty == True:
        html += "none"
        assistants_empty, stop = False, stop + 1
    if done_assistants ==  True:
        for w in range(len(index)):
            html += str(assistants)
            html += str(index[w])
            #input()
            assistants[index[w]] = []
        assistants = [assistant for assistant in assistants if assistant != []]
        index = []

    for m in range(len(assistants)):
        html += str(assistants[m].name)+"("+str(assistants[m].dis_step_na())+"="+str(assistants[m].time_left_for_step())+")"
        #html += str("doing the step")
        assistants[m].do_step()
        #html += str("NAGDECREMENT NA")
    	
    # html += str("REMARKS COLUMN")
    if(len(remarks_checker) == 0):
        html += str("none")
        stop = stop + 1

    if (arrived == True):
    	arrived = False
    	html += str(remarks_dish_arrived.name)+ "arrives"
   
    if cooked_done == True:
    	cooked_done = False
    	html += str(done_cooking.name)+"[cook done]"
    	if win == True:
    		win = False
    		html += str(done_cooking1.name)+"[chosen]"

    if done_assistants == True:
    	done_assistants = False
    	for m in range(len(assistants_done)):
    		html += str(assistants_done[m].name)+"["+str(donetasks_assistants[m])+"done ]"
    	assistants_done, donetasks_assistants = [], []

    remarks_checker = []

    for state in headers:
        if state == "Time":
            html += "<td>{}</td>".format( str(time) )
            #time += 1
        elif state == "Cook":       html += "<td>{}</td>".format( cooking_str )
        elif state == "Ready":      html += "<td>{}</td>".format( ready_str )
        elif state == "Assistants": html += "<td>{}</td>".format( assistants_str )
        elif state == "Remarks":    html += "<td>{}</td>".format( remarks_str )


    if stop == 4:
        html += "</tr>"
        break

    stop = 0
    html += "</tr>"



    # html += str("------------------------------------------------------------------------------------------")

    #input()
    #break


html += "</table></html>"

style = """<style>
th {
    font-weight: bold;
    text-align: -internal-center;
}
user agent stylesheet
td, th {
    display: table-cell;
    vertical-align: inherit;
}
user agent stylesheet
table {
    white-space: normal;
    line-height: normal;
    font-weight: normal;
    font-size: medium;
    font-style: normal;
    color: -internal-quirk-inherit;
    text-align: start;
    font-variant: normal;
}
user agent stylesheet
table {
    display: table;
    border-collapse: separate;
    border-spacing: 2px;
    border-color: grey;
}


table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    table-layout:fixed;
    width: 100%;
}

td {

    /* css-3 */
    white-space: -o-pre-wrap; 
    word-wrap: break-word;
    white-space: pre-wrap; 
    white-space: -moz-pre-wrap; 
    white-space: -pre-wrap; 

}
</style>
"""

html += style


output = open("output.html", "w+")
output.write(html)
output.close()
html += str("YAAAAAAAAY")