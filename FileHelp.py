def displayer():
    print("Press 1 to View Existing Tasks")
    print("Press 2 to Add Another Task")
    print("Press 3 to Set a Task as Complete")
    print("Press 4 to Exit")
    inp = int(input())
    if inp == 1:
        print("Completed : ")
        ReadComeF = open("completedF.txt")
        for line in ReadComeF:
            print(line)
        ReadComeF.close()
        print("Incomplete : ")
        ReadIncomF = open("incompleteF.txt")
        for line in ReadIncomF:
            print(line)
        ReadIncomF.close()
    if inp == 2:
        print("Enter Task Name : ", end="")
        inp = input()
        AppendInComeF = open("incompleteF.txt", "a")
        AppendInComeF.write(inp)
        AppendInComeF.close()
    if inp == 3:
        ReadInComeF2 = open("completedF.txt")
        

displayer()