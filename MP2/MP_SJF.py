def shortest_job_first(ready):
    print("INSIDE shortest_job_first FUNCTION")
    print("ready : ", ready)
    cooktime = ready[0].time_left_for_step()
    dish_to_cook1 = ready[0]
    counter = 0
    p = counter
    for counter in range(len(ready)):
        print("loop")
        print("dish name : ", ready[counter].name)
        print("dish name time cook : ", ready[counter].time_left_for_step())
        print("cooktime = ", cooktime)
        if (ready[counter].time_left_for_step() < cooktime):
            if (ready[counter].time_left_for_step() == cooktime):
                print("EQUAL SILA OMO")
            else:
                dish_to_cook1 = ready[counter]
                print("chosen dish = ", dish_to_cook1)
                p = counter

        print("[inside loop] dish_to_cook1 = ", dish_to_cook1.name)

    ready.pop(p)
    print("[to return] dish_to_cook1 = ", dish_to_cook1.name)
    return dish_to_cook1
