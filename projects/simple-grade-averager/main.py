def get_grades():
    grades = []
    while True:
        grade_input = input("Enter grades (separated by spaces, type 'done' when finished): ")
        grade_list = grade_input.split()
        for grade_str in grade_list:
            if grade_str.lower() == 'done':
                return grades
            try:
                grade = float(grade_str)
                if 0 <= grade <= 100:
                    grades.append(grade)
                else:
                    print("Invalid grade. Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number or 'done'.")


def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)


if __name__ == "__main__":
    grades = get_grades()
    if grades:
        average = calculate_average(grades)
        print(f"Average grade: {average}")
    else:
        print("No grades entered.")
