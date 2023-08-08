user_input = input("Enter a word that contains the letter 'o': ").lower
letter = 'o'
while True:
    if user_input.find(letter) != -1:
            print("Character found")
            break
            else:
            print("Character not found")

