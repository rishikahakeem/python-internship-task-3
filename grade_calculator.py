test_cases = [
    (95, 98),
    (85, 80),
    (72, 76),
    (65, 70),
    (55, 85),
    (40, 90),
    (88, 60),
    (110, 80)
]
for marks, attendance in test_cases:

    print("\nMarks:", marks, "Attendance:", attendance)
    if marks < 0 or marks > 100 or attendance < 0 or attendance > 100:
        print("Invalid input")
    elif attendance < 75:
        print("Fail due to low attendance")
    else:
        if marks >= 90:
            print("Grade A+ : Excellent")
        elif marks >= 80:
            print("Grade A : Very Good")
        elif marks >= 70:
            print("Grade B : Good")
        elif marks >= 60:
            print("Grade C : Average")
        elif marks >= 50:
            print("Grade D : Needs Improvement")
        else:
            print("Grade E : Fail")
