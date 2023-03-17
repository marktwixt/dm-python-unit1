my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def book_parser(book):
    title = book['title']
    author = book['author']
    year = book['year']
    rating = book['rating']
    pages = book['pages']

    info = f"'{title}' by {author} was published in {year}. It has {pages} pages and a rating of {rating}."
    return info

book_string = book_parser(my_book)
print(book_string)



# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_title(book):
    return book['title']

def get_author(book):
    return book['author']

def get_year(book):
    return book['year']

def get_rating(book):
    return book['rating']

def get_pages(book):
    return book['pages']

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
def filter_by_author(books, author_name):
    return [book for book in books if book['author'] == author_name]

def filter_by_min_rating(books, min_rating):
    return [book for book in books if book['rating'] >= min_rating]

def filter_by_year_range(books, start_year, end_year):
    return [book for book in books if start_year <= book['year'] <= end_year]

# Test data: list of book dictionaries
books = [
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "year": 2008,
        "rating": 4.32,
        "pages": 374
    },
    {
        "title": "Catching Fire",
        "author": "Suzanne Collins",
        "year": 2009,
        "rating": 4.29,
        "pages": 391
    },
    {
        "title": "Mockingjay",
        "author": "Suzanne Collins",
        "year": 2010,
        "rating": 4.03,
        "pages": 390
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "rating": 4.19,
        "pages": 328
    }
]

# Test the functions with the list of book dictionaries
filtered_by_author = filter_by_author(books, "Suzanne Collins")
filtered_by_min_rating = filter_by_min_rating(books, 4.2)
filtered_by_year_range = filter_by_year_range(books, 2000, 2010)

print("Filtered by author:")
for book in filtered_by_author:
    print(book_parser(book))

print("\nFiltered by minimum rating:")
for book in filtered_by_min_rating:
    print(book_parser(book))

print("\nFiltered by year range:")
for book in filtered_by_year_range:
    print(book_parser(book))