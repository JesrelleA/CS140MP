18c18
<     def __init__(self, name, time, priority, recipe):
---
>     def __init__(self, name, time):
21d20
<         self.priority = priority
43,47d41
< dishlist = []
< 
< f = open("Tasklist.txt", "r") #open file
< with open('Tasklist.txt') as f:
<     c = [word for line in f for word in line.split()]
49,51c43,45
< f.close()
< p = 1
< i = 0
---
> tasks_count = {}
> tasks       = {}
> dishlist = []
53a48,70
> # from Ri file
> filename = "tasklist.txt"
> file = open(filename, "r")
> 
> for line in file:
>     task_i       = line.split()[0]
>     task_sched_i = int(line.split()[1])
> 
>     if task_i not in tasks_count:    # for 1st encounter with task
>         tasks_count.update({task_i : 1})
>         tasks.update({ task_sched_i : str(task_i+"1")})
>         
>         task = Recipe(str(task_i+"1"), task_sched_i)
>         print("made task", task_i, "with time", task_sched_i)
>         dishlist.append(task)
>     else:                            # for all subsequent encounters
>         tasks_count.update({task_i : tasks_count[task_i]+1})
>         task_v = task_i + str(tasks_count[task_i])
>         tasks.update({ task_sched_i : task_v})
>         
>         task = Recipe(task_v, task_sched_i)
>         print("made task", task_v, "with sched", task_sched_i)
>         dishlist.append(task)
54a72
> """
64a83,85
> """
> 
> 
65a87,89
> """
> p = 1
> i = 0
77a102,103
> """
> 
129a156,175
>     if time in tasks: 
>         task_filename = ''.join(i for i in tasks[time] if not i.isdigit()) + ".txt" # gets file
>         task_file = open(task_filename, "r")   
> 
> 
>         line_num = 0
>         for line in task_file:
>             # print("current recipe is", tasks_list[0])
>             step       =     line.split()[0]      # gets step at a time
>             step_time  = int(line.split()[1]) # gets duration of step
>             dishlist[0].add_step(step, step_time) # adds new Step object to recipe
>             
>             #step_node = [step, step_time]
>             #recipe.append(step_node)
> 
>             line_num += 1
> 
> 
> 
> 
252c298
<     output = " <td style=\"background-color:gray\">" + str(time) + "</td>" #" <th>" + str(time) + "</th>"
---
>     output = " <td> bgcolor=\"gray\">" + str(time) + "</td>" #" <th>" + str(time) + "</th>"
287,290c333,336
<     #if assistants_empty == True:
<         #print("none")
<         #f3.write("  <th>none</th>")
<         #stop = stop + 1 #assistants_empty, stop = False, stop + 1
---
>     if assistants_empty == True:
>         print("none")
>         f3.write("  <th>none</th>")
>         stop = stop + 1 #assistants_empty, stop = False, stop + 1
308c354
<     if (len(assistants) == 0) or (assistants_empty == True): #assistants_empty == True:
---
>     if (len(assistants) == 0) and (assistants_empty == True): #assistants_empty == True:
311c357
<         stop = stop + 1#h = input()
---
>         #h = input()
313c359
<         f3.write("  <th>none</th>")
---
>         f3.write(printthis)
