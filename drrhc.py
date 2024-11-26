import json

def get_user_input():
    name = input("Enter your name: ")
    return name

def save_to_file(names, filename="slambook_names.json"):
    with open(filename, 'w') as f:
        json.dump(names, f, indent=4)
    print(f"Names saved to {filename}")

def load_from_file(filename="slambook_names.json"):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def display_names(names):
    print("\nList of Names in Slambook:")
    for name in names:
        print(name)

def main():
    names = load_from_file()

    while True:
        action = input("\nWould you like to (A)dd a name, (D)isplay names, or (Q)uit? ").lower()
        
        if action == 'a':
            name = get_user_input()
            names.append(name)
            save_to_file(names)
        elif action == 'd':
            display_names(names)
        elif action == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()
