filename = "tasklist.txt"
file = open(filename, "r")

tasks          = {}
tasks_count       = {}

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

print(tasks)
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


cooking    = ""
ready      = ""
assistants = "" #background tasks
to_cook    = {}

# while not done: 

recipe_lineup = []


#while clock <= max(tasks, key=int):  

while clock < 50:
# will fix condition
# atm stops when the last task arrives
# should stop when last task finishes
    remarks    = ""
    recipe = []
     # needs to be cleared every clock; but needs to be accessed beyond fetching function
    """
    # chceks arrival times of tasks and fetches recipe
    if not cooking == "":
        remarks = "something is already cooking so we " + recipe.get_next_step()[0]
        #recipe.get_next_step()[1] = recipe.get_next_step()[1] - 1
"""
    if clock in tasks: 
        remarks = tasks[clock] + " arrives"

        task_filename = ''.join(i for i in tasks[clock] if not i.isdigit()) + ".txt"
        task_file = open(task_filename, "r")   

        line_num = 0
        for line in task_file:
            step       =     line.split()[step_index]      # gets step at a time
            step_time  = int(line.split()[step_time_index]) # gets duration of step
            step_node = [step, step_time]
            recipe.append(step_node)

            line_num += 1

        recipe_lineup.append(recipe)
        #print(recipe)
        #print(tasks[clock], recipe_lineup)
        
        if recipe: # recipe is not empty
            if cooking == "":
                cooking =  '{}({}={})'.format(tasks[clock], recipe[0][0], recipe[0][1])
                recipe[0][1] = recipe[0][1] - 1
                #cooking = ' '.join(map(str, recipe))
            elif not cooking == "":
                ready =  '{}({}={})'.format(tasks[clock], recipe[0][0], recipe[0][1])
                #recipe.get_next_step()[1] = recipe.get_next_step()[1] - 1
                remarks += " something is already cooking" #atm it relaces what was already cooking
            else:
                ready = cooking =  '{}({}={})'.format(tasks[clock], recipe[0][0], recipe[0][1])


        if cooking:
            cooking =  '{}({}={})'.format(tasks[clock], recipe[0][0], recipe[0][1])
            recipe[0][1] = recipe[0][1] - 1



    # ends fetching of next recipe


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

    if clock == 16: # this is just for tentative debugging
        done = True

#print(tasks, recipe_lineup)
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