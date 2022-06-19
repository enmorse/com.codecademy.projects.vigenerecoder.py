alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?!' "


def vigenere_coder(message, keyword):
    letter_pointer = 0
    final_keyword = ''

    for i in range(len(message)):
        if message[i] in punctuation:
            final_keyword += message[i]
        else:
            final_keyword += keyword[letter_pointer]
            letter_pointer = (letter_pointer + 1) % len(keyword)

    translated_message = ''

    for i in range(len(message)):
        if not message[i] in punctuation:
            letter_value = alphabet.find(message[i]) + alphabet.find(
                final_keyword[i])
            translated_message += alphabet[letter_value % 26]
        else:
            translated_message += message[i]

    return translated_message


message = "thanks for teaching me all these cool " \
          "ciphers! you really are the best!"
keyword = "friends"

print(vigenere_coder(message, keyword))
