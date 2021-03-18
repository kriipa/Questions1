# N students take K apples and distribute them among each each other evenly .
# The remaining (the undivisible) part remains in the basket.
# How many apples will each single student get? How many apples will remain in the basket ?
# The program reads the number N  and K . It should print the two answers for the questions above.

apple_value = int(input("Enter the number of apple:"))
student_number = int(input("Enter the number of students:"))
divide = apple_value // student_number
remain = apple_value % student_number
print("each student=",divide)
print("remain=" ,remain)