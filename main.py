
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

print("\n" + "="*50)
print("=== LESSON 2: Accessing Cells (Like Excel A1, B1) ===")
print("="*50)

# Our table again:
table = [
    ["Name",  "Age", "City"],     # Row 0 (Header)
    ["John",  25,    "Paris"],    # Row 1
    ["Alice", 30,    "London"],   # Row 2
    ["Bob",   22,    "Tokyo"]     # Row 3
]

print("Our table:")

# Let's break down this loop step by step:
print("\n=== Understanding the Loop (Lines 54-56) ===")
print("for i, row in enumerate(table):")
print("  - 'enumerate' gives us both the position AND the content")
print("  - 'i' = the row number (0, 1, 2, 3...)")
print("  - 'row' = the actual row data ['Name', 'Age', 'City']")
print()

# Here's what happens step by step:
for i, row in enumerate(table):
    print(f"Step {i+1}: i={i}, row={row}")
    print(f"  So we print: Row {i}: {row}")
    print()

print("=== Why use enumerate? ===")
print("Instead of writing:")
print("  print('Row 0:', table[0])")
print("  print('Row 1:', table[1])")
print("  print('Row 2:', table[2])")
print("  print('Row 3:', table[3])")
print()
print("enumerate() does it automatically for ANY size table!")

print("\n=== What each part means: ===")
print("- for = start a loop")
print("- i, row = two variables (position, content)")
print("- enumerate(table) = gives both position and content")
print("- f'Row {i}: {row}' = formats the output nicely")

print("\n=== How to Access Specific Cells ===")
print("In Excel, you click on A1, B2, etc.")
print("In Python, we use [row][column] - both start from 0!")
print()

# Think of it like coordinates: [row][column]
print("table[0][0] =", table[0][0])  # First row, first column = "Name"
print("table[1][0] =", table[1][0])  # Second row, first column = "John"
print("table[1][1] =", table[1][1])  # Second row, second column = 25
print("table[2][2] =", table[2][2])  # Third row, third column = "London"

print("\n=== Excel vs Python Comparison ===")
print("Excel A1 = table[0][0] =", table[0][0])
print("Excel B1 = table[0][1] =", table[0][1])
print("Excel C1 = table[0][2] =", table[0][2])
print("Excel A2 = table[1][0] =", table[1][0])
print("Excel B2 = table[1][1] =", table[1][1])

print("\n=== Remember: ===")
print("- [0] means first (Python starts counting from 0)")
print("- [row][column] - row first, then column")
print("- table[1][2] means: row 1, column 2")
