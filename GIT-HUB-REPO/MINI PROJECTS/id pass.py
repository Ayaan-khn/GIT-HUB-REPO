userid = input("Enter the username:")
password = input("Enter the password:")
print("userid - ", userid, "|", "password - ", password)

if userid == "ayaankhan00220@gmail.com" and password == "ayaankhan":
    print("Login succesfull")

elif userid == "ayaankhan00220@gmail.com" and password != "ayaankhan":
    print("Incorrect Password ")

elif userid != "ayaankhan00220@gmail.com" and password == "ayaankhan":
    print("Incorrect Username")

else:  # userid != "ayaankhan00220@gmail.com" and password != "ayaankhan":
    print("Userid and password Incorrect")