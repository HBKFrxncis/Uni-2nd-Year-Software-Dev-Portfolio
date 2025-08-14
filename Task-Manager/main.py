# Initialize dictionaries for tasks
days_of_week = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

months_of_year = {
    "January": [],
    "February": [],
    "March": [],
    "April": [],
    "May": [],
    "June": [],
    "July": [],
    "August": [],
    "September": [],
    "October": [],
    "November": [],
    "December": []
}

def add_task(tasks_dict, time_period):
    print(f"Add a task to {time_period}:")
    task = input("Enter the task: ")
    if task:
        tasks_dict.append(task)
        print(f"Task added to {time_period}!")
    else:
        print("No task entered.")

def view_tasks(tasks_dict, time_period):
    if tasks_dict:
        print(f"Tasks for {time_period}:")
        for task in tasks_dict:
            print(f"- {task}")
    else:
        print(f"No tasks for {time_period}.")

def delete_task(tasks_dict, time_period):
    view_tasks(tasks_dict, time_period)
    if tasks_dict:
        task_to_delete = input("Enter the task to delete: ")
        if task_to_delete in tasks_dict:
            tasks_dict.remove(task_to_delete)
            print(f"Task deleted from {time_period}.")
        else:
            print("Task not found.")
    else:
        print("No tasks to delete.")

def main():
    while True:
        print("\nTask Manager Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            print("\nChoose the time period to add a task:")
            print("1. Day of the week")
            print("2. Month of the year")
            try:
                time_choice = int(input("Enter your choice: "))
                if time_choice == 1:
                    day = input("Enter the day (e.g., Monday, Tuesday, etc.): ").capitalize()
                    if day in days_of_week:
                        add_task(days_of_week[day], day)
                    else:
                        print("Invalid day.")
                elif time_choice == 2:
                    month = input("Enter the month (e.g., January, February, etc.): ").capitalize()
                    if month in months_of_year:
                        add_task(months_of_year[month], month)
                    else:
                        print("Invalid month.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == 2:
            print("\nChoose the time period to view tasks:")
            print("1. Day of the week")
            print("2. Month of the year")
            try:
                time_choice = int(input("Enter your choice: "))
                if time_choice == 1:
                    day = input("Enter the day (e.g., Monday, Tuesday, etc.): ").capitalize()
                    if day in days_of_week:
                        view_tasks(days_of_week[day], day)
                    else:
                        print("Invalid day.")
                elif time_choice == 2:
                    month = input("Enter the month (e.g., January, February, etc.): ").capitalize()
                    if month in months_of_year:
                        view_tasks(months_of_year[month], month)
                    else:
                        print("Invalid month.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == 3:
            print("\nChoose the time period to delete a task:")
            print("1. Day of the week")
            print("2. Month of the year")
            try:
                time_choice = int(input("Enter your choice: "))
                if time_choice == 1:
                    day = input("Enter the day (e.g., Monday, Tuesday, etc.): ").capitalize()
                    if day in days_of_week:
                        delete_task(days_of_week[day], day)
                    else:
                        print("Invalid day.")
                elif time_choice == 2:
                    month = input("Enter the month (e.g., January, February, etc.): ").capitalize()
                    if month in months_of_year:
                        delete_task(months_of_year[month], month)
                    else:
                        print("Invalid month.")
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
