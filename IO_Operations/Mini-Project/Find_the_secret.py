# Program to find the meeting time and meeting place from a text file.

try:
    filename = input("Enter file name: ")

    if ".txt" not in filename:
        filename = filename + ".txt"

    file = open(filename, "r")

    lines = file.readlines()

    line_count = len(lines)

    if line_count <= 12:
        print("Meeting time:", line_count, "AM")
    else:
        print("Meeting time:", line_count - 12, "PM")

    file.close()

    file = open(filename, "r")

    words = {}

    for line in file:
        line = line.lower()

        line = line.replace(",", "")
        line = line.replace(".", "")
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace('"', "")

        data = line.split()

        for word in data:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

    max_count = 0
    place = ""

    for word in words:
        if words[word] > max_count:
            max_count = words[word]
            place = word

    print("Meeting place:", place.title(), "Street")

    file.close()

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("Error:", e)