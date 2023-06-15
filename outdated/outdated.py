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
# change from MM/DD/YYYY to YYYY-MM-DD
# examples: 12/31/1636 OR december 31, 1636

while True:

    user_input = input("Date: ")

    if "/" in user_input:
        M, D, Y = user_input.split('/')
        # if month is too big, reprompt
        if int(M) > 12:
            user_input = input("Date: ")
            M, D, Y = user_input.split('/')
        # if day is too big, reprompt
        if int(D) > 31:
            user_input = input("Date: ")
            M, D, Y = user_input.split('/')

        # format month and date to pad leading 0
        print(f"{Y}-{int(M):02d}-{int(D):02d}")
        break

    if "," in user_input:
        M, D, Y = user_input.split(' ')
        # remove trailing ,
        D = D.replace(',', '')
        # change month string to integer
        M = (months.index(M)) + 1

        # if month is too big, reprompt
        if int(M) > 12:
            user_input = input("Date: ")
            M, D, Y = user_input.split(' ')
        # if day is too big, reprompt
        if int(D) > 31:
            user_input = input("Date: ")
            M, D, Y = user_input.split('/')

        print(f"{Y}-{int(M):02d}-{int(D):02d}")
        break
