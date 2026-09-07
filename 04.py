tasks = []

while True:

    print("\n--- TASK SCHEDULER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Execute Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter task name: ")
        priority = input("Is it high priority? (yes/no): ")

        tasks.append({
            "name": task,
            "priority": priority
        })

        print("Task added successfully!")

    elif choice == "2":

        if not tasks:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")
            for task in tasks:
                print("-", task["name"])

    elif choice == "3":

        for task in tasks:

            if task["priority"] == "yes" and task["name"] != "":
                print("Executing high priority task:", task["name"])

            elif task["priority"] == "no" or task["priority"] == "":
                print("Executing normal task:", task["name"])

            else:
                print("Task skipped")

    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    else:
        print("Invalid choice!")
