alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def main():
    
    cipher_continue = True

    while cipher_continue:
        option = input("Will you encode or decode: ")
        message = input("What is your message: ")
        shift = int(input("How much will you offset: "))

        print(caesar(option, message, shift))

        keep_playing = input("Keep Playing? [yes/no]")
        if keep_playing == 'no':
            print("User exited program!")
            cipher_continue = False

def caesar(option, message, shift):
    new_text = ""
    if option == 'decode':
        shift *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_text += alphabet[new_position]

    return new_text



if __name__ == "__main__":
    main()

