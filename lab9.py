#Nikash Jakkidi 
# Mandar Ghade
def main():
    current_password = ''
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            password = input('Please enter your password to encode: ')
            current_password = encode(password)
            print('Your password has been encoded and stored!')
        elif menu_option == 2:
            decoded_password = decode(current_password)
            print(f'The encoded password is {current_password}, and the original password is {decoded_password}.')
        elif menu_option == 3:
            break
        else:
            continue


def encode(password):
    encrypted_password = ''
    for num in password:
        encrypted_password += str(int(num)+3)[-1]
    return encrypted_password


def decode(encrypted_password):
    return ''.join(str(10+int(c)-3)[-1]
                   for c in encrypted_password)


if __name__ == '__main__':
   main()
