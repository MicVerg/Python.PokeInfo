months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# change from MM DD YYYY to YYYY MM DD
# examples: 12/31/1636 OR december 31, 1636

user_input = input("Date: ")

M, D, Y = user_input.split('/')
print(f"{Y}-{M:02d}-{D:02d}")