import operator
from book import Book

b1 = Book("Title 1", "Author 1", 2008, 300)
b2 = Book("Title 2", "Author 2", 1998, 400)

books = [b1, b2]
books.append(Book("Title 3", "Author 3", 2025, 50))

print("List of books")
for book in books:
    print(book)

b4 = Book("Title 1", "Author 1", 1000, 1)

if b1 == b4:
    print("Books are equal")
else:
    print("Books are not equal")

print("Now, the list is sorted and printed again")

books.append(Book("Title 5", "Author 5", 2008, 100))
books.append(Book("Title 6", "Author 5", 2008, 500))

sorted_books = sorted(books)

for book in sorted_books:
    print(book)