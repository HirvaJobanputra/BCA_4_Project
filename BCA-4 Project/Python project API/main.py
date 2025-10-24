
from colorama import Fore, Style, init, Back
from library import Library, Book
from member import Member
from data_io import save_books_to_file

import google.generativeai as genai

init(autoreset=True)

print(Fore.LIGHTBLUE_EX + "-" * 20 + "Welcome to the library" + "-" * 20)
print(Fore.BLUE + "Menu:")
print(Fore.GREEN + "1. Add a book")
print(Fore.GREEN + "2. Remove a book")
print(Fore.CYAN + "3. Display all books")
print(Fore.CYAN + "4. Search a book")
print(Fore.CYAN + "5. Borrow a book")
print(Fore.CYAN + "6. Return a book")
print(Fore.CYAN + "7. Display borrowed books")
print(Fore.YELLOW + "8. Add Member")
print(Fore.YELLOW + "9. Delete Memeber")
print(Fore.YELLOW + "10.Display Member")
print(Fore.YELLOW + "11.Update Member")
print(Fore.YELLOW + "13. Get history")    
print(Fore.RED + "13. Exit" + Style.RESET_ALL)

library = Library()
member = Member()

while True:
    try:
        option = int(input("Enter your choice: "))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
        continue

    match option:
        case 1:
            name = input("Enter the name of the book: ")
            author = input("Enter the author of the book: ")
            copies = int(input("Enter the number of copies: "))
            book = Book(name, author, copies)
            if library.add_book(book):
                save_books_to_file(library.books)

        case 2:
            book_id = int(input("Enter the book ID to remove: "))
            library.remove_book(book_id)
        case 3:
            library.display_books()

        case 4:
            library.search_book()

        case 5:
            member_id = int(input("Enter Member ID: "))
            member.borrow_book(library, member_id)

        case 6:
            member_id = int(input("Enter Member ID: "))
            member.return_book(library, member_id)

        case 7:
            member_id = int(input("Enter Member ID: "))
            member.display_borrowed_books(member_id)

        case 8:
            name = input("Enter member name: ")
            member.add_member(name)
        case 9:
            member_id = int(input("Enter member ID to delete: "))
            member.delete_member(member_id)
        case 10:
            member.display_members()

        case 11:
            member_id = int(input("Enter member ID to update: "))
            new_name = input("Enter new member name: ")
            member.update_member(member_id, new_name)

        case 12:
            member_id = int(input("Enter member ID to get history: "))
            member.get_history(member_id)
            
        case 13:
            print(Fore.LIGHTBLUE_EX + "-" * 20 + "Exiting the library!!" + "-" * 20 + Style.RESET_ALL)
            save_books_to_file(library.books)
            break
        case _:
            print(Fore.RED + "Invalid choice. Please try entering a valid choice from the menu")