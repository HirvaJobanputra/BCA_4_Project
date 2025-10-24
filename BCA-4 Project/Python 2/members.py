from datetime import datetime
import os
from colorama import Fore, Style, init
import google.generativeai as genai
from util import Book, Transaction

init(autoreset=True)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class Member:

    @staticmethod
    def viewBooks():
        books = Book.loadBooks()
        try:
            if not books:
                print(Fore.YELLOW + "⚠️ No books available currently.")
            else:
                print(Fore.CYAN + Style.BRIGHT + "📚 Available Books:")
                for book in books:
                    print(Fore.BLUE + f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Genre: {book[3]} | Copies: {book[4]}")
        except FileNotFoundError:
            print(Fore.RED + "❌ Error loading books file.")

    @staticmethod
    def searchBooks(searchTerm):
        books = Book.loadBooks()
        booksFound = []
        for book in books:
            if searchTerm.lower() in "|".join(book).lower():
                booksFound.append(book)

        if not booksFound:
            print(Fore.YELLOW + "🔍 No books found matching your search.")
            return 0
        else:
            print(Fore.CYAN + Style.BRIGHT + "🔍 Search Results:")
            for book in booksFound:
                print(Fore.BLUE + f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Genre: {book[3]} | Copies: {book[4]}")

    @staticmethod
    def borrowBook(mID, bookName):
        booksFound=Member.searchBooks(bookName)
        if booksFound == 0:
            return
            
        bookId = input(Fore.YELLOW + "Enter the Book ID you want to borrow: ").strip()
        books = Book.loadBooks()

        for book in books:
            if book[0] == bookId:
                available = int(book[4])
                if available <= 0:
                    print(Fore.RED + "❌ Sorry, this book is not available for borrowing.")
                    return
                else:
                    book[4] = str(available - 1)
                    break
        else:
            print(Fore.RED + "❌ Book not found.")
            return

        transactions = Transaction.loadHistory()
        transactions.append([mID, bookId, "Borrowed", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        Transaction.saveHistory(transactions)
        Book.saveBooks(books)
        print(Fore.GREEN + "✅ Book borrowed successfully!")

    @staticmethod
    def returnBook(mID, bookID):
        books = Book.loadBooks()
        for book in books:
            if book[0] == bookID:
                available = int(book[4])
                book[4] = str(available + 1)
                break
        else:
            print(Fore.RED + "❌ Book not found.")
            return

        transactions = Transaction.loadHistory()
        transactions.append([mID, bookID, "Returned", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        Transaction.saveHistory(transactions)
        Book.saveBooks(books)
        print(Fore.GREEN + "📥 Book returned successfully!")

    @staticmethod
    def viewBorrowedBooks(mID):
        transactions = Transaction.loadHistory()
        borrowed_books = [record for record in transactions if record[0] == mID and record[2] == "Borrowed"]

        if not borrowed_books:
            print(Fore.YELLOW + "📭 No borrowed books found.")
            return

        print(Fore.CYAN + Style.BRIGHT + "📕 Borrowed Books:")
        for book in borrowed_books:
            print(Fore.BLUE + f"Book ID: {book[1]} | Action: {book[2]} | Date: {book[3]}")

    @staticmethod
    def viewHistory(mID):
        transactions = Transaction.loadHistory()
        member_history = [record for record in transactions if record[0] == mID]

        if not member_history:
            print(Fore.YELLOW + "📭 No history found for this member.")
            return

        print(Fore.CYAN + Style.BRIGHT + "🕓 Member History:")
        for record in member_history:
            print(Fore.BLUE + f"Book ID: {record[1]} | Action: {record[2]} | Date: {record[3]}")

    @staticmethod
    def getBookSummary(bookId):
        books = Book.loadBooks()
        for book in books:
            if book[0] == bookId:
                title = book[1]
                author = book[2]
                break
        else:
            return Fore.RED + "❌ Invalid book ID provided."

        prompt = f"Summarize the book '{title}' by {author} in 3 sentences."

        try:
            response = genai.GenerativeModel('gemini-2.0-flash-exp').generate_content(prompt)
            return response.text
        except Exception as e:
            return Fore.RED + f"❌ Error generating summary: {e}"
