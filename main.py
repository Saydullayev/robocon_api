from User import PublicUser

s = input("username ni kiriting: ")
user = PublicUser(username=s)

print(user.get_data())