import string
import random


if __name__ == "__main__" :
    s1 = string.ascii_lowercase
    # print((s1))
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)

    # to get the length of the password
    plen = int(input("Enter The Password Length:\n "))

    # to combine all strings
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)

    # to shuffle the string
    random.shuffle(s)
    # print(s)
    print("".join(s[0:plen]))

