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


print("count was:", tasks_count)
print("task list is", tasks)

headers = ["Time", "Cook", "Ready", "Assistants", "Remarks"]
clock = 1;

html = "<html><table border=\"1\">"     # formats header
for state in headers:
    html += "<td>{}</td>".format(state)
html += "</tr>"
prio_queue = "none"
for luto in tasks:
    #html += "<tr><td>{}</td>".format(task)
    for state in headers:
        if state == "Time":
            html += "<td>{}</td>".format( str(clock) )
            clock+=1
        elif state == "Cook":
            task_filename = ''.join(i for i in tasks[luto] if not i.isdigit()) + ".txt"
            task_file = open(task_filename, "r")

            cooking = task_filename

            for line in task_file:
            	cooking += "\n " + line

            """
            if ()
            if (prio_queue == "none"):
                cooking = tasks[luto]
                html += "<td>{}</td>".format( cooking )
            """
            html += "<td>{}</td>".format( cooking )
        else:
            html += "<td>{}</td>".format("")
        #"<td>{}</td>".format('<br>'.join("laman"))
    html += "</tr>"
html += "</table></html>"

output = open("output.html", "w+")
output.write(html)
output.close()