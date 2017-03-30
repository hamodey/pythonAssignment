objStr = str(input("Input all your objects: ")) # input of all the objects
spltStr = objStr.split(" ") # objects split into a list to navigate through
print("Here you can see your objects: ", spltStr)
s0 = input("Please describe your initial state: ").lower() # input of the current stat
s1 = s0.split(" ") # splits the instial state to navigate through and search
goal = input("Input your goal: ").lower()
g0split = goal.split(" ") # splits the goal to navigate through8
g1split = []
copyS0 = []
final = [] # a holding list to test for which is empty and has nothing on top when appended
length_of_list = len(s1) # length of state1
length_of_goal = len(g0split) # length of g0split

def toyWorld():
    for i in range(length_of_list):
        # Sn state is split into a list for search
        # this will be useful to identify each index in the list to test
        s1[i] = s1[i].replace("(", " ")
        s1[i] = s1[i].replace(")", "") # close brackets are deleted as they are not needed
        s1[i] = s1[i].replace(",", " ")
        s1[i] = s1[i].split(" ")  # split where spaces are available to have a 2d list
        # print(s1)

    for a in range(length_of_list):
        if s1[a][0] == "on":
            # identifies which element is ON which element
            elem1 = s1[a][1]  # this is A (elem1)
            elem2 = s1[a][2]  # A is on this(elem2) on(elem1,elem2)
            final.append(elem1)
            final.append(elem2)  # added to final list in order of ON
                                 # this will be used to test weather a table is empty or not

        if s1[a][0] == "clear":
            # identifies which element is CLEAR on top
            global clearElem
            clearElem = s1[a][1]  # clear only takes one parameter so only one is need [1]

            # print(clearElem, "is clear")

    for j in range(length_of_goal):
        # goal state being split into a list for the search

        g0split[j] = g0split[j].replace("(", " ")
        g0split[j] = g0split[j].replace(")", "")  # close brackets are deleted as they are not needed
        g0split[j] = g0split[j].replace(",", " ")
        g0split[j] = g0split[j].split(" ")  # split where spaces are available to have a 2d list
        # print(g0split)

    for b in range(length_of_goal):
        global goalOn1
        global goalOn2
        if "on" in g0split[b]:  # search for on in the first index of a 2d list in the FIRST dimension
            goalOn1 = g0split[b][1] # splits the entities on which is ON
            goalOn2 = g0split[b][2] # on(goalOn1, goalOn2) on(s[a][1], s[a][2])
            for a in range(length_of_list):
                global search1
                global search2
                if s1[a][0] == "on":  # search for on in the first index of a 2d list in the second dimension
                    if s1[a][1] == goalOn1:
                        # identifies which element is ON which element
                        search1 = s1[a][1]  # this is A (elem1)
                        search2 = s1[a][2]  # A is on this(elem2)
        ############
        global goalClr
        if "clear" in g0split[b]:  # searches for the clear in the first dimension
            # print(g0split[b])
            notIn = [item for item in spltStr if item not in final]  # checks with the final list to see weather something is empty or not (like table2 in the assignment page2)
            # x for x in a if x not in [2, 3, 7]
            goalClr = g0split[b][1]
            search2 = goalClr  # where its moving from
            # print(notIn, "NOT IN ")
            for c in range(length_of_list):
                if s1[c][0] == "on":  # searching for on in the second dimension of the 2d list
                    if s1[c][2] == goalClr:  #  if the goal on on is the clear then the first index needs to be cleared - hence below
                        goalOn1 = s1[c][1]  # this is A (elem1)
                        # goalOn2 = notIn[c]
                        if notIn == []:  # if the not in list is empty therefore there is no clear
                            goalOn2 = g0split[2]  # the seconds index of goal
                        else:
                            goalOn2 = notIn[c]
        # Printing the move operator
        print("Move( %s, %s, %s)" % (goalOn1, search2, goalOn2))  # formatting of the Move operator to loop via the list and print any movement and changes in goalOn1 goalOn2 and search2

def main():
    toyWorld()

main()
