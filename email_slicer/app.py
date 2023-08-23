def main():
    print(" Welcome to EmailSlicer!")
    print("************************")
    email_input = input("Your email adres:")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username:",username,"|","Domain:",domain,"|","Extension:",extension)

#infinite loop
while True:
    main()