import os
from pathlib import Path
import csv
import sys


question_content = """# metadata
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

# Function to load LOs and K-levels from a csv file
def load_learning_objectives(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # Ensure row has the expected number of columns
                if len(row) == 2:
                    lo, k_level = row
                    # Strip extra whitespace from each element
                    data.append((lo.strip(), k_level.strip()))
                else:
                    print(f"Warning: Skipping invalid row: {row}")
    except Exception as e:
        print(f"Error: Failed to load learning objectives from '{file_path}'. Reason: {e}")
        sys.exit(1)
    return data

# Function to determine points and handle warnings for unexpected K-levels
def get_points_and_warn(lo, k_level):
    points_map = {"K1": 1, "K2": 1, "K3": 2, "K4": 3, "K5": 3, "K6": 3}
    points = points_map.get(k_level, 0)
    if points == 0:
        print(
            f"Warning: Unexpected K-level '{k_level}' for LO '{lo}'. Defaulting to 0 points.")
    return points


# Function to generate the content of the Markdown file
def generate_md_questions(lo, k_level):
    # Get points and handle warnings
    points = get_points_and_warn(lo, k_level)
    return question_content.format(lo=lo, k_level=k_level, points=points)
    
# Main script
if __name__ == "__main__":
    # Check for help flag
    if "--help" in sys.argv or "-h" in sys.argv:
        print("""
Usage: python generate_questions.py <prefix> [file_path]

Description:
  This script generates Markdown question files for learning objectives (LOs) with a specified prefix.

Arguments:
  <code>         A unique code for the ISTQB module (e.g.: tae) used for the questions file names.
                 This prefix is added to the filenames to prevent overwriting.
  [file_path]    (Optional) Path to the source CSV file. Defaults to 'learning-objectives.csv'.

Examples:
  python generate_questions.py CTFL
  python generate_questions.py CTFL-AT custom-objectives.csv
        """)
        sys.exit(0)

    # Check for required arguments
    if len(sys.argv) < 2:
        print("Error: Missing required argument "code". Run with --help for usage details.")
        sys.exit(1)

    # Get the prefix from the command-line arguments
    prefix = sys.argv[1]
    # Optional: Path to the input CSV file, default to 'learning-objectives.csv'
    file_path = sys.argv[2] if len(sys.argv) > 2 else "learning-objectives.csv"

    # Load the LOs and K-levels from the file
    try:
        data = load_learning_objectives(file_path)
    except Exception as e:
        print(f"Error: Failed to load learning objectives from '{file_path}'. Reason: {e}")
        sys.exit(1)

    # Set the output directory to 'libs'
    output_dir = Path("./../sample-exam/")

    # Ensure the 'libs' directory exists (if it doesn't, create it)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Iterate over the data list and generate files for each LO
    for lo, k_level in data:
        # Generate a filename with the prefix
        filename = f"question-{prefix}-{lo.replace(' ', '_')}.md"
        # Combine the output directory path with the filename
        filepath = output_dir / filename
        # Write the generated content to the file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(generate_md_questions(lo, k_level))

    # Print a summary message to confirm generation
    print(f"Generated {len(data)} files in the '{output_dir}' directory.")