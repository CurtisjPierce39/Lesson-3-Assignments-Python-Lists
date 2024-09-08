#Question 1 Task 1
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(key = int, reverse = True)
print(grades)
average = sum(grades) / len(grades)  #Question 1 Task 2
print("The average of the list is:", {average})