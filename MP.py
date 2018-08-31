filename = "recipe.txt"
file = open(filename, "r")
for line in file:
   print(line)

task = {"adob", "sinigang", "tapsilog"} 

#html = """<html><table border="1">
#<tr><th>Time</th><th>Cook</th><th>Ready</th><th>Assistants</th></tr>"""

clock = 0;
headers = ["Time", "Cook", "Ready", "Assistants", "Remarks"]
html = """<html><table border="1">
<tr>
    <th>Time</th>
    <th>Cook</th>
    <th>Ready</th>
    <th>Assistants</th>
    <th>Remarks</th>
</tr>"""

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