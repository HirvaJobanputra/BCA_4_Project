import os
from colorama import Fore, Style, Back
from data_io import load_books_from_file, save_books_to_file
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel('Gemini 2.0 Flash')


class Book:
    def __init__(self, name, author, copies):
        self.name = name
        self.author = author
        self.available_copies = copies
        self.bookID = None

    def __str__(self):
        return f"Book ID: {self.bookID}, Name: {self.name}, Author: {self.author}, Copies Available: {self.available_copies}"

class Library:
    def __init__(self):
        self.books = load_books_from_file()
        if not self.books:
            self.books = [
                {"Name": "Mahabharat", "Author": "VedVyas", "available_copies": 5, "bookID": 101},
                {"Name": "Ikigai", "Author": "Francesc Miralles Hector Garcia", "available_copies": 3, "bookID": 102},
                {"Name": "Good Vibes Good Life", "Author": "King Vex", "available_copies": 2, "bookID": 103},
                {"Name": "Rework", "Author": "Fried Jason", "available_copies": 4, "bookID": 104},
                {"Name": "The Go Getter", "Author": "Kyne Peter", "available_copies": 1, "bookID": 105}
            ]
            self.next_book_id = 106
        else:
            self.next_book_id = max(book['bookID'] for book in self.books) + 1

    def add_book(self, book):
        book.bookID = self.next_book_id
        self.books.append({"Name": book.name, "Author": book.author, "available_copies": book.available_copies, "bookID": book.bookID})
        self.next_book_id += 1
        print(Fore.GREEN + f"The book named {book.name} has been added to the library with ID {book.bookID}" + Style.RESET_ALL)
        return True

    def display_books(self):
        for book in self.books:
            print(Fore.YELLOW + f"Book ID: {book['bookID']} | Name: {book['Name']} | Author: {book['Author']} | Copies Available: {book['available_copies']}")

    def search_book(self):
        if not self.books:
            print(Fore.RED + "No books available in the library" + Style.RESET_ALL)
            return

        book_name = input("Enter the name of the book you want to search: ")
        for book in self.books:
            if book['Name'] == book_name:
                # Generate and display the summary
                summary = self.get_book_summary(book['Name'], book['Author']) 
                print(Back.WHITE + Fore.MAGENTA + f"Book ID: {book['bookID']} | Name: {book['Name']} | Author: {book['Author']} | Copies Available: {book['available_copies']}")
                print(Fore.GREEN + "Summary:" + Style.RESET_ALL)
                print(summary)
                return

        print(Fore.RED + "Book not found in the library" + Style.RESET_ALL)

    def get_book_summary(self, title, author):
        """Generates a short summary of a book using the Gemini API."""
        prompt = f"Summarize the book {title} by {author} in 3 sentences."
        try:
            response = genai.GenerativeModel('gemini-2.0-flash-exp').generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating summary: {e}"

    def borrow_book(self, book_name):
        for book in self.books:
            if book['Name'] == book_name:
                if book['available_copies'] > 0:
                    book['available_copies'] -= 1
                    save_books_to_file(self.books)
                    return book
                else:
                    print(Fore.RED + f"Book '{book_name}' is currently unavailable." + Style.RESET_ALL)
                    return None
        print(Fore.RED + "Book not found in the library." + Style.RESET_ALL)
        return None

    def return_book(self, book_name):
        for book in self.books:
            if book['Name'] == book_name:
                book['available_copies'] += 1
                save_books_to_file(self.books)
                print(Fore.GREEN + f"Book '{book_name}' returned." + Style.RESET_ALL)
                return
        print(Fore.RED + "Book not found in the library." + Style.RESET_ALL)

    def remove_book(self, book_id):
        initial_length = len(self.books)
        self.books = [book for book in self.books if book['bookID'] != book_id]
        if len(self.books) < initial_length:
            save_books_to_file(self.books)
            print(Fore.RED + f"Book with ID {book_id} removed." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Book with ID {book_id} not found." + Style.RESET_ALL)

    def get_history(self, member_id):
        pass
        