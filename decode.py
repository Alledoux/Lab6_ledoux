
#Carson Hernandez
def decoder(coded):

    decoded_string = str(coded)

    for i in decoded_string:

        if i == "0":
            decoded_string = decoded_string.replace("0", "7")
        if i == "1":
            decoded_string = decoded_string.replace("1", "8")
        if i == "2":
            decoded_string = decoded_string.replace("2", "9")
        if i == "3":
            decoded_string = decoded_string.replace("3", "0")
        if i == "4":
            decoded_string = decoded_string.replace("4", "1")
        if i == "5":
            decoded_string = decoded_string.replace("5", "2")
        if i == "6":
            decoded_string = decoded_string.replace("6", "3")
        if i == "7":
            decoded_string = decoded_string.replace("7", "4")
        if i == "8":
            decoded_string = decoded_string.replace("8", "5")
        if i == "9":
            decoded_string = decoded_string.replace("9", "6")

            return decoded_string

    return decoded_string