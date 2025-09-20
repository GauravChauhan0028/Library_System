#Library Management System Made by Gaurav Chauhan

import random

# Store books in a list
library = []

# Function to generate random book ID
def generate_book_id():
    return random.randint(1000, 9999)

# Add a book (with user input)
def add_book():
    author = input("Enter Author: ")
    name = input("Enter Book Name: ")
    year = int(input("Enter Publishing Year: "))
    top_seller = input("Top Seller? (y/n): ")
    rating = float(input("Enter Rating: "))
    availability = int(input("Enter Number of Copies: "))
    language = input("Enter Language: ")

    book = {
        "id": generate_book_id(),
        "author": author,
        "name": name,
        "year": year,
        "top_seller": top_seller,
        "rating": rating,
        "availability": availability,
        "language": language
    }
    library.append(book)
    print(f" Book '{name}' added successfully!\n")

# Borrow a book
def borrow_book():
    name = input("Enter Book Name to Borrow: ")
    qty = int(input("Enter Number of Copies: "))

    for book in library:
        if book["name"].lower() == name.lower():
            if book["availability"] >= qty:
                book["availability"] -= qty
                print(f" Borrowed {qty} copy/copies of '{name}'. Remaining: {book['availability']}\n")
            else:
                print("Not enough copies available!\n")
            return 0

# Show high-rated books (>4.5)
def high_rated_books(): 
    print("\n Books rated more than 4.5:")
    found = False
    for book in library:
        if book["rating"] > 4.5:
            print(book)
            found = True
    if not found:
        print(" No books found with rating > 4.5")
    print()

# List books by language
def books_by_language():
    lang = input("Enter Language: ")
    print(f"\n Books in {lang}:")
    found = False
    for book in library:
        if book["language"].lower() == lang.lower():
            print(book)
            found = True
    if not found:
        print(" No books found in this language")
    print()

# Main Menu
def menu():
    while True:
        print(" Welcome to Library Management System : ")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Show High Rated Books (>4.5)")
        print("4. Books by Language")
        print("5. Show books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            borrow_book()
        elif choice == "3":
            high_rated_books()
        elif choice == "4":
            books_by_language()
        elif choice == "5":
            print("\n Current Books in Library:")
            for book in library:
                print(book)
            print()
        elif choice == "6":
            print("👋 Exiting Library System...")
            break
        else:
            print(" Invalid choice! Try again.\n")

# Run program
if __name__ == "__main__":
    menu()
