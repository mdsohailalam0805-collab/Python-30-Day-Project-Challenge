books = ["python", "java", "c++", "javascript", "html", "css"]

print("Welcome to the simple library management system")

print("------------------------------")
print("Available books in the library:")
print("------------------------------")

for book in books:
    print(book)
    
choice = input("\n Do you want to issue or return a book? (issue/return): ")

if choice.lower() == "issue":
    book_name = input("Enter the name of the book you want to issue: ").lower()
    
    if book_name in books:
        books.remove(book_name)
        print(book_name, "has been issued to you successfully.")
        
    else:
        print("book is not available in the library.")
        
elif choice.lower() == "return":
    book_name = input("Enter the name of the book you want to return: ").lower()
    
    if book_name not in books:
        books.append(book_name)
        print(book_name, "has been returned successfully.")
        
    else:
        print("book is already available in the library.")
        
print("\n Updated list of available books in the library:")
print("------------------------------")

for book in books:
     print(book)
     
print('\n Total books available in the library:', len(books))
print("Thank you for using the simple library management system!")
    
     
               
    
 