def melon_report(day, file):
    """Using the given day and file, prints the count of melon, the type of melon sold, and the amount made"""

    print(f"Day {day}")
    # print the day and day number

    the_file = open(file)
    # set the_file to open the the given parameter, file

    for line in the_file:
        line = line.rstrip()
        # removes any trailing characters
        words = line.split('|')
        # splits each line into a list, separated by the |

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
        #prints count, melon type, and amount made

    the_file.close()

melon_report("1", "um-deliveries-20140519.txt")
melon_report("2", "um-deliveries-20140520.txt")
melon_report("3", "um-deliveries-20140521.txt")