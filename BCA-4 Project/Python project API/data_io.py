from colorama import Fore, Style, init

init(autoreset=True)

def save_member_details(members, filename="members.txt"):
    with open(filename, "w") as file:
        for member in members:
            borrowed_books_str = "|".join([book['Name'] for book in member.get('Borrowed Books', [])])
            file.write(f"{member['Member ID']}|{member['Member Name']}|{borrowed_books_str}\n")

def save_books_to_file(books, filename="books.txt"):
    with open(filename, "w") as file:
        for book in books:
            file.write(f"{book['bookID']}|{book['Name']}|{book['Author']}|{book['available_copies']}\n")

def load_members_from_file(filename="members.txt"):
    members = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    values = line.split("|")
                    if len(values) >= 2:
                        try:
                            member_id, member_name, *borrowed_books_list = values
                            borrowed_books = []
                            if len(borrowed_books_list) > 0 and borrowed_books_list[0]:
                                borrowed_books = [{'Name': book_name} for book_name in borrowed_books_list[0].split("|")]
                            members.append({
                                "Member ID": int(member_id),
                                "Member Name": member_name,
                                "Borrowed Books": borrowed_books
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
                            book_id, name, author, copies = values
                            books.append({
                                "bookID": int(book_id),
                                "Name": name.strip(),  # Remove leading/trailing spaces
                                "Author": author.strip(), # Remove leading/trailing spaces
                                "available_copies": int(copies)
                            })
                        except ValueError:
                            print(Fore.YELLOW + f"Skipping line with invalid book ID or copies: {line}" + Style.RESET_ALL)
                    else:
                        print(Fore.YELLOW + f"Skipping line with incorrect format: {line}" + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.YELLOW + f"File '{filename}' not found." + Style.RESET_ALL)
    return books