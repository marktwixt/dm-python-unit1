### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
def book_parser(book):
    title = book['title']
    author = book['author']
    year = book['year']
    rating = book['rating']
    pages = book['pages']

    info = f"'{title}' by {author} was published in {year}. It has {pages} pages and a rating of {rating}."
    return info

# def add_book(books):
#     title = input("Enter the book's title: ")
#     author = input("Enter the author's name: ")
#     year = (input("Enter the publication year: "))
#     rating = (input("Enter the book's rating (0-5): "))
#     pages = (input("Enter the number of pages: "))

#     book = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     books.append(book)
#     print(f"\nBook '{title}' has been added to the library.\n")


# # Example usage:
# books = []

# # Add a book using the function
# add_book(books)

# # Print the updated list of books
# print("Updated book list:")
# for book in books:
#     print(book_parser(book))

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
def add_book(books):
    title = input("Enter the book's title: ")
    author = input("Enter the author's name: ")
    year = int(input("Enter the publication year: "))
    rating = float(input("Enter the book's rating (0-5): "))
    pages = int(input("Enter the number of pages: "))

    book = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    books.append(book)
    print(f"\nBook '{title}' has been added to the library.\n")


# Example usage:
books = []

# Add a book using the function
add_book(books)

# Print the updated list of books
print("Updated book list:")
for book in books:
    print(book_parser(book))


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
def add_book(books):
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
    print(f"\nBook '{title}' has been added to the library.\n")


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def main_menu():
    books = []

    while True:
        print("\nLibrary Main Menu")
        print("1. Add a book")
        print("2. List all books")
        print("3. Exit")

        choice = input("\nPlease choose an option (1-3): ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            list_books(books)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose an option between 1 and 3.")

def list_books(books):
    if not books:
        print("\nThere are no books in the library.\n")
    else:
        print("\nList of books in the library:")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - Rating: {book['rating']}/5 - Pages: {book['pages']}")

if __name__ == "__main__":
    main_menu()

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
def main_menu():
    books = []

    while True:
        print("\nLibrary Main Menu")
        print("1. Add a book")
        print("2. List all books")
        print("3. Exit")

        choice = input("\nPlease choose an option (1-3): ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            list_books(books)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please choose a number between 1 and 3.")

def list_books(books):
    if not books:
        print("\nThere are no books in the library.\n")
    else:
        print("\nList of books in the library:")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - Rating: {book['rating']}/5 - Pages: {book['pages']}")

if __name__ == "__main__":
    main_menu()
