#simple to do list without file handling
tasks={}
while True:
    print("Welcome!\n")
    print("1.View tasks \n2.Add task\n3.Delete task\n4.Mark task as Done\n5.exit")
    choice=int(input("Choose: "))

    if choice==1:
        if len(tasks)==0:
            print("No tasks Added")
            continue
        for a,b in tasks.items():
            print(a+" : "+b)
                
    elif choice==2:
        i=int(input("Enter the amount of tasks to be added"))
        for x in range(i):
            tasks[input("Enter task")]="Not Done"
    elif choice==3:
        x=input("Enter the task")
        if x in tasks:
            tasks.pop(x)
        else:
            print("Invalid task")
    elif choice==4:
        for key in tasks:
            print(key)
        x=input("Which task should be marked as done?")
        if x in tasks:
            tasks[x]="Done"
        else:
            print("Invalid Task")
    elif choice==5:
            break
    else:
        print("Invalid choice")
