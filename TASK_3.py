import random


def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_"
    password = ""
    for _ in range(length):
        next_char_index = random.randrange(len(characters))
        password += characters[next_char_index]
    return password


def main():
    num_passwords = int(input("Number of Passwords to be Generated? : "))
    print("Generating {} passwords.....".format(num_passwords))

    passwords = []

    for i in range(num_passwords):
        while True:
            length = int(input("Enter the length of Password #{}: ".format(i + 1)))
            if length < 6:
                print("Error: Password length should be at least 6 characters.")
            else:
                passwords.append(generate_password(length))
                break

    for i, password in enumerate(passwords):
        print("Password #{} = {}".format(i + 1, password))


if __name__ == "__main__":
    main()
