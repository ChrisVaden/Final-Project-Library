import csv

filename = r"C:\Users\osman512sd06\PycharmProjects\Ivytechstuff\books_new.csv"
book_survey = {} # Main Dict

with open(filename, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        title = row['Title'].strip()
        author = row['Author'].strip().lower()
        genre = row['Genre'].strip()
        publisher = row['Publisher'].strip()

        # Storing data into book_servery dict
        book_survey[author] = {
            "title": title,
            "genre": genre,
            "publisher": publisher
        }

print(book_survey)

while True:
    asked_author = input("Enter an author name from the dictionary: ").lower().strip()
    if asked_author in book_survey:
        print(f"Their book title is: {book_survey[asked_author]['title']}")
        print(f"The genre is: {book_survey[asked_author]['genre']}")
        print(f"The publisher is: {book_survey[asked_author]['publisher']}")
        break
    else:
        print("Sorry, that author is not in the dictionary, try again.")

# I added this, basically they can add an author, book, genre, etc. if they want
# But it only shows the added books after entering quit

while True:
    action = input(
        "Do you want to add a new book/author? "
        "Type 'add' or 'quit': "
    ).lower().strip()

    if action == "add":
        new_author = input("Enter new author name: ").lower().strip()
        new_title = input("Enter book title: ").strip()
        new_genre = input("Enter genre: ").strip()
        new_publisher = input("Enter publisher: ").strip()

        # nested dictionary for the added author
        book_survey[new_author] = {
            "title": new_title,
            "genre": new_genre,
            "publisher": new_publisher
        }
        print("New entry added successfully!")

    elif action == "quit":
        break
    else:
        print("Invalid choice. Please type 'add' or 'quit'.")

print(book_survey)

# I can add index once you're done turning it into python
# You have to type the exact author's name in order for it to work
# Ex: "hawking, stephen" (without the parenthesis)