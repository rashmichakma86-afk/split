with open("sample_doc.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

    file.close()