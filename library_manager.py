import json  # Importing JSON module to handle file storage
import shutil  # Importing shutil to create backup files

# File to store library data
LIBRARY_FILE = "library.json"  # Main file for storing book data
BACKUP_FILE = "library_backup.json"  # Backup file in case of errors

# Section: Load Library Functions
def load_library():
    """Load the library from a file."""
    try:
        with open(LIBRARY_FILE, "r") as file:  # Open the file in read mode
            return json.load(file)  # Load and return the JSON data as a list
    except (FileNotFoundError, json.JSONDecodeError):  # Handle errors if file is missing or corrupt
        return []  # Return an empty list if no valid data is found

# Section: Save Library Functions
def save_library(library):
    """Save the library to a file with backup handling."""
    try:
        shutil.copy(LIBRARY_FILE, BACKUP_FILE)  # Create a backup before overwriting
    except FileNotFoundError:
        pass  # No backup needed if file doesn't exist yet
    
    with open(LIBRARY_FILE, "w") as file:  # Open the file in write mode
        json.dump(library, file, indent=4)  # Save the library data in a structured format

# Section: Book Management Functions
def add_book(library):
    """Add a book to the library."""
    title = input("Enter the book title: ")  # Get book title from user
    author = input("Enter the author: ")  # Get author's name
    
    while True:
        try:
            year = int(input("Enter the publication year: "))  # Get publication year as an integer
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a valid year.")  # Handle non-integer input
    
    genre = input("Enter the genre: ")  # Get book genre
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"  # Get read status
    
    library.append({  # Add book details to the library list
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    })
    print("Book added successfully!")
    save_library(library)  # Save the updated library to file

def remove_book(library):
    """Remove a book from the library by title."""
    title = input("Enter the title of the book to remove: ")  # Get book title to remove
    for book in library:
        if book["title"].lower() == title.lower():  # Find the matching book
            library.remove(book)  # Remove the book from the list
            print("Book removed successfully!")
            save_library(library)  # Save the updated library
            return
    print("Book not found!")

def search_book(library):
    """Search for a book by title or author."""
    print("Search by: \n1. Title \n2. Author")
    choice = input("Enter your choice: ")  # Get user choice for search criteria
    query = input("Enter search term: ").strip().lower()  # Get search query and convert to lowercase
    
    results = [book for book in library if query in book["title"].lower() or query in book["author"].lower()]  # Filter books based on query
    
    if results:  # If matching books are found
        for i, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"  # Convert boolean to readable text
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")  # Display book details
    else:
        print("No matching books found.")

# Section: Display Functions
def display_books(library):
    """Display all books in the library."""
    if not library:  # Check if library is empty
        print("Your library is empty.")
        return
    
    print("Your Library:")
    for i, book in enumerate(library, 1):  # Loop through books
        status = "Read" if book["read"] else "Unread"  # Convert read status to text
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")  # Display book details

def display_statistics(library):
    """Display statistics about the library."""
    total_books = len(library)  # Get total number of books
    read_books = sum(1 for book in library if book["read"])  # Count books marked as read
    
    if total_books == 0:  # If no books are in the library
        print("No books in the library.")
        return
    
    read_percentage = (read_books / total_books) * 100  # Calculate percentage of books read
    print(f"Total books: {total_books}")
    print(f"Percentage read: {read_percentage:.2f}%")  # Display percentage with two decimal places

# Section: Main Program Logic
def main():
    """Main function to run the Personal Library Manager."""
    library = load_library()  # Load existing library data from file
    
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        
        choice = input("Enter your choice: ")  # Get user menu selection
        
        if choice == "1":
            add_book(library)  # Call function to add a book
        elif choice == "2":
            remove_book(library)  # Call function to remove a book
        elif choice == "3":
            search_book(library)  # Call function to search for a book
        elif choice == "4":
            display_books(library)  # Call function to display all books
        elif choice == "5":
            display_statistics(library)  # Call function to display statistics
        elif choice == "6":
            save_library(library)  # Save library before exiting
            print("Library saved to file. Goodbye!")
            break  # Exit the loop and terminate program
        else:
            print("Invalid choice, please try again.")  # Handle incorrect input










# Section: Program Entry Point
if __name__ == "__main__":
    main()  # Call main function to start the program