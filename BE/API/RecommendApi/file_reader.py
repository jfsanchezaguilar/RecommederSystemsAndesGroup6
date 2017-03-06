def read_file(algorithm, similarity, training):
    if algorithm == "Jaccard" and similarity == "Item":
        with open("rj"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    elif algorithm == "Cosine" and similarity == "Item":
        with open("rc"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    elif algorithm == "Pearson" and similarity == "Item":
        with open("rp"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    if algorithm == "Jaccard" and similarity == "User":
        with open("rj"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    elif algorithm == "Cosine" and similarity == "User":
        with open("rc"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    elif algorithm == "Pearson" and similarity == "User":
        with open("rp"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
