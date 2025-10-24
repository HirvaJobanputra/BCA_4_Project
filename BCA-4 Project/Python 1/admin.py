from colorama import Fore, Style
from datetime import datetime
from util import Book, Member, Transaction, generateMemberID, generateBookID

class Admin:
    def __init__(self, adminID):
        self.adminID = adminID

    def addMember(self, name, email, passowrd):
        members = Member.loadMembers()
        nextID = generateMemberID(members)
        members.append([nextID, name,passowrd, email])
        Member.saveMembers(members)
        history = Transaction.loadHistory()
        history.append([nextID, "New Member", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        Transaction.saveHistory(history)
        print(Fore.GREEN + f"✅ Member '{name}' added successfully with ID {nextID}!")

    def removeMember(self, memberID):
        members = Member.loadMembers()
        members = [member for member in members if member[0] != memberID]
        Member.saveMembers(members)
        history = Transaction.loadHistory()
        history.append([memberID, "Removed Member", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        Transaction.saveHistory(history)
        print(Fore.RED + f"🗑️ Member with ID {memberID} has been removed.")

    def viewMembers(self):
        members = Member.loadMembers()
        if not members:
            print(Fore.YELLOW + "⚠️ No members found.")
        else:
            print(Fore.CYAN + Style.BRIGHT + "📋 Members List:")
            for member in members:
                print(Fore.WHITE + f"ID: {member[0]}, Name: {member[1]}, Email: {member[2]}")

    def searchMembers(self, searchTerm):
        members = Member.loadMembers()
        found_members = [member for member in members if searchTerm.lower() in member[0].lower() or searchTerm.lower() in member[1].lower()]
        if not found_members:
            print(Fore.YELLOW + "🔍 No members found.")
        else:
            print(Fore.CYAN + Style.BRIGHT + "🔍 Found Members:")
            for member in found_members:
                print(Fore.WHITE + f"ID: {member[0]}, Name: {member[1]}, Email: {member[2]}")

    def addBook(self, title, author, genre, copies):
        books = Book.loadBooks()
        nextID = generateBookID(books)
        books.append([nextID, title, author, genre, copies])
        Book.saveBooks(books)
        history = Transaction.loadHistory()
        history.append([nextID, "New Book", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        Transaction.saveHistory(history)
        print(Fore.GREEN + f"📚 Book '{title}' added successfully with ID {nextID}!")

    def removeBook(self, bookID):
        books = Book.loadBooks()
        books = [book for book in books if book[0] != bookID]
        Book.saveBooks(books)
        history = Transaction.loadHistory()
        history.append([bookID, "Removed the Book", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        Transaction.saveHistory(history)
        print(Fore.RED + f"❌ Book with ID {bookID} has been removed.")

    def viewBooks(self):
        books = Book.loadBooks()
        if not books:
            print(Fore.YELLOW + "⚠️ No books found.")
        else:
            print(Fore.CYAN + Style.BRIGHT + "📚 Books List:")
            for book in books:
                if len(book)<4:
                    print(Fore.RED + "❌ Error: Book data is incomplete.")
                    continue
                print(Fore.WHITE + f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}")

    def searchBooks(self, searchTerm):
        books = Book.loadBooks()
        found_books = [book for book in books if len(book) >= 2 and (searchTerm.lower() in book[0].lower() or searchTerm.lower() in book[1].lower())]
        if not found_books:
            print(Fore.YELLOW + "🔍 No books found.")
        else:
            print(Fore.CYAN + Style.BRIGHT + "🔍 Found Books:")
            for book in found_books:
                print(Fore.WHITE + f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}")

    def viewHistory(self):
        history = Transaction.loadHistory()
        if not history:
            print(Fore.YELLOW + "📭 No transaction history found.")
        else:
            print(Fore.MAGENTA + Style.BRIGHT + "📖 Transaction History:")
            for transaction in history:
                print(Fore.WHITE + f"The object: {transaction[0]}, What happened?: {transaction[1]}, Date: {transaction[2]}")

