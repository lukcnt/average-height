student_heights = input("Input a list of students heights in centimeters and "
                        "with a space between each one: ").split()

# I didn't use sum and len function purposely to get a better grasp of for loops.
sum_heights = 0
total_students = 0

for height in student_heights:
    sum_heights += int(height)
    total_students += 1

average_height = round(sum_heights / total_students)
print(f"The average height of the students are: {average_height} centimeters.")