import os


def read_file(algorithm, similarity, training, user_id, book_id, is_book):
    if algorithm == "Jaccard" and similarity == "Item":
        path = os.path.join(os.path.expanduser('~'), 'ItemBased', "rj" + str(training) + ".json")
    elif algorithm == "Cosine" and similarity == "Item":
        path = os.path.join(os.path.expanduser('~'), 'ItemBased', "rc" + str(training) + ".json")
    elif algorithm == "Pearson" and similarity == "Item":
        path = os.path.join(os.path.expanduser('~'), 'ItemBased', "rp" + str(training) + ".json")
    if algorithm == "Jaccard" and similarity == "User":
        path = os.path.join(os.path.expanduser('~'), 'UserBased', "rj50.json")
    elif algorithm == "Cosine" and similarity == "User":
        path = os.path.join(os.path.expanduser('~'), 'UserBased', "rj50.json")
    elif algorithm == "Pearson" and similarity == "User":
        path = os.path.join(os.path.expanduser('~'), 'UserBased', "rj50.json")
    print(path)
    if is_book:
        lines = [line for line in open(path) if book_id in line]
    else:
        lines = [line for line in open(path) if user_id in line]
    lines = [line[1:].rstrip('\n') for line in lines]
    lines = ",".join(lines)
    lines = "["+lines+"]"
    return lines
