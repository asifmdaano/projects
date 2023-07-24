# ______________Email conditons___________
# 1. a-z     mdasifwarsi12@gmail.com
# 2. 0-9
# 3. '.' '_' only 1 times
# 4. '@' only 1 times
# 5. '.'  in 3rd or 4th positon


import re
def main():
    emailConditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    userEmail = input("Enter your email Id: ")
    if re.search(emailConditions, userEmail):
        print("Success!")
    else:
        print("Enter the valid email Id")
main()