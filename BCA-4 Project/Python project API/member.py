from colorama import Fore, Style, init, Back
from data_io import load_members_from_file, save_member_details

init(autoreset=True)

class Member:
    def __init__(self):
        self.members = load_members_from_file()
        self.books = []
        self.next_member_id = self.calculate_next_member_id()

    def calculate_next_member_id(self):
        if self.members:
            return max(member["Member ID"] for member in self.members) + 1
        else:
            return 101

    def add_member(self, member_name):
            new_member = {
                "Member ID": self.next_member_id,
                "Member Name": member_name,
                "Borrowed Books": []
            }
            self.members.append(new_member)
            self.next_member_id += 1
            save_member_details(self.members)
            print(Fore.GREEN + f"Member '{member_name}' added with ID: {new_member['Member ID']}" + Style.RESET_ALL)

    def update_member(self, member_id, new_member_name):
        found = False
        for member in self.members:
            if member["Member ID"] == member_id:
                member["Member Name"] = new_member_name
                found = True
                save_member_details(self.members)
                print(Fore.GREEN + f"Member ID {member_id} updated to name '{new_member_name}'" + Style.RESET_ALL)
                break
        if not found:
            print(Fore.RED + f"Member ID {member_id} not found." + Style.RESET_ALL)

    def delete_member(self, member_id):
        initial_length = len(self.members)
        self.members = [member for member in self.members if member["Member ID"] != member_id]
        if len(self.members) < initial_length:
            save_member_details(self.members)
            print(Fore.RED + f"Member ID {member_id} deleted." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Member ID {member_id} not found." + Style.RESET_ALL)

    def display_members(self):
            if not self.members:
                print(Fore.YELLOW + "No members in the system." + Style.RESET_ALL)
                return
            for member in self.members:
                print(Fore.CYAN + f"Member ID: {member['Member ID']} | Member Name: {member['Member Name']}")
    
    def __str__(self):
        member_info = f"-" * 10 + f"Member ID: {self.next_member_id}, Name: {self.members[0]['Member Name: ']}" + "-" * 10 + "\n"
        member_info += "Books borrowed:\n"
        if self.books:
            for book in self.books:
                member_info += f"  ->Book ID: {book['bookID']} | Name: {book['Name']} | Author: {book['Author']} | Copies Available: {book['available_copies']}\n"
        else:
            member_info += "No books borrowed yet.\n"
        return member_info

    def borrow_book(self, library, member_id):
        book_name = input("Enter the name of the book: ")
        borrowed_book = library.borrow_book(book_name)
        if borrowed_book:
            for member in self.members:
                if member["Member ID"] == member_id:
                    member["Borrowed Books"].append(borrowed_book)
                    save_member_details(self.members)
                    print(Fore.GREEN + f"Book '{book_name}' has been borrowed successfully by Member ID {member_id}." + Style.RESET_ALL)
                    return
            print(Fore.RED + "Member ID not found." + Style.RESET_ALL)

    def return_book(self, library, member_id):
            book_name = input("Enter the name of the book to return: ")
            library.return_book(book_name)
            for member in self.members:
                if member["Member ID"] == member_id:
                    member["Borrowed Books"] = [book for book in member["Borrowed Books"] if book['Name'] != book_name]
                    save_member_details(self.members)
                    print(Fore.GREEN + f"Book '{book_name}' returned by Member ID {member_id}." + Style.RESET_ALL)
                    return
            print(Fore.RED + "Member ID not found." + Style.RESET_ALL)

    def display_borrowed_books(self, member_id):
        for member in self.members:
            if member["Member ID"] == member_id:
                if not member["Borrowed Books"]:
                    print(Fore.YELLOW + "No books borrowed yet." + Style.RESET_ALL)
                    return
                print(Fore.CYAN + f"Books borrowed by {member['Member Name']}:" + Style.RESET_ALL)
                for book in member["Borrowed Books"]:
                    print(f"  - Book ID: {book['bookID']}, Name: {book['Name']}, Author: {book['Author']}, Copies Available: {book['available_copies']}")
                return
        print(Fore.RED + "Member ID not found." + Style.RESET_ALL)

        print(Fore.CYAN + "Books borrowed by " + self.members[0]['Member Name: '] + ":" + Style.RESET_ALL)
        for book in self.books:
            print(f"  - Book ID: {book['bookID']}, Name: {book['Name']}, Author: {book['Author']}, Copies Available: {book['available_copies']}")