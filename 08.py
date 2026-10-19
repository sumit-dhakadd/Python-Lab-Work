def score_report(*marks, **details):
    if len(marks) == 0:
        return 0, 0, 0, {}

    lowest = min(marks)
    highest = max(marks)
    avg = sum(marks) / len(marks)

    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for mark in marks:
        letter = (
            "A" if mark >= 90 else
            "B" if mark >= 80 else
            "C" if mark >= 70 else
            "D" if mark >= 60 else
            "F"
        )
        grades[letter] += 1

    print("Assessment Details:", details)
    return lowest, highest, avg, grades


scores = [int(value) for value in input("Enter grades separated by spaces: ").split()]

low, high, mean, result = score_report(
    *scores, subject="Python", class_name="BCA"
)

print("Minimum Grade:", low)
print("Maximum Grade:", high)
print("Average Grade:", round(mean, 2))
print("Letter Grade Distribution:", result)
