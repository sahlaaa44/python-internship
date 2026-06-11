class TaskNotFoundError(Exception):
    pass


class TaskAlreadyExistsError(Exception):
    pass


tasks = {}


def get_all_tasks() -> list:
    return list(tasks.values())


def get_task(id: int) -> dict:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")

    return tasks[id]


def create_task(data: dict) -> dict:
    task_id = data["id"]

    if task_id in tasks:
        raise TaskAlreadyExistsError("Task ID already exists")

    tasks[task_id] = data
    return data


def update_task(id: int, data: dict) -> dict:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")

    tasks[id].update(data)
    return tasks[id]


def delete_task(id: int) -> bool:
    if id not in tasks:
        raise TaskNotFoundError("Task not found")

    del tasks[id]
    return True


while True:
    print("\n___TASK MANAGER___")
    print("1. View all tasks")
    print("2. View task")
    print("3. Create task")
    print("4. Update task")
    print("5. Delete task")
    print("6. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == "1":
            print(get_all_tasks())

        elif choice == "2":
            task_id = int(input("Enter task ID: "))
            print(get_task(task_id))

        elif choice == "3":
            task_id = int(input("Enter ID: "))
            title = input("Enter title: ")

            task = {
                "id": task_id,
                "title": title
            }

            print(create_task(tasks))

        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            new_title = input("Enter new title: ")

            print(update_task(task_id, {"title": new_title}))

        elif choice == "5":
            task_id = int(input("Enter task ID: "))

            if delete_task(task_id):
                print("Task deleted")

        elif choice == "6":
            print("Bye!")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number.")

    except Exception as e:
        print("Error:", e)