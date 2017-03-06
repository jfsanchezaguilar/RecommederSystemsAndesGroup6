def read_file(algorithm, similarity, training):
    if algorithm == "Jaccard" and similarity == "Item":
        with open("/home/ubuntu/ItemBased/rj"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    elif algorithm == "Cosine" and similarity == "Item":
        with open("/home/ubuntu/ItemBased/rc"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    elif algorithm == "Pearson" and similarity == "Item":
        with open("/home/ubuntu/ItemBased/rp"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    if algorithm == "Jaccard" and similarity == "User":
        with open("/home/ubuntu/UserBased/rj"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    elif algorithm == "Cosine" and similarity == "User":
        with open("/home/ubuntu/UserBased/rc"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
    elif algorithm == "Pearson" and similarity == "User":
        with open("/home/ubuntu/UserBased/rp"+str(training)+".json", 'r') as content_file:
            content = content_file.read()
        return content
