# ============================================================
# Programming for AI - Extra Lecture
# Python Loops: The Engines of Automation
# ============================================================

# ============================================================
# 1. WITHOUT A LOOP
# ============================================================

# Tedious and does not scale

print("scores[0] =", scores[0])
print("scores[1] =", scores[1])
print("scores[2] =", scores[2])
print("scores[3] =", scores[3])


# ============================================================
# 2. WHILE LOOP
# ============================================================

count = 1

while count <= 5:
    print("count =", count)
    count += 1

print("Done! → while loop finished")


# ============================================================
# 3. INFINITE LOOP EXAMPLE
# ============================================================

# count = 1
#
# while count <= 5:
#     print(count)
#     # forgot count += 1
#
#     # The condition never becomes False.


# ============================================================
# 4. FOR LOOP - LIST
# ============================================================

cats = ["Tom", "Whiskers", "Luna"]

for cat in cats:
    print(cat, "→ says meow")


# ============================================================
# 5. FOR LOOP - STRING
# ============================================================

for letter in "AI":
    print("letter =", letter)


# ============================================================
# 6. SINGULAR AND PLURAL NAMING
# ============================================================

for cat in cats:
    print("cat =", cat)

for x in cats:
    print("x =", x)


# ============================================================
# 7. range()
# ============================================================

# range(5) generates:
# 0, 1, 2, 3, 4

for i in range(5):
    print("i =", i, "→ Hello!")


# range(1, 5) generates:
# 1, 2, 3, 4

for i in range(1, 5):
    print("range(1, 5) →", i)


# range(0, 10, 2) generates:
# 0, 2, 4, 6, 8

for i in range(0, 10, 2):
    print("range(0, 10, 2) →", i)


# ============================================================
# 8. OFF-BY-ONE EXAMPLE
# ============================================================

for day in range(1, 5):
    print("Day", day)

# Output:
# Day 1
# Day 2
# Day 3
# Day 4


# To print Day 1 through Day 5:
for day in range(1, 6):
    print("Day", day)


# ============================================================
# 9. break
# ============================================================

for num in range(1, 10):

    if num == 5:
        print("num =", num, "→ break: loop stopped")
        break

    print("num =", num)


# ============================================================
# 10. continue
# ============================================================

for num in range(1, 6):

    if num == 3:
        print("num =", num, "→ continue: skipped")
        continue

    print("num =", num)


# ============================================================
# 11. pass
# ============================================================

for num in range(1, 6):

    if num == 3:
        pass  # TODO: handle this case later

    print("num =", num, "→ pass does nothing")


# ============================================================
# 12. CORRECT INDENTATION
# ============================================================

for cat in cats:
    print("cat =", cat)
    print("---")

print("done → loop finished")


# ============================================================
# 13. LOOP ELSE
# ============================================================

for num in [2, 4, 6, 8]:

    if num % 2 != 0:
        break

else:
    print("All numbers were even. → loop completed normally")


# ============================================================
# 14. LOOP ELSE - ANOTHER EXAMPLE
# ============================================================

enrolled = ["Asha", "Raj", "Meera", "Kabir"]

target = "Meera"

for name in enrolled:

    if name == target:
        print(target, "→ found!")
        break

else:
    print(target, "→ not found in the list.")


# ============================================================
# 15. SEARCHING WITH break
# ============================================================

enrolled = ["Asha", "Raj", "Meera", "Kabir"]

target = "Meera"

for name in enrolled:

    if name == target:
        print(target, "→ found!")
        break

else:
    print(target, "→ not found in the list.")

