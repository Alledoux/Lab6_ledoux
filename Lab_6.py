# Alfred LeDoux
def encoder(uncoded):
    code_dict = {'0':'3','1':'4','2':'5','3':'6','4':'7','5':'8','6':'9','7':'0','8':'1','9':'2'}
    global coded
    coded = ""
    for i in uncoded:
        if i.isdigit():
            coded += code_dict[i]
    return


def main():
    menu = True
    while menu == True:
        print('Menu')
        print('-------------')
        print("1.Encode")
        print('2.Decode')
        print('3.Quit')
        option = input("Please enter an option: ")
        if option == '1':
            uncoded = input("please enter your password to encode: ")
            encoder(uncoded)
            print('your password has been encoded and stored!')
        elif option == '2':
            print('Not done yet')
        elif option == '3':
            break


if __name__ == '__main__':
    main()