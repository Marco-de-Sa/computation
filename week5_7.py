pn = input("input your phone number")
if "+351" in pn:
    print("you come from portugal")
elif "+90" in pn:
    print("you come from turkey")
elif "+354" in pn:
    print("you come from iceland")
else:
    print("Sorry, I don’t recognize your country")