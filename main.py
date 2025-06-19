
# LESSON 1: Creating Tables in Python (Excel-like structure)
# =========================================================

print("=== LESSON 1: What is a Table? ===")
print()

# In Excel, you have rows and columns like this:
# |  Name  |  Age  |  City   |
# |  John  |  25   |  Paris  |
# |  Alice |  30   |  London |

# In Python, we create this using "lists inside lists"
# Each inner list [] represents one ROW
# The outer list [] holds all the rows together

# Let's start simple - create one row:
first_row = ["John", 25, "Paris"]
print("One row:", first_row)
print()

# Now let's create a table with multiple rows:
table = [
    ["John", 25, "Paris"],     # Row 1
    ["Alice", 30, "London"]    # Row 2
]

print("Complete table:", table)
print()

# Let's see each row separately:
print("Row 1:", table[0])  # [0] means first row
print("Row 2:", table[1])  # [1] means second row
print()

print("=== Understanding the Structure ===")
print("- Each [] creates a list")
print("- Commas (,) separate items in a row")
print("- Rows are separated by commas too")
print("- The whole thing is wrapped in [] to make it one big list")
