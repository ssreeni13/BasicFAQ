def brac_balance(str):
    count = 0
    # flag = False
    for i in str:
        if i == "{" or i == "[" or i == "(":
            count += 1
        elif i == "}" or i == "]" or i == ")":
            count -= 1
    if count > 0:
        print("Not Balanced String")
    elif count == 0:
        print("Balanced String")


str = "{[()}]"
brac_balance(str)
