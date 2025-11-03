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
        
        # 1. Get ONLY this member's book transactions (must have 4 fields)
        member_book_history = [
            record for record in transactions 
            if record[0] == mID and len(record) == 4
        ]

        if not member_book_history:
            print(Fore.YELLOW + "📭 You have not borrowed any books yet.")
            return

        # 2. This dictionary will store the FINAL status of each book.
        #    Key: BookID, Value: [Action, Date]
        book_status = {}

        # 3. Loop through all transactions...
        for record in member_book_history:
            book_id = record[1]
            action = record[2]
            date = record[3]
            
            # 4. This line is the magic! It automatically overwrites
            #    the 'Borrowed' status if a 'Returned' one appears later.
            book_status[book_id] = [action, date]

        # 5. Now, print the final status list
        print(Fore.CYAN + Style.BRIGHT + "📕 Your Book Status:")
        
        currently_borrowed_count = 0
        
        for book_id, status in book_status.items():
            action = status[0]
            date = status[1]
            
            if action == "Borrowed":
                # It's currently borrowed! Print in bright white.
                print(Fore.WHITE + Style.BRIGHT + f"  Book ID: {book_id} | Status: {action} | Date: {date}")
                currently_borrowed_count += 1
            else:
                # It's returned. Print in a dimmer (cyan) color.
                print(Fore.CYAN + f"  Book ID: {book_id} | Status: {action} | Date: {date}")

        # Add a helpful summary at the end
        if currently_borrowed_count == 0:
            print(Fore.GREEN + "\n✅ You have no books currently checked out.")
        else:
            print(Fore.YELLOW + f"\n🔔 You have {currently_borrowed_count} book(s) currently checked out.")

            
    @staticmethod
    def viewHistory(mID):
        transactions = Transaction.loadHistory()
        member_history = [record for record in transactions if record[0] == mID]

        if not member_history:
            print(Fore.YELLOW + "📭 No history found for this member.")
            return

        print(Fore.CYAN + Style.BRIGHT + "🕓 Member History:")
        for record in member_history:
            if len(record) == 4:
                # For Borrow/Return records: [MemberID, BookID, Action, Date]
                print(Fore.BLUE + f"Book ID: {record[1]} | Action: {record[2]} | Date: {record[3]}")
            elif len(record) == 3:
                # For Member creation/removal records: [MemberID, Action, Date]
                print(Fore.BLUE + f"Action: {record[1]} | Date: {record[2]}")
            else:
                print(Fore.RED + "❌ Corrupted history record found.")

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
