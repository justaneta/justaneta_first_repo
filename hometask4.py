#1
user_input = input("Enter a word that contains the letter 'o': ")
while True:
    if user_input.lower() == 'o':
        print("Character found")
        break
    else:
        print("Character not found")


#2
list_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list_2 = []
for item in list_1:
    if isinstance(item, str):
        list_2.append(item)
print(list_2)

#3
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list_of_numbers:
    if num % 2 == 0:
        print(num, end=" ")
