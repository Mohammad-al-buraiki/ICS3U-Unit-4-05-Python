# !/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program is a loop a for loop


def main():
    # this function uses a for loop

    loop_counter = 0

    # input
    print("")
    positive_integer = input("How many times to add: ")

    # process and output
    try:
        positive_integer = int(positive_integer)
        while loop_counter < positive_integer:
            loop_counter = loop_counter + 1
            if positive_integer < 0:
                continue
            print(input("Enter a number: "))

    except Exception:
        print("that was not an integer")


if __name__ == "__main__":
    main()
