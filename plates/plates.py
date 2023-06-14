def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    two_letters = s[0:2].isalpha()
    if two_letters == False:
        return False
    plate_length = len(s)
    if plate_length < 2 or plate_length > 6:
        return False

    # numbers must come at the end, the first number cannot be 0
    for index, char in enumerate(s):
        if char.isdigit():
            check_numbers = s[index:-1].isdigit()
            if check_numbers == False:
                return False
        if s[index:-1][0] == '0':
            return False

    return True
main()