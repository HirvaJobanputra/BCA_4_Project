from colorama import Fore, Style, init
init(autoreset=True)

class Book:
    @staticmethod
    def loadBooks(file="books.txt"):
        try:
            with open(file, "r") as f:
                books = f.readlines()
                book_data = [book.strip().split("|") for book in books]
                return book_data
        except FileNotFoundError:
            print(Fore.RED + "❌ Error: The books file does not exist.")
            return []

    @staticmethod
    def saveBooks(books, file="books.txt"):
        try:
            with open(file, "w") as f:
                for book in books:
                    f.write("|".join(book) + "\n")
        except Exception as e:
            print(Fore.RED + f"❌ Error saving books: {e}")


class Member:
    @staticmethod
    def loadMembers(file="members.txt"):
        try:
            with open(file, "r") as f:
                members = f.readlines()
                member_data = [member.strip().split("|") for member in members]
                return member_data
        except FileNotFoundError:
            print(Fore.RED + "❌ Error: The members file does not exist.")
            return []

    @staticmethod
    def saveMembers(members, file="members.txt"):
        try:
            with open(file, "w") as f:
                for member in members:
                    f.write("|".join(member) + "\n")
        except Exception as e:
            print(Fore.RED + f"❌ Error saving members: {e}")


class Transaction:
    @staticmethod
    def loadHistory(file="history.txt"):
        try:
            with open(file, "r") as f:
                history = f.readlines()
                transactions = [transaction.strip().split("|") for transaction in history]
                return transactions
        except FileNotFoundError:
            print(Fore.RED + "📭 Error: The history file does not exist.")
            return []

    @staticmethod
    def saveHistory(history, file="history.txt"):
        try:
            with open(file, "w") as f:
                for transaction in history:
                    f.write("|".join(transaction) + "\n")
        except Exception as e:
            print(Fore.RED + f" Error saving history: {e}")


def generateBookID(books):
    valid_books = [book for book in books if book and book[0].startswith("B") and book[0][1:].isdigit()]
    if not valid_books:
        return "B001"
    else:
        last_id = valid_books[-1][0]
        new_id = int(last_id[1:]) + 1
        return f"B{new_id:03d}"


def generateMemberID(members):
    valid_members = [m for m in members if m and len(m) > 0 and m[0].startswith("M") and m[0][1:].isdigit()]
    if not valid_members:
        return "M001"
    else:
        last_id = valid_members[-1][0]
        new_id = int(last_id[1:]) + 1
        return f"M{new_id:03d}"

