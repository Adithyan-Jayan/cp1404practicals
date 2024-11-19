"""
CP1404/CP5632 Practical
"""
FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert number of students to an integer
        subjects.append(parts)  # Append the list of parts to the subjects list
    input_file.close()
    return subjects  # Return the list of lists


def display_subject_details(subjects):
    """Display subject details in a formatted manner."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
