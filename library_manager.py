import json  # Importing JSON module to handle file storage
import shutil  # Importing shutil to create backup files

# File to store library data
LIBRARY_FILE = "library.json"  # Main file for storing book data
BACKUP_FILE = "library_backup.json"  # Backup file in case of errors

# Section: Load and Save Library Functions
def load_library():
    """Load the library from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:  # Open the file in read mode
            return json.load(file)  # Load and return the JSON data as a list
    except (FileNotFoundError, json.JSONDecodeError):  # Handle errors if file is missing or corrupt
        return []  # Return an empty list if no valid data is found

def save_library(library):
    """Save the library to a file with backup handling."""
    try:
        shutil.copy(LIBRARY_FILE, BACKUP_FILE)  # Create a backup before overwriting
    except FileNotFoundError:
        pass  # No backup needed if file doesn't exist yet
    
    with open(LIBRARY_FILE, "w") as file:  # Open the file in write mode
        json.dump(library, file, indent=4)  # Save the library data in a structured format





# Section: Program Entry Point
if __name__ == "__main__":
    main()  # Call main function to start the program