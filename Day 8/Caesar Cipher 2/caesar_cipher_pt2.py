alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shift_pos = alphabet.index(letter) + shift_amount
        shift_pos %= len(alphabet)
        output_text += alphabet[shift_pos]
    print(f"Here is the result: {output_text}")

caesar(text, shift, direction)


