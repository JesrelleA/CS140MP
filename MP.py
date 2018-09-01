filename = "recipe.txt"
file = open(filename, "r")
for line in file:
   print(line)

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