# Interactive Student Gradebook Manager (Dict & Set Operations)

def run_gradebook():
    gradebook = {
        "Alice": [85, 90, 92],
        "Bob": [78, 80, 70],
    }

    while True:
        print("\n=== Student Gradebook ===")
        print("1. View all students")
        print("2. Add student / grade")
        print("3. View student stats")
        print("4. Exit")

        choice = input("Choice (1-4): ").strip()

        if choice == "1":
            print("\nCurrent Students:")
            for name, grades in gradebook.items():
                avg = sum(grades) / len(grades) if grades else 0
                print(f"  - {name}: Grades={grades} | Avg={avg:.1f}")

        elif choice == "2":
            name = input("Student name: ").strip().title()
            if not name:
                continue
            try:
                grade = float(input(f"Enter grade for {name}: "))
                gradebook.setdefault(name, []).append(grade)
                print(f"Added grade {grade} to {name}.")
            except ValueError:
                print("Invalid number!")

        elif choice == "3":
            name = input("Student name: ").strip().title()
            if name in gradebook:
                grades = gradebook[name]
                print(f"\nStats for {name}:")
                print(f"  Highest Grade: {max(grades)}")
                print(f"  Lowest Grade:  {min(grades)}")
                print(f"  Unique Grades: {set(grades)}")
            else:
                print("Student not found!")

        elif choice == "4":
            print("Exiting Gradebook.")
            break
        else:
            print("Invalid selection!")

if __name__ == "__main__":
    run_gradebook()
