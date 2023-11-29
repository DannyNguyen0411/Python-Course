student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0

# using sum loop
for height in student_heights:
  total_height += height
# print(total_height)

total_students = 0

# using len loop
for students in student_heights:
  total_students += 1
# print(total_students)

average_height = total_height / total_students

print(round(average_height))

asking = input("Are you exited about the scores of the students?")


if asking.lower() == "yes":

    print("Welcome to the best scores")
    student_scores = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
       student_scores[n] = int(student_scores[n])
       
       highest_scores = 0
    for scores in student_scores:
        if scores > highest_scores:
           highest_scores = scores
    print(f"The highest score in the class is: {highest_scores}")

elif asking.lower() == "no":
    print("Welcome to the failure scores")
    student_scores = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])

        lowest_scores = 9999999999999999999999999999999999999999
        for scores in student_scores:
            if scores < lowest_scores:
               lowest_scores = scores

    print(f"The highest score in the class is: {lowest_scores}")