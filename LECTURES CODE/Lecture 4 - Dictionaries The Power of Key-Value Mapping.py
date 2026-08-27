# ============================================================
# Programming for AI - Week 3
# Dictionaries: The Power of Key-Value Mapping
# ============================================================


# ============================================================
# 1. CREATING A DICTIONARY
# ============================================================

student = {
    "name": "Asha",
    "age": 21,
    "city": "Bengaluru"
}

print(student["name"])

print(student["age"])


# ============================================================
# 2. MODELING REAL-WORLD OBJECTS
# ============================================================

user_profile = {
    "name": "Kabir",
    "age": 24,
    "location": "Gurugram"
}

print(user_profile["location"])


# Update an existing value
user_profile["age"] = 25


# Add a brand-new key
user_profile["email"] = "k@ex.com"

print(user_profile)


# ============================================================
# 3. MISSING KEY - KeyError
# ============================================================

user_profile = {
    "name": "Kabir",
    "age": 24
}

# This will cause a KeyError because "email" does not exist.
# print(user_profile["email"])


# ============================================================
# 4. GUARDING AGAINST KeyError USING in
# ============================================================

user_profile = {
    "name": "Kabir",
    "age": 24
}

if "email" in user_profile:
    print(user_profile["email"])
else:
    print("No email on file.")


# ============================================================
# 5. setdefault()
# ============================================================

user_profile = {
    "name": "Kabir",
    "age": 24
}

email = user_profile.setdefault("email", "not provided")

print(email)


# Existing key - value remains unchanged
name = user_profile.setdefault("name", "Unknown")

print(name)


# ============================================================
# 6. WORD FREQUENCY COUNTING
# ============================================================

words = ["ai", "ml", "ai", "nlp", "ml", "ai"]

counts = {}

for w in words:
    counts[w] = counts.setdefault(w, 0) + 1

print(counts)


# ============================================================
# 7. PRACTICE - BOOK DICTIONARY
# ============================================================

book = {
    "title": "Python 101",
    "pages": 320
}


# Safely check whether "author" exists
if "author" in book:
    print(book["author"])
else:
    print("Author key does not exist.")


# Add "author" only if it is missing
book.setdefault("author", "Unknown")


# Update pages
book["pages"] = 350


# Add a brand-new key
book["edition"] = 1


print(book)