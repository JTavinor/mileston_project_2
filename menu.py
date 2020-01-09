import app

def menu():
    while True:
        user_input = input(f"""Do you want to?:
View your library? (v);
Search your library? (s);
Add a book to your library? (a);
Mark a book in your library as read? (r);
Delete a book from your library? (d);
Add a new library? (n);
Or exit the app? (q): """)
        if user_input == 'v':
            app.view_books()
        if user_input == 's':
            print()
            app.search_books()
        if user_input == 'a':
            app.add_book()
        if user_input == 'r':
            app.read_book()
        if user_input == 'd':
            app.delete_book()
        if user_input == 'n':
            app.add_library()
        if user_input == 'q':
            print('Goodbye!')
            break


menu()
