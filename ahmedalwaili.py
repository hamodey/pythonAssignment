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
length_of_goal = len(g1split)
elem1 = 0

def toyWorld():
    for i in range(length_of_list):
        s1[i] = s1[i].replace("(", " ")
        s1[i] = s1[i].replace(")", " ")
        s1[i] = s1[i].replace(",", " ")
        s1[i] = s1[i].split(" ")
        print(s1)
        if "on" in s1[i]:
            global elem1
            elem1 = s1[i][i+1]
            elem2 = s1[i][i+2]
            final.append(elem2)
            final.append(elem1)
            print(final, "this is final")
            print(elem1,"> is On > ", elem2)
            print("You want \n", elem2, "> is On > ", elem1)
    for j in range(length_of_goal):
        g0split[j] = g0split[j].replace("(", " ")
        g0split[j] = g0split[j].replace(")", " ")
        g0split[j] = g0split[j].replace(",", " ")
        g0split[j] = g0split[j].split(" ")
        print(g0split)

    copyS0.append(spltStr)
    g1split.append(elem1)
    # print(copyS0)
    empty = "empty"
    for i in range(len(g0split)):
        if g0split[i] == copyS0[0]:
            g0split[i] = empty

def isGoal(node):
    if str(node) == goal:
        return True
    else:
        return False


def generateChild(t):
    for i in t:
        if isinstance(i, list):
            if len(i) <= 0:  # empty list
                print("Empty List")
                return False
            else:
                generateChild(i)
        else:
            anw = isGoal(i)
            if anw:
                print(i)
                break

def main():
    toyWorld()
    generateChild(copyS0)

main()
