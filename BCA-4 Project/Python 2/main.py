from colorama import Fore, Style, init, Back
from admin import Admin
from members import Member

init(autoreset=True)

def adminTasks(admin):
    while True:
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "------------- Admin Tasks 🛠️ -------------")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "1. Add a new member 👤") 
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "2. Remove a member 🗑️")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "3. View all members 📋")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "4. Search for members 🔍")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "5. Add a new book 📕")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "6. Remove a book ❌")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "7. View all books 📚")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "8. Search for books 🔍")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "9. View library history 📖")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "10. Exit 🚪")

        task = input(Fore.YELLOW + Style.BRIGHT + "Enter the task number: ")

        if task == "1":
            name = input(Fore.CYAN + "Enter the member's name: ")
            email = input(Fore.CYAN + "Enter the member's email: ")
            password = input(Fore.CYAN + "Let the member enter the password: ")
            admin.addMember(name, email, password)
        elif task == "2":
            memberID = input(Fore.CYAN + "Enter the member's ID: ")
            admin.removeMember(memberID)
        elif task == "3":
            admin.viewMembers()
        elif task == "4":
            searchTerm = input(Fore.CYAN + "Enter the member id or name: ")
            admin.searchMembers(searchTerm)
        elif task == "5":
            title = input(Fore.CYAN + "Enter the book's title: ")
            author = input(Fore.CYAN + "Enter the book's author: ")
            genre = input(Fore.CYAN + "Enter the book's genre: ")
            copies = input(Fore.CYAN + "Enter the number of copies: ")
            admin.addBook(title, author, genre, copies)
        elif task == "6":
            bookID = input(Fore.CYAN + "Enter the book's ID: ")
            admin.removeBook(bookID)
        elif task == "7":
            admin.viewBooks()
        elif task == "8":
            searchTerm = input(Fore.CYAN + "Enter the book id or title: ")
            admin.searchBooks(searchTerm)
        elif task == "9":
            admin.viewHistory()
        elif task == "10":
            print(Fore.MAGENTA + "Thank you for using the library. Goodbye! 👋")
            exit()
        else:
            print(Fore.RED + "Invalid task number ❌")


def memberTasks(mID):
    member = Member()
    while True:
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "------------- Member Tasks 📖 -------------")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "1. View all books 📚")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "2. Search for books 🔍")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "3. Borrow a book 📥")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "4. Return a book 📤")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "5. View borrowed books 📕")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "6. See your history 🕓")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "7. Get a book summary 📑")
        print(Fore.BLUE + Style.BRIGHT + Back.WHITE + "8. Exit 🚪")

        task = input(Fore.YELLOW + Style.BRIGHT + "Enter the task number: ")

        if task == "1":
            member.viewBooks()
        elif task == "2":
            searchTerm = input(Fore.CYAN + "Enter the book id or title: ")
            member.searchBooks(searchTerm)
        elif task == "3":
            bookName = input(Fore.CYAN + "Enter the book's name: ")
            member.borrowBook(mID, bookName)
        elif task == "4":
            bookID = input(Fore.CYAN + "Enter the book's ID: ")
            member.returnBook(mID, bookID)
        elif task == "5":
            member.viewBorrowedBooks(mID)
        elif task == "6":
            member.viewHistory(mID)
        elif task == "7":
            bookID = input(Fore.CYAN + "Enter the book ID: ")
            summary = member.getBookSummary(bookID)
            print(Fore.GREEN + Style.BRIGHT + "📘 Book Summary:")
            print(Fore.CYAN + summary)
        elif task == "8":
            print(Fore.MAGENTA + "Thank you for using the library. Goodbye! 👋")
            exit()
        else:
            print(Fore.RED + "Invalid task number ❌")


# ---------- MAIN PROGRAM STARTS ----------
print(Fore.CYAN + Style.BRIGHT + "-------------📚 Welcome to the Library System 📚-------------")

role = input(Fore.YELLOW + "Are you a member or the administrator? (m/a): ")

if role.lower() == "m":
    mID = input(Fore.YELLOW + "Enter your ID: ")
    mPassword = input(Fore.YELLOW + "Enter your password: ")
    try:
        with open("members.txt", "r") as f:
            members = f.readlines()
            logged_in = False
            for member in members:
                fields = member.strip().split("|")  
                if len(fields) >= 3 and mID == fields[0] and mPassword == fields[2]:
                    print(Fore.GREEN + "🔓 You are now logged in as a member.")
                    memberTasks(mID)
                    logged_in = True
                    break
            if not logged_in:
                print(Fore.RED + "❌ ID or password is incorrect.")
    except FileNotFoundError:
        print(Fore.RED + "❌ The members file does not exist.")
        exit()

elif role.lower() == "a":
    aID = input(Fore.YELLOW + "Enter your ID: ")
    aPassword = input(Fore.YELLOW + "Enter your password: ")
    try:
        with open("admins.txt", "r") as f:
            admins = f.readlines()
            logged_in = False
            for admin_entry in admins:
                fields = admin_entry.strip().split("|")
                if len(fields) >= 3 and aID == fields[0] and aPassword == fields[2]:
                    print(Fore.GREEN + "🔓 You are now logged in as an administrator.")
                    admin = Admin(aID)
                    adminTasks(admin)
                    logged_in = True
                    break

            if not logged_in:
                print(Fore.RED + "❌ ID or password is incorrect.")
    except FileNotFoundError:
        print(Fore.RED + "❌ Error loading the admin file.")
        exit()
else:
    print(Fore.RED + "❌ Invalid role entered. Please restart and choose 'm' or 'a'.")
