import os
from pathlib import Path

# Function to load LOs and K-levels from a text file
def load_learning_objectives(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                # Split by comma and strip any extra spaces from each part
                lo, k_level = [part.strip() for part in line.split(',')]
                data.append((lo, k_level))
    return data


# Load the LOs and K-levels from the file 'learning-objectives'
file_path = 'learning-objectives'  # Provide the correct path to your file
data = load_learning_objectives(file_path)

# Function to generate the content of the Markdown file
def generate_md_questions(lo, k_level):
    # Assign points based on the K-level using a dictionary
    points_map = {"K1": 1, "K2": 1, "K3": 2, "K4": 3, "K5": 3, "K6": 3}
    # Default to 0 for any unexpected K-level
    points = points_map.get(k_level, 0)
    if points == 0:
        print(
            f"Warning: Unexpected K-level '{k_level}' for LO '{lo}'. Defaulting to 0 points.")
    return f"""# metadata
lo: {lo}
k-level: {k_level}
points: {points}
correct:

## question


## answers
a)
b)
c)
d)

## justification
a)
b)
c)
d)

"""

# Set the output directory to 'libs'
output_dir = Path("libs")

# Ensure the 'libs' directory exists (if it doesn't, create it)
output_dir.mkdir(parents=True, exist_ok=True)

# Delete all files in the 'libs' directory
for file in output_dir.glob('*'):
    file.unlink()

# Iterate over the data list and generate files for each LO
for lo, k_level in data:
    # Generate a filename
    filename = f"question-{lo}.md"
    # Combine the output directory path with the filename
    filepath = os.path.join(output_dir, filename)
    # Write the generated content to the file
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(generate_md_questions(lo, k_level))

# Print a summary message to confirm generation
print(f"Generated {len(data)} files in the '{output_dir}' directory.")
