def email_validation(email:str,/)-> str:
    """It's a Email validation program that
    check whether your email is valid or not.
    """
    k,j, d = 0,0,0
    if len(email) >= 6:
        if email[0].isalpha():
            if ("@" in email) and (email.count("@") == 1):
                if (email[-4] == ".") ^ (email[-3] == "."):
                    for i in email:
                        if i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1
                    if k == 1 or j == 1 or d == 1:
                        print("5:Please enter valid email")
                    else:
                        print("Success!")
                else:
                    print("4:Please enter valid email ")
            else:
                print("3:Pleae enter valid email ")
        else:
            print("2:Please enter valid email ")
    else:
        print("1:Please enter valid email ")

def main():
    print(email_validation.__doc__)
    email = input("Enter your valid email here: ")  # a@b.in | mdsifwarsi12@gmail.com
    email_validation(email)

main()