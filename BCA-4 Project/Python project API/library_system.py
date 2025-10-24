from colorama import Fore, Style, init, Back

init(autoreset=True)

from colorama import Fore, Style, init

init(autoreset=True)

def save_member_details(members, filename="members.txt"):
    with open(filename, "w") as file:
        for member in members:
            file.write(f"{member['Member ID: ']} | {member['Member Name: ']}\n")

def save_books_to_file(books, filename="books.txt"):
    with open(filename, "w") as file:
        for book in books:
            file.write(f"{book['bookID']} | {book['Name']} | {book['Author']} | {book['Status']}\n")

def load_members_from_file(filename="members.txt"):
    members = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    values = line.split("|")
                    if len(values) == 2:
                        try:
                            memberID, memberName = values
                            members.append({
                                "Member ID: ": int(memberID),
                                "Member Name: ": memberName
                            })
                        except ValueError:
                            print(Fore.YELLOW + f"Skipping line with invalid member ID: {line}" + Style.RESET_ALL)
                    else:
                        print(Fore.YELLOW + f"Skipping line with incorrect format: {line}" + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.YELLOW + f"File '{filename}' not found. Creating a new file." + Style.RESET_ALL)
    return members

def load_books_from_file(filename="books.txt"):
    books = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    values = line.split("|")
                    if len(values) == 4:
                        try:
                            book_id, name, author, status = values
                            books.append({
                                "bookID": int(book_id),
                                "Name": name,
                                "Author": author,
                                "Status": status
                            })
                        except ValueError:
                            print(Fore.YELLOW + f"Skipping line with invalid book ID: {line}" + Style.RESET_ALL)
                    else:
                        print(Fore.YELLOW + f"Skipping line with incorrect format: {line}" + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.YELLOW + f"File '{filename}' not found. Creating a new file." + Style.RESET_ALL)
    return books
    


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.status = "Available"
        self.bookID = None

    def __str__(self):
        return f"Book ID: {self.bookID}, Name: {self.name}, Author: {self.author}, Status: {self.status}"


class Library:
    def __init__(self):
        self.books = load_books_from_file()
        if not self.books:
            self.books = [
                {"Name": "Mahabharat", "Author": "VedVyas", "Status": "Available", "bookID": 101},
                {"Name": "Ikigai", "Author": "Francesc Miralles Hector Garcia", "Status": "Available", "bookID": 102},
                {"Name": "Good Vibes Good Life", "Author": "King Vex", "Status": "Available", "bookID": 103},
                {"Name": "Rework", "Author": "Fried Jason", "Status": "Available", "bookID": 104},
                {"Name": "The Go Getter", "Author": "Kyne Peter", "Status": "Available", "bookID": 105}
            ]
            self.next_book_id = 106
        else:
            self.next_book_id = max(book['bookID'] for book in self.books) + 1  # Find next ID

    def add_book(self, book):
        book.bookID = self.next_book_id
        self.books.append({"Name": book.name, "Author": book.author, "Status": book.status, "bookID": book.bookID})
        self.next_book_id += 1
        print(Fore.GREEN + f"The book named {book.name} has been added to the library with ID {book.bookID}" + Style.RESET_ALL)
        return True

    def display_books(self):
        for book in self.books:
            print(Fore.YELLOW + f"Book ID: {book['bookID']} | Name: {book['Name']} | Author: {book['Author']} | Status: {book['Status']}")
    def search_book(self):
        if not self.books:
            print(Fore.RED + "No books available in the library" + Style.RESET_ALL)
            return

        book_name = input("Enter the name of the book you want to search: ")
        for book in self.books:
            if book['Name'] == book_name:
                print(Back.WHITE + Fore.MAGENTA + f"Book ID: {book['bookID']} | Name: {book['Name']} | Author: {book['Author']} | Status: {book['Status']}")
                return

        print(Fore.RED + "Book not found in the library" + Style.RESET_ALL)


class Member:
    def __init__(self):
        self.members = load_members_from_file()
        
        self.next_member_id = 101

    def __str__(self):
        member_info = f"-" * 10 + f"Member ID: {self.member_id}, Name: {self.name}" + "-" * 10 + "\n"
        member_info += "Books borrowed:\n"
        if self.books:
            for book in self.books:
                member_info += f"  ->Book ID: {book['bookID']} | Name: {book['Name']} | Author: {book['Author']} | Status: {book['Status']}\n"
        else:
            member_info += "No books borrowed yet.\n"
        return member_info


    def borrow_book(self, library):
        book_name = input("Enter the name of the book: ")
        for book in library.books:
            if book['Name'] == book_name:
                if book['Status'] == "Available":
                    book['Status'] = "Checked Out"
                    self.books.append(book)
                    print(Fore.GREEN + f"Book '{book_name}' has been borrowed successfully." + Style.RESET_ALL)
                    save_books_to_file(library.books)
                    return
                else:
                    print(Fore.RED + f"Book '{book_name}' is already checked out." + Style.RESET_ALL)
                    return
        print(Fore.RED + "Book not found in the library." + Style.RESET_ALL)

    def return_book(self, library):
        book_name = input("Enter the name of the book: ")
        for book in library.books:
            if book['Name'] == book_name:
                if book['Status'] == "Checked Out" and book in self.books:
                    book['Status'] = "Available"
                    self.books.remove(book)
                    print(Fore.GREEN + f"Book '{book_name}' has been returned successfully." + Style.RESET_ALL)
                    save_books_to_file(library.books)
                    return
                elif book['Status'] == "Available":
                    print(Fore.RED + f"Book '{book_name}' is already available in the library." + Style.RESET_ALL)
                    return
                else:
                    print(Fore.RED + f"Book '{book_name}' is not borrowed by you." + Style.RESET_ALL)
                    return
        print(Fore.RED + "Book not found in the library." + Style.RESET_ALL)

    def display_borrowed_books(self):
        print(self)
        return


##### Main method ######
print(Fore.LIGHTBLUE_EX + "-" * 20+ "Welcome to the library"+"-" * 20)
print(Fore.CYAN + "Menu:")
print(Fore.CYAN +"1. Add a book")
print(Fore.CYAN +"2. Display all books")
print(Fore.CYAN +"3. Search a book")
print(Fore.CYAN +"4. Borrow a book")
print(Fore.CYAN +"5. Return a book")
print(Fore.CYAN +"6. Display borrowed books")
print(Fore.CYAN +"7. Exit" + Style.RESET_ALL)

library = Library()
member = Member(1)

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
            book = Book(name, author)
            if library.add_book(book):
                save_books_to_file(library.books)

        case 2:
            library.display_books()

        case 3:
            library.search_book()

        case 4:
            member.borrow_book(library)

        case 5:
            member.return_book(library)

        case 6:
            member.display_borrowed_books()

        case 7:
            print(Fore.LIGHTBLUE_EX + "-" * 20+ "Exiting the library!!"+ "-" * 20 + Style.RESET_ALL)
            save_books_to_file(library.books)
            break
        case _:
            print(Fore.RED + "Invalid choice. Please try entering a valid choice from the menu")