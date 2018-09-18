class Step:
    def __init__(self, step, time):
        self.step = step
        self.time = time

    def __repr__(self):         # same as 'whats_da_step'
        return(str(self.step))

    def do_step(self):          # time_step_decrement
        self.time = self.time - 1

    def get_time(self):
        return int(self.time)

class Recipe:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.recipe = [] # is a list of Steps (data struct)

    def __repr__(self):
        return str(self.name)

    def get_step(self):
        return self.recipe[0]

    def add_step(self, step, time):
        s = Step(step, time)
        self.recipe.append(s)

    def do_step(self):
        if self.recipe[0].time > 0:
            self.recipe[0].do_step()
        else:
            self.recipe.pop(0)


filename = "tasklist.txt"
file = open(filename, "r")

tasks_count = {}
tasks       = {}
tasks_list = [] # list of objects Recipe

# gets list of all dishes to be processed
for line in file:
    task_i       = line.split()[0]
    task_sched_i = int(line.split()[1])

    if task_i not in tasks_count:    # for 1st encounter with task
        tasks_count.update({task_i : 1})
        tasks.update({ task_sched_i : str(task_i+"1")})
        
        task = Recipe(str(task_i+"1"), task_sched_i)
        print("made task", task_i, "with time", task_sched_i)
        tasks_list.append(task)
    else:                            # for all subsequent encounters
        tasks_count.update({task_i : tasks_count[task_i]+1})
        task_v = task_i + str(tasks_count[task_i])
        tasks.update({ task_sched_i : task_v})
        
        task = Recipe(task_v, task_sched_i)
        print("made task", task_v, "with sched", task_sched_i)
        tasks_list.append(task)
        
# tasks is now a list of class Recipe with their time
del(tasks_count)

# print(tasks)
headers = ["Time", "Cook", "Ready", "Assistants", "Remarks"]
clock = 1;

# formats header
html = "<html><table border=\"1\">"     
for state in headers:
    html += "<td>{}</td>".format(state)
html += "</tr>"

default = "none"
done_i = None
done_all = False;

head      = 0
step_index      = 0
step_time_index = 1


cooking_str    = ""
ready_str      = ""
assistants_str = "" #background tasks

cooking    = []
ready      = []
assistants = []

# while not done: 

time = 0
arrived_dish = []
cook = [] 
ready = []
assistants = []

arrived = False
cooked_done = False
cook_empty = False
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



while clock < 50:
# will fix condition
# atm stops when the last task arrives
# should stop when last task finishes
    remarks_str    = ""
    recipe = []
     # needs to be cleared every clock; but needs to be accessed beyond fetching function
    """
    # chceks arrival times of tasks and fetches recipe
    if not cooking_str == "":
        remarks = "something is already_str cooking_str so we " + recipe.get_next_step()[0]
        #recipe.get_next_step()[1] = recipe.get_next_step()[1] - 1
"""
    if clock in tasks: 

        remarks = tasks[clock] + " arrives"

        SMTH = tasks_list[0] # gets head of tasklist
        
        task_filename = ''.join(i for i in tasks[clock] if not i.isdigit()) + ".txt" # gets file
        task_file = open(task_filename, "r")   
        

        line_num = 0
        for line in task_file:
            # print("current recipe is", tasks_list[0])
            step       =     line.split()[step_index]      # gets step at a time
            step_time  = int(line.split()[step_time_index]) # gets duration of step
            tasks_list[0].add_step(step, step_time) # adds new Step object to recipe
            
            #step_node = [step, step_time]
            #recipe.append(step_node)

            line_num += 1

        # print(tasks_list[0], "is first step of recipe and has time", tasks_list[0].get_time())

        print("tasks list is", tasks_list)
        
        if recipe: # recipe is not empty
            if cooking_str == "":
                cooking_str =  '{}({}={})'.format(tasks[clock], recipe[0][0], recipe[0][1])
                recipe[0][1] = recipe[0][1] - 1
                #cooking_str = ' '.join(map(str, recipe))
            elif not cooking_str == "":
                ready_str =  '{}({}={})'.format(tasks[clock], recipe[0][0], recipe[0][1])
                #recipe.get_next_step()[1] = recipe.get_next_step()[1] - 1
                remarks += " something is already_str cooking_str" #atm it relaces what was already_str cooking_str
            else:
                ready_str = cooking_str =  '{}({}={})'.format(tasks[clock], recipe[0][0], recipe[0][1])

        if cooking_str:
            cooking_str =  '{}({}={})'.format(tasks[clock], recipe[0][0], recipe[0][1])
            recipe[0][1] = recipe[0][1] - 1



    # ends fetching of next recipe


    for state in headers:
        if state == "Time":
            html += "<td>{}</td>".format( str(clock) )
            clock += 1
        elif state == "Cook":       html += "<td>{}</td>".format( cooking_str )
        elif state == "Ready":      html += "<td>{}</td>".format( ready_str )
        elif state == "Assistants": html += "<td>{}</td>".format( assistants_str )
        elif state == "Remarks":    html += "<td>{}</td>".format( remarks_str )
        else:                       html += "<td>{}</td>".format( default )
        #"<td>{}</td>".format('<br>'.join("laman"))
    html += "</tr>"

    if clock == 16: # this is just for tentative debugging
        done = True

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
}
</style>
"""

html += style

output = open("output.html", "w+")
output.write(html)
output.close()