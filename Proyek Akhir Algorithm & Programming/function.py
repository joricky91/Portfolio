def writeFile(s, filename):  # mungkin g kepake #####
    newfile = open(filename, 'w')
    for wlist in range(len(s)):
        if wlist == (len(s) - 1):
            line = s[wlist][0] + ',' + s[wlist][1]
        else:
            line = s[wlist][0] + ',' + s[wlist][1] + '\n'
        newfile.write(line)
    newfile.close()


def openFile(filename):  # buka file sekalian read isinya #
    file = open(filename, 'r')  # buka file
    data1 = file.read().split('\n')
    file.close()
    return data1


def writeFormat(li):  # list yg dimasukan harus list terkecil
    s = ''
    for i in range(len(li)):
        if i != len(li)-1:
            s += li[i] + ','
        else:
            s += li[i] + '\n'
    return s


def writeFile2(a, value, filename):
    file = open(filename, 'w')
    for line in range(len(a)):
        text = ''
        for content in range(value):
            if content != value-1:
                text += a[line][content] + ','
            if content == value-1 and line != len(a)-1:
                text += a[line][content] + '\n'
            if line == (len(a)-1) and content == value-1:
                text += a[line][content]
        file.write(text)
    file.close()
