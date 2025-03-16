# Importing JSON module to handle file storage
import json
# Importing shutil to create backup files
import shutil

# File to store library data

# Main file for storing book data
LIBRARY_FILE = "library.json"
# Backup file in case of errors
BACKUP_FILE = "library_backup.json"

# Section: Load Library Functions
def load_library():
    """Load the library from a file."""
    try:
        # Open the file in read mode
        with open(LIBRARY_FILE, "r") as file:
            # Load and return the JSON data as a list
            return json.load(file)
        
    # Handle errors if file is missing or corrupt
    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty list if no valid data is found
        return []

# Section: Save Library Functions
def save_library(library):
    """Save the library to a file with backup handling."""
    try:
        # Create a backup before overwriting
        shutil.copy(LIBRARY_FILE, BACKUP_FILE)
    except FileNotFoundError:
        # No backup needed if file doesn't exist yet
        pass 
    
    # Open the file in write mode
    with open(LIBRARY_FILE, "w") as file:
        # Save the library data in a structured format
        json.dump(library, file, indent=4)

# Section: Book Management Functions
def add_book(library):
    """Add a book to the library."""
    # Get book title from user
    title = input("Enter the book title: ")  
    # Get author's name
    author = input("Enter the author: ") 
    
    while True:
        try:
            # Get publication year as an integer
            year = int(input("Enter the publication year: "))
            # Exit loop if input is valid
            break
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a valid year.")  
    
    # Get book genre
    genre = input("Enter the genre: ")  
    # Get read status
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"  
    
    # Add book details to the library list
    library.append({  
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    })
    print("Book added successfully!")
    # Save the updated library to file
    save_library(library)

def remove_book(library):
    """Remove a book from the library by title."""
    # Get book title to remove
    title = input("Enter the title of the book to remove: ")  
    for book in library:
        # Find the matching book
        if book["title"].lower() == title.lower():  
            # Remove the book from the list
            library.remove(book)  
            print("Book removed successfully!")
            # Save the updated library
            save_library(library)  
            return
    print("Book not found!")

def search_book(library):
    """Search for a book by title or author."""
    print("Search by: \n1. Title \n2. Author")
    # Get user choice for search criteria
    choice = input("Enter your choice: ")  
    # Get search query and convert to lowercase
    query = input("Enter search term: ").strip().lower()  
    
    # Filter books based on query
    results = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]  
    
    # If matching books are found
    if results:  
        for i, book in enumerate(results, 1):
            # Convert boolean to readable text
            status = "Read" if book["read"] else "Unread" 
            # Display book details
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")  
    else:
        print("No matching books found.")

# Section: Display Functions
def display_books(library):
    """Display all books in the library."""
    # Check if library is empty
    if not library:  
        print("Your library is empty.")
        return
    
    print("Your Library:")
    # Loop through books
    for i, book in enumerate(library, 1): 
        # Convert read status to text
        status = "Read" if book["read"] else "Unread" 
        # Display book details
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")  

def display_statistics(library):
    """Display statistics about the library."""
    # Get total number of books
    total_books = len(library)
    # Count books marked as read
    read_books = sum(1 for book in library if book["read"])
    
    # If no books are in the library
    if total_books == 0:  
        print("No books in the library.")
        return
    
    # Calculate percentage of books read
    read_percentage = (read_books / total_books) * 100  
    print(f"Total books: {total_books}")
    # Display percentage with two decimal places
    print(f"Percentage read: {read_percentage:.2f}%")  

# Section: Main Program Logic
def main():
    """Main function to run the Personal Library Manager."""
    # Load existing library data from file
    library = load_library()  
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        # Get user menu selection
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Call function to add a book
            add_book(library)
        elif choice == "2":
            # Call function to remove a book
            remove_book(library)
        elif choice == "3":
            # Call function to search for a book
            search_book(library)
        elif choice == "4":
            # Call function to display all books
            display_books(library)
        elif choice == "5":
            # Call function to display statistics
            display_statistics(library)
        elif choice == "6":
            # Save library before exiting
            save_library(library)
            print("Library saved to file. Goodbye!")
            # Exit the loop and terminate program
            break 
        else:
            # Handle incorrect input
            print("Invalid choice, please try again.")



# Section: Program Entry Point
if __name__ == "__main__":
    # Call main function to start the program
    main()