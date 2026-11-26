# student_marks.py

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

total = m1 + m2 + m3
average = total / 3

if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
else:
    grade = "C"

print("Total Marks =", total)
print("Average Marks =", average)
print("Grade =", grade)
