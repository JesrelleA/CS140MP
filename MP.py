from queue import *

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

"""
print("count was:", tasks_count)
print("task list is", tasks)

"""

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
# while not done: 

cooking    = ""
ready      = ""
assistants = "" #background tasks
to_cook     = {}
queue      = []


while clock <= max(tasks, key=int):
    remarks    = ""
    recipe = [] # needs to be cleared every clock; but needs to be accessed beyond fetching function

    # chceks arrival times of tasks and fetches recipe
    if clock in tasks: 
        remarks = tasks[clock] + " arrives"
        queue.append(tasks[clock])


        task_filename = ''.join(i for i in tasks[clock] if not i.isdigit()) + ".txt"
        task_file = open(task_filename, "r")   

        line_num = 0
        for line in task_file:
            recipe.append([])
            
            step       =     line.split()[step_index]      # gets step at a time
            step_time  = int(line.split()[step_time_index]) # gets duration of step
            recipe[line_num].append(step)
            recipe[line_num].append(step_time)

            line_num += 1
          
        to_cook[tasks[clock]] = recipe
        #print(recipe)
        #print(to_cook)

        # to_cook.update({tasks[clock]: recipe})

        if recipe: # recipe is not empty
            if cooking == "":
                cooking =  '{}({}={})'.format(tasks[clock], recipe[head][step_index], recipe[head][step_time_index])
                recipe[head][step_time_index] = recipe[head][step_time_index] - 1
                #cooking = ' '.join(map(str, recipe))
            elif not cooking == "":
                cooking =  '{}({}={})'.format(tasks[clock], recipe[head][step_index], recipe[head][step_time_index])
                recipe[head][step_time_index] = recipe[head][step_time_index] - 1

               #remarks += " something is already cooking"
            else:
                ready = cooking =  '{}({}={})'.format(tasks[clock], recipe[head][step_index], recipe[head][step_time_index])


                """
                if recipe[head][step_time_index] == 0:
                cooking = ""
                """





    for state in headers:
        if state == "Time":
            html += "<td>{}</td>".format( str(clock) )
            clock += 1
        elif state == "Cook":       html += "<td>{}</td>".format( cooking )
        elif state == "Ready":      html += "<td>{}</td>".format( ready )
        elif state == "Assistants": html += "<td>{}</td>".format( assistants )
        elif state == "Remarks":    html += "<td>{}</td>".format( remarks )
        else:                       html += "<td>{}</td>".format( default )
        #"<td>{}</td>".format('<br>'.join("laman"))
    html += "</tr>"

    if clock == 16:
        done = True

html += "</table></html>"

style = """
<style>
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