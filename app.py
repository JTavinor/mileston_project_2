import json

file = open(f'books.json', 'r')
books = json.load(file)  # reads the file and turns it into a dictionary
file.close()


def view_books(parameter=books):
    for book in parameter:
        print()
        for key, value in book.items():
            print(f"{key.title()} : {value.title()}")
    print()


def view_name(search_term):
    name_term = input(f'What {search_term} do you want to search for?: ')
    found_books = [book for book in books if book[search_term].lower() == name_term.lower()]

    if found_books:
        print(f'All books in your library with {search_term} {name_term}:')
        view_books(found_books)
    else:
        print(f'No books of {search_term} {name_term} found in your library')
        print()


def view_read():
    read_term = input("Do you want to see books you've read or books you haven't read (y/n)?: ")
    if read_term == 'y':
        found_books = [book for book in books if book['read'] == 'yes']
        view_books(found_books)
    elif read_term == 'n':
        found_books = [book for book in books if book['read'] == 'no']
        view_books(found_books)
    else:
        print(f'{read_term} is not a valid search term')
        print()
        view_read()


def search_books():
    user_input = input('Do you want to search by name, author, or whether you have read the book?: ')
    if user_input == 'name':
        view_name('name')
    elif user_input == 'author':
        view_name('author')
    elif user_input == 'read':
        view_read()
    else:
        print(f'{user_input} is not a valid search term')
        print()
        search_books()


def add_book():
    name = input('What is the books name?: ')
    author = input('Who is the author?: ')
    read = input(f'Have you read {name}? (yes/no):')
    if read != 'yes' and read != 'no':
        print('Input must be yes or no!')
        read = input(f'Have you read {name}? (yes/no):')

    new_entry = {'name': name, 'author': author, 'read': read}

    books.append(new_entry)

    file = open("books.json", "w")
    json.dump(books, file)
    file.close()

    print('This book has been added to your library')
    print()


def read_book():
    read = input('What book have you now read?: ')
    for book in books:
        if read.title() == book['name'].title():
            book['read'] = 'True'

    print(f'{read} set to read')
    print()


def delete_book():
    delete = input('What book do you want to delete from your library?: ')
    book_delete = [book for book in books if book['name'] != delete]
    file = open("books.json", "w")
    json.dump(book_delete, file)
    file.close()

    print(f'{delete} has been deleted from your library!')
