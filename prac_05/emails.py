def extract_name_from_email(email):
    name_part = email.split('@')[0]

    name_part = name_part.replace('.', ' ').replace('_', ' ')
    return name_part.title()

def get_emails():
    email_to_name = {}

    while True:
        # Ask the user for an email
        email = input("Email: ")

        if email == "":
            break

        name = extract_name_from_email(email)

        response = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if response == 'n' or response == 'no':
            name = input("Name: ")

        email_to_name[email] = name

    return email_to_name


def main():
    emails_dict = get_emails()

    for email, name in emails_dict.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
