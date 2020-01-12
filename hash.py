data = ["","","","","","","","","",""]
def list(key,value,num):
    global data
    data1 = {key,value}
    if data[num] == "":
        data[num]=data1
    else:
        count = -1
        for i in data:
            count = count + 1
            if i == "":
                data[count] = data1
                break
    return data