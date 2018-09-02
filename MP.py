filename = "tasklist.txt"
file = open(filename, "r")

tasks          = {}
tasks_count       = {}

class Recipe:
    to_do = []
    def __init__(self, recipe_list=None):
        self.to_do = recipe_list

    def add_to_recipe(step, step_time):
        to_do.append(step, step_time)




for line in file:
    task_i       = line.split()[0]
    task_sched_i = int(line.split()[1])

    if task_i not in tasks_count:    # for 1st encounter with task
        tasks_count.update({task_i : 1})
        tasks.update({ task_sched_i : str(task_i+"1")})
    else:                            # for all subsequent encounters
        tasks_count.update({task_i : tasks_count[task_i]+1})
        task_v = task_i + str(tasks_count[task_i])
        tasks.update({ task_sched_i : task_v})


print("count was:", tasks_count)
print("task list is", tasks)

headers = ["Time", "Cook", "Ready", "Assistants", "Remarks"]
clock = 1;

# formats header
html = "<html><table border=\"1\">"     
for state in headers:
    html += "<td>{}</td>".format(state)
html += "</tr>"

prio_queue = "none"

default = "none"
done_i = None
done_all = False;
# while not done: 

while clock <= max(tasks, key=int):
    cooking = ""
    ready = ""
    assistants = "" #background tasks
    remarks = ""

    # chceks arrival times of tasks and fetches recipe
    if clock in tasks: 
        recipe = []
        remarks = tasks[clock] + " arrives"


        task_filename = ''.join(i for i in tasks[clock] if not i.isdigit()) + ".txt"
        task_file = open(task_filename, "r")   

        line_num = 0
        for line in task_file:
            recipe.append([])
            
            step       = line.split()[0]      # gets step at a time
            step_time  = int(line.split()[1]) # gets duration of step
            recipe[line_num].append(step)
            recipe[line_num].append(step_time)

            line_num += 1

        print(recipe)

        if recipe: # recipe is not empty
            if cooking == "":
                
                cooking = str(recipe[0][0]) +"="+ str(recipe[0][1]) 
                recipe[0][1]=recipe[0][1]-1
                #cooking = ' '.join(map(str, recipe))
            else:
                ready = "smth"


    for state in headers:
        if state == "Time":
            html += "<td>{}</td>".format( str(clock) )
            clock += 1
        elif state == "Cook":

#            print(tasks[clock], recipe)

            """
            if ()
            if (prio_queue == "none"):
                cooking = tasks[luto]
                html += "<td>{}</td>".format( cooking )
            """
            html += "<td>{}</td>".format( cooking )
        elif state == "Ready":
            html += "<td>{}</td>".format( ready )
        elif state == "Assistants":
            html += "<td>{}</td>".format( assistants )

        elif state == "Remarks":
            html += "<td>{}</td>".format( remarks )
        else:
            html += "<td>{}</td>".format( default )
        #"<td>{}</td>".format('<br>'.join("laman"))
    html += "</tr>"

    if clock == 16:
        done = True

html += "</table></html>"

output = open("output.html", "w+")
output.write(html)
output.close()