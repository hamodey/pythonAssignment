objStr = str(input("Input all your objects: "))
spltStr = objStr.split(" ")
print("Here you can see your objects: ", spltStr)
s0 = input("Please describe your initial state: ").lower()
s1 = s0.split(" ")
goal = input("Input your goal: ").lower()
g0split = goal.split(" ")
g1split = []
copyS0 = []
final = []
length_of_list = len(s1)
length_of_goal = len(g0split)

def toyWorld():
    for i in range(length_of_list):
        # Sn state is split into a list for search
        s1[i] = s1[i].replace("(", " ")
        s1[i] = s1[i].replace(")", "")
        s1[i] = s1[i].replace(",", " ")
        s1[i] = s1[i].split(" ")
        # print(s1)

    for a in range(length_of_list):
        if s1[a][0] == "on":
            # identifies which element is ON which element
            elem1 = s1[a][1] # this is A (elem1)
            elem2 = s1[a][2] # A is on this(elem2) on(elem1,elem2)
            final.append(elem1)
            final.append(elem2) # added to final list in order of ON

        if s1[a][0] == "clear":
            # identifies which element is CLEAR on top
            global clearElem
            clearElem = s1[a][1]
            # print(clearElem, "is clear")

    for j in range(length_of_goal):
        # goal state being split into a list for the search

        g0split[j] = g0split[j].replace("(", " ")
        g0split[j] = g0split[j].replace(")", "")
        g0split[j] = g0split[j].replace(",", " ")
        g0split[j] = g0split[j].split(" ")
        # print(g0split)

    for b in range(length_of_goal):
        global goalOn1
        global goalOn2
        if "on" in g0split[b]:
            goalOn1 = g0split[b][1] # splits the entities on which is ON
            goalOn2 = g0split[b][2] # on(goalOn1, goalOn2) on(s[a][1],
            for a in range(length_of_list):
                global search1
                global search2
                if s1[a][0] == "on":
                    if s1[a][1] == goalOn1:
                        # identifies which element is ON which element
                        search1 = s1[a][1]  # this is A (elem1)
                        search2 = s1[a][2]  # A is on this(elem2)
        ############
        global goalClr
        if "clear" in g0split[b]:
            # print(g0split[b])
            notIn = [item for item in spltStr if item not in final]
            # x for x in a if x not in [2, 3, 7]
            goalClr = g0split[b][1]
            search2 = goalClr
            # print(notIn, "NOT IN ")
            for c in range(length_of_list):
                if s1[c][0] == "on":
                    if s1[c][2] == goalClr:
                        goalOn1 = s1[c][1]  # this is A (elem1)
                        # goalOn2 = notIn[c]
                        if notIn == []:
                            goalOn2 = g0split[2]
                        else:
                            goalOn2 = notIn[c]
        # Printing the move operator
        print("Move( %s, %s, %s)" % (goalOn1, search2, goalOn2))

def main():
    toyWorld()

main()
