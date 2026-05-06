from typing import Any

# """
# Day 2: Dictionary-Based Student Grading System
# ===============================================

# BUILD OBJECTIVE:
# Create a grading system using dictionaries as the primary data structure.
# Track students, their grades, and compute statistics.

# DEFEND: Narrative Comments on Data Structures, Mutability, and Memory Management
# =================================================================================

# Why Dictionaries (Not Lists)?
# - We use dictionaries with student names as KEYS because lookup is O(1) average case.
# - Lists would force O(n) iteration to find a student. With dictionaries, accessing
#   a student's grades is instant (hash table lookup).
# - KEY INSIGHT: The dict's internal hash table maps keys to memory addresses. When we
#   call students["Alice"], Python computes hash("Alice"), probes the hash table, and
#   retrieves the value in constant time on average. This is WHY we chose dicts.

# References vs. Values in Dictionaries:
# - When we do students["Alice"] = {"math": 90, "english": 85}, we are NOT copying
#   the inner dictionary. We are storing a REFERENCE to that dictionary object.
# - The variable "grades" in students["Alice"] and the variable "grades" in a loop
#   both point to the SAME object in memory. Mutating one mutates the other.
# - Example: If we later do students["Alice"]["math"] = 95, we are modifying the
#   actual dictionary object, not a copy. This is because Python passes REFERENCES,
#   not values (unless explicitly copying).

# Object Identity and Mutability:
# - Each dictionary is a unique object with an id() in memory. The dictionary itself
#   is MUTABLE - we can add, remove, or modify keys without creating a new object.
# - When we call students["Alice"]["math"] = 95, we are NOT creating a new dictionary.
#   We are modifying the existing object at that memory location.
# - This is efficient (O(1) insertion/update) but requires care: if multiple variables
#   point to the same dictionary, changing it through one reference affects all others.

# Time Complexity Analysis:
# - Lookup: students["Alice"] -> O(1) average case (hash table)
# - Insert: students["Bob"] = {...} -> O(1) average case
# - Update: students["Alice"]["math"] = 95 -> O(1) average case
# - Delete: del students["Alice"] -> O(1) average case
# - Iteration: for name in students -> O(n) where n is number of students

# Space Complexity:
# - O(n * m) where n = number of students, m = average number of subjects per student.
# - Each dictionary entry consumes space proportional to the number of key-value pairs.

# Why NOT Use Nested Classes or Custom Objects?
# - Dictionaries are flexible: we can add new subjects without modifying the class.
# - For this simple system, OOP overhead is unnecessary. Dicts are lean and dynamic.
# - The tradeoff: we lose type hints and IDE autocomplete, but gain flexibility.
# """

# # ============================================================================
# # EXECUTION FLOW AND INTERPRETER BEHAVIOR
# # ============================================================================
# # When Python loads this file, it creates a module object. Each function
# # definition creates a function object in memory. Variables are bound to
# # objects, not the other way around. This is WHY dictionaries are mutable:
# # the variable stores a REFERENCE to the dict, not the dict itself.

# # ============================================================================
# # CORE DATA STRUCTURE: The Students Dictionary
# # ============================================================================
# # Structure:
# # {
# #     "student_name": {
# #         "subject": grade,
# #         "subject": grade,
# #         ...
# #     },
# #     ...
# # }
# #
# # MEMORY MODEL:
# # The outer dict is a hash table. Each key (student name) hashes to a bucket.
# # Each value is a REFERENCE to an inner dict (another hash table).
# # Modifying students["Alice"]["math"] mutates the inner dict object.
# # This is O(1) because we're not copying; we're changing the object in place.

# students = {
#     "Alice": {"math": 92, "english": 88, "science": 95},
#     "Bob": {"math": 78, "english": 92, "science": 85},
#     "Charlie": {"math": 88, "english": 76, "science": 91},
# }

# # ============================================================================
# # FUNCTION 1: Add a new student
# # ============================================================================
# def add_student(name, grades):
#     """
#     Add a student to the grading system.
    
#     MEMORY BEHAVIOR:
#     - 'name' is a string object in memory. The reference to this object is
#     stored as a key in the students dict.
#     - 'grades' is a dictionary object. We store a REFERENCE to it in students[name].
#     - If the caller modifies 'grades' after calling add_student(), the students
#     dict sees those changes because it's the same object (same memory address).
#     - This is mutability in action: the grades dict is mutable, so changes propagate.
    
#     TIME COMPLEXITY: O(1)
#     - Dictionary insertion is constant time on average.
#     """
#     students[name] = grades
#     print(f"Added {name} with grades: {grades}")


# # ============================================================================
# # FUNCTION 2: Update a student's grade
# # ============================================================================
# def update_grade(name, subject, new_grade):
#     """
#     Update a specific grade for a student.
    
#     OBJECT IDENTITY:
#     - students[name] returns a REFERENCE to the inner dict (same object, same id()).
#     - When we do students[name][subject] = new_grade, we are modifying that
#       object at its memory location. No new dict is created.
#     - This is why updates are O(1) and efficient.
    
#     ERROR HANDLING:
#     - If the student doesn't exist, we raise KeyError (dict behavior).
#     - If the subject doesn't exist, we create it (dict is mutable, allows new keys).
    
#     TIME COMPLEXITY: O(1)
#     - Dictionary key access and insertion are constant time on average.
#     """
#     if name not in students:
#         raise KeyError(f"Student '{name}' not found in the system.")
    
#     students[name][subject] = new_grade
#     print(f"Updated {name}'s {subject} grade to {new_grade}")


# # ============================================================================
# # FUNCTION 3: Calculate average grade for a student
# # ============================================================================
# def calculate_average(name):
#     """
#     Calculate the average grade for a student.
    
#     REFERENCES AND ITERATION:
#     - students[name] returns a reference to the inner dict.
#     - When we iterate with for subject, grade in students[name].items(),
#       'grade' is the actual integer value, not a reference (ints are immutable).
#     - The sum() function iterates over the grades and adds them. Each iteration
#       accesses the dict value through the reference.
    
#     TIME COMPLEXITY: O(m)
#     - m = number of subjects for this student.
#     - We must iterate through all subjects to compute the average.
#     - No way to do this faster (we need to see all values).
    
#     SPACE COMPLEXITY: O(1)
#     - We only use constant extra space (the sum variable, count, average).
#     """
#     if name not in students:
#         raise KeyError(f"Student '{name}' not found in the system.")
    
#     grades_dict = students[name]  # Reference to the inner dict
    
#     if not grades_dict:
#         return 0
    
#     # Sum the values in the dict. dict.values() returns a view object (lazy, O(1) to create).
#     total = sum(grades_dict.values())
#     count = len(grades_dict)  # O(1): dict maintains length, not computed
#     average = total / count
    
#     return average


# # ============================================================================
# # FUNCTION 4: Get class average
# # ============================================================================
# def get_class_average():
#     """
#     Calculate the average grade across all students.
    
#     NESTED ITERATION AND REFERENCES:
#     - Outer loop: for name in students iterates through keys.
#     - Inner loop: for grade in students[name].values() iterates through grades.
#     - students[name] is always the same inner dict object (reference).
#     - We iterate through all values in all dicts to compute the class average.
    
#     TIME COMPLEXITY: O(n * m)
#     - n = number of students
#     - m = average number of subjects per student
#     - We must access every grade in the entire system.
    
#     SPACE COMPLEXITY: O(1)
#     - We use only constant extra space (sum, count, average).
#     """
#     if not students:
#         return 0
    
#     all_grades = []
    
#     # Outer loop iterates through student keys
#     for name in students:
#         # Inner reference to the grades dict
#         grades_dict = students[name]
        
#         # Iterate through the values in this dict
#         for grade in grades_dict.values():
#             all_grades.append(grade)
    
#     if not all_grades:
#         return 0
    
#     return sum(all_grades) / len(all_grades)


# # ============================================================================
# # FUNCTION 5: View all grades
# # ============================================================================
# def view_all_grades():
#     """
#     Display all students and their grades.
    
#     DICTIONARY UNPACKING AND MUTABILITY SAFETY:
#     - We use a loop to display data without modifying the original dicts.
#     - Dictionaries are mutable, but we're only reading here, so the data is safe.
#     - If we wanted to prevent accidental modification, we could use deepcopy(),
#       but that's O(n * m) time and defeats the purpose of using efficient dicts.
    
#     TIME COMPLEXITY: O(n * m)
#     - We must iterate through all students and all their grades to display them.
#     """
#     print("\n" + "="*60)
#     print("ALL STUDENTS AND GRADES")
#     print("="*60)
    
#     for name in students:
#         grades_dict = students[name]  # Reference to inner dict
#         print(f"\n{name}:")
#         for subject, grade in grades_dict.items():
#             print(f"  {subject}: {grade}")


# # ============================================================================
# # FUNCTION 6: Remove a student
# # ============================================================================
# def remove_student(name):
#     """
#     Remove a student from the system.
    
#     OBJECT DELETION:
#     - del students[name] removes the KEY from the outer dict.
#     - This breaks the reference from the dict to the inner grades dict.
#     - The inner dict object will be garbage collected (no more references).
#     - In CPython, when refcount reaches 0, the object is freed immediately.
    
#     TIME COMPLEXITY: O(1)
#     - Dictionary deletion is constant time on average.
    
#     MEMORY BEHAVIOR:
#     - Before deletion: students["Alice"] points to a dict object with refcount >= 1
#     - After deletion: if no other variables reference it, refcount becomes 0 and
#     the object is destroyed. Memory is freed.
#     """
#     if name not in students:
#         raise KeyError(f"Student '{name}' not found in the system.")
    
#     del students[name]
#     print(f"Removed {name} from the system.")


# # ============================================================================
# # FUNCTION 7: Get top performers
# # ============================================================================
# def get_top_performers(threshold=90):
#     """
#     Get students with average grade above a threshold.
    
#     FILTERING WITH DICTIONARY COMPREHENSION (CONCEPTUAL):
#     - We loop through students and calculate averages.
#     - This combines O(n) iteration with O(m) average calculation = O(n * m).
#     - We filter results, which doesn't add asymptotic complexity.
    
#     TIME COMPLEXITY: O(n * m)
#     - n = number of students
#     - m = average number of subjects
#     - We calculate average for each student, which requires iterating through subjects.
    
#     SPACE COMPLEXITY: O(k)
#     - k = number of top performers (subset of n)
#     - We return a new list, so extra space is proportional to result size.
#     """
#     top_performers = []
    
#     for name in students:
#         avg = calculate_average(name)
#         if avg >= threshold:
#             top_performers.append((name, avg))
    
#     # Sort by average (descending)
#     top_performers.sort(key=lambda x: x[1], reverse=True)
    
#     return top_performers


# # ============================================================================
# # MAIN EXECUTION: Demonstrating the System
# # ============================================================================

# if __name__ == "__main__":
#     print("="*60)
#     print("DICTIONARY-BASED STUDENT GRADING SYSTEM")
#     print("="*60)
    
#     # Display initial data
#     view_all_grades()
    
#     # Update a grade (mutates the inner dict in-place)
#     print("\n--- Updating Alice's Math Grade ---")
#     update_grade("Alice", "math", 98)
    
#     # Calculate individual average
#     print(f"\nAlice's Average: {calculate_average('Alice'):.2f}")
#     print(f"Bob's Average: {calculate_average('Bob'):.2f}")
#     print(f"Charlie's Average: {calculate_average('Charlie'):.2f}")
    
#     # Calculate class average
#     print(f"\nClass Average: {get_class_average():.2f}")
    
#     # Add a new student
#     print("\n--- Adding New Student ---")
#     add_student("Diana", {"math": 96, "english": 94, "science": 92})
    
#     # Get top performers
#     print("\n--- Top Performers (90+) ---")
#     top = get_top_performers(90)
#     for name, avg in top:
#         print(f"  {name}: {avg:.2f}")
    
#     # Display all grades after modifications
#     view_all_grades()
    
#     # Remove a student
#     print("\n--- Removing Charlie ---")
#     remove_student("Charlie")
    
#     # Final class average
#     print(f"\nFinal Class Average: {get_class_average():.2f}")
    
#     print("\n" + "="*60)
#     print("EXECUTION COMPLETE")
#     print("="*60)


# Day 2: Variables and Memory Basics
#     - Build: Dictionary-based Student Grading System.
#     - Defend: Narrative comments explaining references vs. values, object identity, and mutability.

# features
# {
#     student_name {
#         "subject" : grade
#     }
# }

# storage, input, math, retrieval

record_book: dict[str, Any] = {
    "Ore" : {"math": 44, "english": 44, "physics": 44, "chemistry": 44, "biology": 44},
    "Daniel" : {"math": 44, "english": 44, "physics": 44, "chemistry": 44, "biology": 44},
    "Rapheal" : {"math": 44, "english": 44, "physics": 44, "chemistry": 44, "biology": 44}
}


def add_student(target_dict):
    
    student_name = input("What is the name of this student of yours? ")
    student_math_score = input(f"What did {student_name} score in Mathematics ")
    student_english_score = input(f"What did {student_name} score in English ")
    student_physics_score = input(f"What did {student_name} score in Physics ")
    student_chemistry_score = input(f"What did {student_name} score in Chemistry ")
    student_biology_score = input(f"What did {student_name} score in Biology ")
    
    


    target_dict[student_name] = {
        "math": student_math_score,
        "english": student_english_score,
        "physics": student_physics_score,
        "chemistry": student_chemistry_score,
        "biology": student_biology_score,
    }
    
    print(f"Internal Check: {target_dict}")
    return target_dict
    
add_student(record_book)
print(record_book)

# def main():
#     pass

#     while True:
#         pass

