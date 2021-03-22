def decrypt(d_val):

    d_word = ''

    for i in d_val:
        d_word = d_word + chr(i-100)

    return d_word


def encrypt(e_val):

    e_list = []

    for i in e_val:
        e_list.append(ord(i)+100)

    return e_list

