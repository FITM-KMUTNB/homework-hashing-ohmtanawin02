information = ["","","","","","","","","",""]
again = "Y"
def list(key,value,number):
    global information
    data = {key,value}
    if information[number] == "":
        information[number]=data
    else:
        count = -1
        for i in information:
            count = count + 1
            if i == "":
                information[count] = data
                break
    return information

def hash_key(key):
    index_num = hash(key)%10
    if index_num >= 10 :
        index_num = index_num % 10
    return index_num
while again == "Y":
    print("1.INSERT")
    print("2.SEARCH")
    print("3.EXIT")
    enter = input("Enter choice : ")
    if enter == "1":
        one = "Y"
        while one == "Y":
            if "" not in information:
                print("Full")
                one = "N"
            key = input("Enter Name : ")
            value = input("Enter id : ")
            number = hash_key(key)
            list(key,value,number)
            one = input("More input : Y=yes ,N = Negative : ")
    elif enter == "2" :
        two = "Y"
        while two == "Y":
            key = input('Enter name : ')
            number = hash_key(key)
            if key in information[number]:
                print("Your ID : ",information[number].get(key))
            else:
                for i in information:
                    if key in i :
                        print("your ID : ",i.get(key))
                        break
            two = input("More input : Y=yes ,N = Negative : ")
    else:
        again = "N"