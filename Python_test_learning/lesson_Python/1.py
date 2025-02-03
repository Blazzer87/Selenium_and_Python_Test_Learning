with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    print(contents)
    print(type(contents))
    len_user = []
    len_user.append([str1])
    print(len_user)