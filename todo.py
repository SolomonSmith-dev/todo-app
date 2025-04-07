def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n📝 TO-DO LIST 📝")
        show_tasks(tasks)
        print("\nOptions: [A]dd, [R]emove, [Q]uit")
        choice = input("Choose an option: ").strip().lower()

        if choice == 'a':
            task = input("Enter new task: ").strip()
            tasks.append(task)
            save_tasks(tasks)
        elif choice == 'r':
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
            else:
                print("Invalid task number.")
        elif choice == 'q':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
