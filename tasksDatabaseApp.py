tasks={}
menu="""
1) View Tasks
2) Fetch all the records
3) Add Task
4) Exit
"""
while True:
    print("-----Tasks Database-----")
    print(menu)
    choice = int(input("Enter Your Choice"))
    if choice==1:
        if len(tasks.keys())==0:
            print("No Records in the list")
        else:
            name=input("Enter the name to find task")
            answer=tasks.get(name, "No record found")
            print(answer)

    elif choice==2:
        if len(tasks.keys())==0:
            print("No Records in the list")
        else:
            for i in tasks.items():
                print(i)
    elif choice==3:
        name=input("Enter the task you want to add")
        date=input("Enter the date of task")
        tasks[name]=date
        print("Record added")
    elif choice==4:
        break
    else:
        print("Invalid choice please try again!")