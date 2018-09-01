filename = "tasklist.txt"
file = open(filename, "r")

recipe       = {}
recipe_count = {}

for line in file:
    task_i       = line.split()[0]
    task_sched_i = int(line.split()[1])

    if task_i not in recipe_count:	# for 1st encounter with task
        recipe_count.update({task_i : 1})
        recipe.update({ task_sched_i : str(task_i+"1")})
    else:							# for all subsequent encounters
        recipe_count.update({task_i : recipe_count[task_i]+1})
        task_v = task_i + str(recipe_count[task_i])
        recipe.update({ task_sched_i : task_v})

print("count was:", recipe_count)
print("task list is", recipe)
    #print(recipe_count)
    
    # print(recipe, time)
    #print(line)
task = {"adob", "sinigang", "tapsilog"} 

#html = """<html><table border="1">
#<tr><th>Time</th><th>Cook</th><th>Ready</th><th>Assistants</th></tr>"""


headers = ["Time", "Cook", "Ready", "Assistants", "Remarks"]
clock = 0;

html = "<html><table border=\"1\">"     # formats header
for state in headers:
    html += "<td>{}</td>".format(state)
html += "</tr>"

for luto in task:
    #html += "<tr><td>{}</td>".format(task)
    for state in headers:
        if state == "Time":
            html += "<td>"+str(clock)+"</td>"
            clock+=1
        else:
            html += "<td>{}</td>".format(state)

        #"<td>{}</td>".format('<br>'.join("laman"))

    html += "</tr>"

html += "</table></html>"

f = open("output.html", "w+")
f.write(html)
f.close()