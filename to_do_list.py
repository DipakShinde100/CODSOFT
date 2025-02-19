# To-Do List Application in Python (Command-line version)

class TodoApp:
    def __init__(self):
        # Initialize an empty list of tasks
        self.tasks = []

    def show_tasks(self):
        """Display the current list of tasks."""
        if len(self.tasks) == 0:
            print("\nNo tasks available.\n")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        print()

    def add_task(self):
        """Add a new task to the to-do list."""
        task = input("Enter a new task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.\n")

    def update_task(self):
        """Update an existing task."""
        self.show_tasks()
        try:
            task_num = int(input("Enter the number of the task to update: "))
            if 1 <= task_num <= len(self.tasks):
                new_task = input("Enter the updated task: ")
                self.tasks[task_num - 1] = new_task
                print(f"Task {task_num} has been updated.\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Invalid input! Please enter a valid task number.\n")

    def delete_task(self):
        """Delete an existing task."""
        self.show_tasks()
        try:
            task_num = int(input("Enter the number of the task to delete: "))
            if 1 <= task_num <= len(self.tasks):
                removed_task = self.tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' has been deleted.\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Invalid input! Please enter a valid task number.\n")

    def main_menu(self):
        """Display the main menu and handle user input."""
        while True:
            print("\nTo-Do List Application")
            print("1. View All Tasks")
            print("2. Add a Task")
            print("3. Update a Task")
            print("4. Delete a Task")
            print("5. Exit")

            choice = input("Choose an option (1-5): ")

            if choice == '1':
                self.show_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("Exiting To-Do List Application. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.\n")


if __name__ == "__main__":
    # Create an instance of TodoApp and start the application
    app = TodoApp()
    app.main_menu()
