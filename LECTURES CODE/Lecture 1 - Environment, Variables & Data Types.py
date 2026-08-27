# ============================================================
# Programming for AI - Week 1 Lecture 1
# Environment, Variables & Data Types
# ============================================================


# ============================================================
# 1. BASIC PYTHON
# ============================================================

print("Hello, AI world!")


# ============================================================
# 2. INTERACTIVE SHELL EXAMPLES
# ============================================================

print("5 + 3 =", 5 + 3)

print('"Hello" + "World" =', "Hello" + "World")

print("10 / 4 =", 10 / 4)


# ============================================================
# 3. FILE EDITOR / SCRIPT MODE
# ============================================================

name = "Aditi"

print("Welcome to Python,", name)

print("Let's build AI together!")


# ============================================================
# 4. INTEGER (int)
# ============================================================

age = 17

print("age =", age, "type() =", type(age))

temperature = -5

print("temperature =", temperature)

big_number = 1000000

print("big_number =", big_number)


# ============================================================
# 5. FLOAT (float)
# ============================================================

pi_value = 3.14

print("pi_value =", pi_value, "type() =", type(pi_value))

height = 5.6

print("height =", height)

gpa = 9.2

print("gpa =", gpa)


# ============================================================
# 6. STRING (str)
# ============================================================

name = "Ravi"

print("name =", name, "type() =", type(name))

greeting = "Good Morning"

print("greeting =", greeting)

student_id = "12A-07"

print("student_id =", student_id)


# Digits inside quotes are strings
student_number = "123"

print("student_number =", student_number, "type() =", type(student_number))


# ============================================================
# 7. CHECKING DATA TYPES USING type()
# ============================================================

print("10 →", type(10))

print("3.14 →", type(3.14))

print('"AI" →', type("AI"))


# ============================================================
# 8. VARIABLES
# ============================================================

age = 17

print("age =", age)


# ============================================================
# 9. WORKING WITH VARIABLES
# ============================================================

student_name = "Meera"

student_age = 17

average_score = 88.5

print("student_name =", student_name)

print("student_age =", student_age)

student_age = 18

print("student_age after changing =", student_age)


# ============================================================
# 10. VALID VARIABLE NAMES
# ============================================================

student_name = "Punit"

age2 = 25

_score = 90

totalMarks = 95

class_XII = "A"

print("student_name =", student_name)

print("age2 =", age2)

print("_score =", _score)

print("totalMarks =", totalMarks)

print("class_XII =", class_XII)


# ============================================================
# 11. INVALID VARIABLE NAMES
# ============================================================

# These are examples from the lecture.
# They are kept as comments because they will produce errors.

# 2nd_score = 90
# student name = "Punit"
# class = "XII"
# total-marks = 95


# ============================================================
# 12. EXPRESSIONS
# ============================================================

print("4 + 5 =", 4 + 5)

print("2 * 3.5 =", 2 * 3.5)

print("10 - 4 * 2 =", 10 - 4 * 2)

print('"AI" + " " + "Class" =', "AI" + " " + "Class")


# ============================================================
# 13. ARITHMETIC OPERATORS
# ============================================================

print("5 + 2 =", 5 + 2)       # Addition

print("5 - 2 =", 5 - 2)       # Subtraction

print("5 * 2 =", 5 * 2)       # Multiplication

print("5 / 2 =", 5 / 2)       # Division

print("5 // 2 =", 5 // 2)     # Floor Division

print("5 % 2 =", 5 % 2)       # Modulus / Remainder

print("5 ** 2 =", 5 ** 2)     # Exponent / Power


# ============================================================
# 14. EXPRESSIONS WITH VARIABLES
# ============================================================

length = 5

breadth = 3

area = length * breadth

print("area = length * breadth =", area)


price = 49.5

quantity = 3

total_cost = price * quantity

print("total_cost = price * quantity =", total_cost)
