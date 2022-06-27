def show_menu():
    print("1. Add To Do")
    print("2. Delete To Do")
    print("3. Quite")

def add_todo(todo_list):
    user_input = input("To Do: ")
    todo_list.append(user_input)

def show_todo(todo_list):
    print("-" * 20)
    for i, todo in enumerate(todo_list):
        print(i+1, todo)
    print("-" * 20)

def delete_todo(todo_list):
    user_input = input("Index: ")
    index = int(user_input)-1
    del todo_list[index]

def main():
    todo_list = []

    while True:
        show_menu()
        user_input = input(">> ")

        if user_input == '1':
            add_todo(todo_list)
            show_todo(todo_list)
        elif user_input == '2':
            delete_todo(todo_list)
            show_todo(todo_list)
        elif user_input == '3':
            break

main()