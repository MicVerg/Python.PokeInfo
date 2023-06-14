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
    for char in s:
        if char.isdigit():
            check_numbers = [char:-1].isdigit()
        if check_numbers == False:
            return False
        if [char:-1][0] == '0':
            return False

main()