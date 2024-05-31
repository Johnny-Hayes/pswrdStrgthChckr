def lenCheck(password):
    passLen = len(password)
    if passLen < 8:
        print("your password is too short.")
    elif passLen >= 8 and passLen < 12:
        print("password length is acceptable. Try reach 12 characters.")
    else:
        print("password length is strong.")


def symbolCheck(password):
    symbols = "!#@?()/*£$%&+_-:;{}[]<>^,."
    symbols_found = []
    for character in password:
        if character in symbols:
            symbols_found.append(character)
    if len(symbols_found) == 0:
        print("password is weak. Add special symbols.")
    elif len(symbols_found) == 1:
        print("password symbol use is acceptable. Try add 1 more symbol.")
    else:
        print("password symbol use is strong.")


def capitalCheck(password):
    for character in password:
        if character.isupper():
            print("Password contains capital letter. Well done!")
            break
        else:
            print("Add at least 1 capital letter.")
            break


def pswrdStrengthCheck(password):
    lenCheck(password)
    symbolCheck(password)
    capitalCheck(password)


password = input("Is your password compliant with NIST guidelines?: ")

pswrdStrengthCheck(password)
