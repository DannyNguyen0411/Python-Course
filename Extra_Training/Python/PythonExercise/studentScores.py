student_scores = {
    "Harry": 85,
    "Ron": 80,
    "Hermeline": 100,
    "Draco": 71,
    "Neville": 60,
    "Gandalf the Gray": 100,
}

student_result = {}

for student in student_scores:
    score = student_scores[student]
    if score >= 90:
        student_result[student] = "Good Job"
    else:
        student_result[student_scores] = "Failure"

print(student_result)