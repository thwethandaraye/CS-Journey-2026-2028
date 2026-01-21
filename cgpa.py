def s_to_c(score):
    if 98 <= score <= 100:
        return 4.00
    elif 93 <= score <= 97:
        return 4.00
    elif 90 <= score <= 92:
        return 3.67
    elif 88 <= score <= 89:
        return 3.33
    elif 83 <= score <= 87:
        return 3.0
    elif 80 <= score <= 82:
        return 2.67
    elif 78 <= score <= 79:
        return 2.33
    elif 73 <= score <= 77:
        return 2.00
    elif 70 <= score <= 72:
        return 1.67
    elif 68 <= score <= 69:
        return 1.33
    elif 63 <= score <= 67:
        return 1.00
    else:
        return 0.00

while True:
    try:
        c = int(input("Enter numbers of courses you have finished:"))
        if 1 <= c <= 40:
            break
        else:
            print("Error: Courses must be between 1 and 40.")
    except ValueError:
        print("Error: Please enter a valid number.")

total_g = 0.0
for i in range(1, c + 1):
    while True:
        try:
            score = float(input(f"Enter score for course {i} (0-100): "))
            if 0 <= score <= 100:
                total_g += s_to_c(score)
                break
            else:
                print("Score must between 0 and 100.")
        except ValueError:
            print("Please enter a valid score.")

cgpa = total_g / c

print("\n#........ RESULT ........#")
print(f"Total Courses: {c}")
print(f"Your CGPA (UoPeople): {cgpa:.2f}")