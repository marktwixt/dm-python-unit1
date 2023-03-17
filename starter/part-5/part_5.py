### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def add_book(books, filename="library.txt"):
    title = input("Enter the book's title: ")
    author = input("Enter the author's name: ")

    # Input validation for year
    while True:
        try:
            year = int(input("Enter the publication year: "))
            break
        except ValueError:
            print("Please enter a valid integer for the publication year.")

    # Input validation for rating
    while True:
        try:
            rating = float(input("Enter the book's rating (0-5): "))
            if 0 <= rating <= 5:
                break
            else:
                print("Please enter a rating between 0 and 5.")
        except ValueError:
            print("Please enter a valid number for the rating.")

    # Input validation for pages
    while True:
        try:
            pages = int(input("Enter the number of pages: "))
            break
        except ValueError:
            print("Please enter a valid integer for the number of pages.")

    book = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    books.append(book)

    # Create a properly formatted string for the book
    book_string = f"{title},{author},{year},{rating},{pages}\n"

    # Write the book_string to the file
    with open(filename, "a") as file:
        file.write(book_string)

    print(f"\nBook '{title}' has been added to the library.\n")

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def list_books(filename="library.txt"):
    try:
        with open(filename, "r") as file:
            book_lines = file.readlines()

        if not book_lines:
            print("\nThere are no books in the library.\n")
        else:
            print("\nList of books in the library:")
            for index, book_line in enumerate(book_lines, start=1):
                title, author, year, rating, pages = book_line.strip().split(',')
                print(f"{index}. {title} by {author} ({year}) - Rating: {rating}/5 - Pages: {pages}")
    except FileNotFoundError:
        print(f"\nFile '{filename}' not found. No books to display.\n")

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script
def main_menu():
    while True:
        print("\nLibrary Main Menu")
        print("1. Add a book")
        print("2. List all books")
        print("3. Exit")

        choice = input("\nPlease choose an option (1-3): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose a number between 1 and 3.")

if __name__ == "__main__":
    main_menu()

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
## Full Code for Home Library App (added to new file in directory as well):
def load_books(filename="library.txt"):
    books = []

    try:
        with open(filename, "r") as file:
            book_lines = file.readlines()

        for book_line in book_lines:
            title, author, year, rating, pages = book_line.strip().split(',')
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            }
            books.append(book)
    except FileNotFoundError:
        print(f"\nFile '{filename}' not found. No books to display.\n")

    return books


def list_books(filename="library.txt"):
    books = load_books(filename)

    if not books:
        print("\nThere are no books in the library.\n")
    else:
        print("\nList of books in the library:")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - Rating: {book['rating']}/5 - Pages: {book['pages']}")


def total_pages(filename="library.txt"):
    books = load_books(filename)
    total = sum(book["pages"] for book in books)
    print(f"\nThe total number of pages in the library is {total}.\n")


def average_rating(filename="library.txt"):
    books = load_books(filename)

    if not books:
        print("\nThere are no books in the library to calculate an average rating.\n")
    else:
        avg_rating = sum(book["rating"] for book in books) / len(books)
        print(f"\nThe average rating of books in the library is {avg_rating:.2f}/5.\n")


def search_books(filename="library.txt"):
    query = input("Enter a search term (title or author): ").lower()
    books = load_books(filename)
    results = [book for book in books if query in book["title"].lower() or query in book["author"].lower()]

    if not results:
        print(f"\nNo books found matching '{query}'.\n")
    else:
        print("\nSearch results:")
        for index, book in enumerate(results, start=1):
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - Rating: {book['rating']}/5 - Pages: {book['pages']}")


def main_menu():
    while True:
        print("\nLibrary Main Menu")
        print("1. Add a book")
        print("2. List all books")
        print("3. Total pages")
        print("4. Average rating")
        print("5. Search books")
        print("6. Exit")

        choice = input("\nPlease choose an option (1-6): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            list_books()
        elif choice == '3':
            total_pages()
        elif choice == '4':
            average_rating()
        elif choice == '5':
            search_books()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()





