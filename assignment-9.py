user = input("please enter the first name\n")
my_name = "Hakan"
password = "Zt*17"
if user.capitalize().strip()==my_name:
    print(f"Hello, Hakan! The password is :{password}")
else:
    print(f"Hello,{user}! See you later.")