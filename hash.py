information = ["","","","","","","","","",""]
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

def hash_key(ke):
    index_num = hash(ke)%10
    if index_num >= 10 :
        index_num = index_num % 10
    return index_num