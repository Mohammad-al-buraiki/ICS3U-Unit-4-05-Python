# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a loop a for loop


def main():
    # this function uses a for loop

    loop_counter = 0

    # input
    print("")
    times = int(input("How many times to add: "))
    total = 0

    # process and output
    try:
        times == int(times)
        for loop_counter in range(times):
            number = int(input("Enter the number:"))
            total = total + number
        print("")
        print("the total is {0}.".format(total))

    except Exception:
        print("that was not an integer")


if __name__ == "__main__":
    main()
