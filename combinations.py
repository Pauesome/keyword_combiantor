import csv

# Columns from the image
A = ["Word 1.1"]
B = ["Word 2.1", "Word 2.2", "Word 2.3", "Word 2.4", "Word 2.5", "Word 2.6"]
C = ["Word 3.1", "Word 3.2", "Word 3.3", "Word 3.4"]
D = ["Word 4.1", "Word 4.2"]

# Combinations based on the specified rules
combinations = []

# B + C
for b in B:
    for c in C:
        combinations.append([f"{b} {c}"])

# B + D
for b in B:
    for d in D:
        combinations.append([f"{b} {d}"])

# B + C + D
for b in B:
    for c in C:
        for d in D:
            combinations.append([f"{b} {c} {d}"])

# A + B + C + D
for a in A:
    for b in B:
        for c in C:
            for d in D:
                combinations.append([f"{a} {b} {c} {d}"])

# A + B
for a in A:
    for b in B:
        combinations.append([f"{a} {b}"])

# Writing combinations to CSV
with open('combinations.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(combinations)

