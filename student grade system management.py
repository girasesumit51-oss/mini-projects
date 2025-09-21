# Student Grade System in Python

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def main():
    print("===== Student Grade System =====")
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    
    subjects = int(input("Enter number of subjects: "))
    total = 0
    
    for i in range(1, subjects + 1):
        marks = float(input(f"Enter marks for subject {i}: "))
        total += marks
    
    average = total / subjects
    grade = calculate_grade(average)
    
    print("\n===== Report Card =====")
    print("Name:", name)
    print("Roll Number:", roll)
    print("Total Marks:", total)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)

if __name__ == "__main__":
    main()
