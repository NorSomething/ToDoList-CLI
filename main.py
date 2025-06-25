import os

tasks = {
        "completed" : [],
        "incompleted" : []
    }

comF = open("completedF.txt", "a")
incomF = open("incompleteF.txt", "a")

def main():
    print("Welcome to ToDoList.")
    while True:
        displayer()
    

def displayer():
    print("Press 1 to View Existing Tasks")
    print("Press 2 to Add Another Task")
    print("Press 3 to Set a Task as Complete")
    print("Press 4 to Exit")
    print()
    inp = int(input())
    print()
    def checker():
        if inp == 1:
            print("Completed :")
            lenC = len(tasks["completed"])
            for i in range(lenC):
                print(i+1, tasks["completed"][i])
                # print(*tasks["completed"], sep=",")
            print()
            print("Incomplete :")
            lenI = len(tasks["incompleted"])
            for i in range(lenI):
                print(i+1, tasks["incompleted"][i])
            print()
        elif inp == 2:
            task = input("Enter the Task to Add : ")
            tasks["incompleted"].append(task)
        elif inp == 3:
            print("Incomplete :")
            print(*tasks["incompleted"], sep=",")
            set = int(input("Which task to be set as Complete : (Numerical Value) "))
            tt = tasks["incompleted"].pop(set-1)
            tasks["completed"].append(tt)
        elif inp == 4:
            exit()
        else:
            print("wrong input")
    checker()




main()
