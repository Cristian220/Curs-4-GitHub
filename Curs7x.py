def addbook():
    book_name = input("Insert a book name ->")
    author_name = input("Insert a author name ->")
    import csv
    with open("booksDB.csv", "w") as file:
        writer = csv.DictWriter(file,fieldnames=[
            "BookName", "AuthorName", "SharedWith", "Isread"
        ])
        writer.writerow({"BookName": book_name,
                        "AuthorName": author_name
                            })
print("Book was added successfully")
def add_Book():
    print("Add a book option")
def list_Books():
    print("List books option")
def update_Book():
    print("Update a book option")
def share_Book():
    print("Share a book option")








#Main menu for use
print("Menu : ")
print("1 : Add a book")
print("2 : List books")
print("3 : Update book")
print("4 : Share book")
option = int(input("Select one option -> "))
if option == 1:
    add_Book()
elif option == 2:
    list_Books()
elif option == 3:
    update_Book()
elif option == 4:
    share_Book()
else:
    print("Not a valid option")


