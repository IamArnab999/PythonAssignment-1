def calculate_grade(marks):
    average = sum(marks) / len(marks)
    
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def main():
    subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
    marks = []

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    grade = calculate_grade(marks)
    print("Average marks:", sum(marks) / len(marks))
    print("Grade:", grade)

if __name__ == "__main__":
    main()
