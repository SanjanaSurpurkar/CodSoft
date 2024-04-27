import random
import string

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(random.choice(char) for _ in range(length))
    return passw
def main():
    print("Password Generator!")

    while True:
        try:
            len = int(input("Enter the desired length of the password: "))
            if len <= 0:
                print("Please Enter a Positive Integer.")
                continue
            passw = generate_password(len)
            print(f"Generated Password: {passw}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
