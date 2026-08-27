# ============================================================
# Programming for AI - Week 2 Monday Lecture
# Lists: Python's Dynamic Workhorse
# ============================================================

# ============================================================
# 1. CREATING LISTS
# ============================================================

scores = [88, 92, 79, 95]

mixed = ["AI", 3.14, True, [1, 2]]

print("scores =", scores)

print("mixed =", mixed)


# ============================================================
# 2. LIST INDEXING
# ============================================================

scores = [88, 92, 79, 95]

print("scores[0] =", scores[0])

print("scores[-1] =", scores[-1])

print("scores[2] =", scores[2])


# ============================================================
# 3. MEMBERSHIP - in / not in
# ============================================================

fruits = ["apple", "banana", "mango"]

print('"banana" in fruits →', "banana" in fruits)

print('"grape" in fruits →', "grape" in fruits)

print('"grape" not in fruits →', "grape" not in fruits)


# ============================================================
# 4. MEMBERSHIP WITH IF
# ============================================================

enrolled = ["Asha", "Raj", "Meera"]

name = "Kabir"

if name not in enrolled:
    print(name, "→ must register first.")


# ============================================================
# 5. .append()
# ============================================================

queue = ["Asha", "Raj"]

queue.append("Meera")

print("After append('Meera') →", queue)


# Appending a list adds the entire list as ONE item
queue.append(["Kabir", "Dev"])

print("After append(['Kabir', 'Dev']) →", queue)

print("len(queue) →", len(queue))


# ============================================================
# 6. .extend()
# ============================================================

team_a = ["Asha", "Raj"]

team_b = ["Kabir", "Dev"]

team_a.extend(team_b)

print("After extend(team_b) →", team_a)

print("len(team_a) →", len(team_a))


# ============================================================
# 7. .insert()
# ============================================================

queue = ["Asha", "Raj", "Meera"]

queue.insert(1, "Priya")

print("After insert(1, 'Priya') →", queue)


# ============================================================
# 8. WORKED EXAMPLE - ATTENDANCE LIST
# ============================================================

attendance = []

attendance.append("Asha")

attendance.append("Raj")

attendance.extend(["Kabir", "Dev"])

attendance.insert(0, "Meera")

print("attendance →", attendance)

print('"Raj" in attendance →', "Raj" in attendance)

print("len(attendance) →", len(attendance))

