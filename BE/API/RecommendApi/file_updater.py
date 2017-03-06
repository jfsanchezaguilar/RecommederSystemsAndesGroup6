def update_book_user_file(user_id, location, age):
    f = open("Users.csv", "a")
    f.write("\"" + str(user_id) + "\";" + "\"" + str(location) + "\";" + "\"" + str(age) + "\"\n")
    f.close()


def update_book_file(isbn, book_title, book_author, year_publish, publisher, image_small, image_medium, image_large):
    f = open("Books.csv", "a")
    f.write("\"" + str(isbn) + "\";" + "\"" + str(book_title) + "\";" + "\"" + str(book_author) + "\";"
            + "\"" + str(year_publish) + "\";" + "\"" + str(publisher) + "\";"
            + "\"" + str(image_small) + "\";" + "\"" + str(image_medium) + "\";"
            + "\"" + str(image_large) + "\"\n")
    f.close()


def update_book_raiting_file(user_id, isbn, raiting):
    f = open("Raiting.csv", "a")
    f.write("\"" + str(user_id) + "\";" + "\"" + str(isbn) + "\";" + "\"" + str(raiting) + "\"\n")
    f.close()
