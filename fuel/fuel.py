
while True:
    try:
        user_input = input("Fraction: ")
    
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break