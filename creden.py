def loggedin():
    cls.a = a1
    if (cls.a == 's'):
        register()
    else:
        login()



def register(username,password,avatar_name):
        username = username
        password = password
        avatar_name = avatar_name
        file = open("login.txt", "a")
        file.write(username)
        file.write(" ")
        file.write(password)
        file.write(" ")
        file.write(avatar_name)
        file.write("\n")
        file.close()


def login(username,password):
        username = username
        password = password
        for line in open("login.txt", "r").readlines():  # Read the lines
            login_info = line.split()  # Split on the space, and store the results in a list of two strings
            if username == login_info[0] and password == login_info[1]:
                print("Correct credentials!")
                return True
        print("Incorrect credentials.")
        return False



def initiate():
    print("enter S for the registeration and L for the login")
    a1 = input('press either S or L for as per your choice')
    if (a1 == 's' or a1 == 'S'):
       register()
        #print(f'NAME OF THE AVATAR IS {playerform.avatar_name}')
    else:
        login()


a1 = input('PRESS S FOR REG AND L FOR LOGIN')


if (a1 == 's' or a1 == 'S'):
    username = input("Enter your player name ")
    password = input("Please enter/Update your password ")
    avatar_name = input('Enter your avatar name')

    register(username,password,avatar_name)
else:
    username = input("Enter your player name ")
    password = input("Please enter/Update your password ")
    avatar_name = input('Enter your avatar name')
    login(username,password)



