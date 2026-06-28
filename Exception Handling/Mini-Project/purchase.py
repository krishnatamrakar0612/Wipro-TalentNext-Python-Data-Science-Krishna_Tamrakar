# Program to read purchase details from a file and display
# number of items, free items, amount to pay,
# discount, and final amount.

try:
    filename = input("Enter the file name: ")

    if not filename.endswith(".txt"):
        filename += ".txt"

    file = open(filename, "r")

    item_count = 0
    free_items = 0
    total_amount = 0

    for line in file:
        line = line.strip()

        if line == "":
            continue

        data = line.split()

        item_count += 1

        price = int(data[1])

        if price == 0:
            free_items += 1

        total_amount += price

    file.close()

    if total_amount > 100:
        discount = 5
    else:
        discount = 0

    final_amount = total_amount - discount

    print("No of items purchased:", item_count)
    print("No of free items:", free_items)
    print("Amount to pay:", total_amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("Error:", e)