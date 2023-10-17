def updatecheckpoint(file, index):
    f = open(file, "w")
    f.write(str(index))
    f.close()


def opencheckpoint(file):
    return open(file, "r")
