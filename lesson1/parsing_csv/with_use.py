def parseLine(line):
    L = line.split(",")
    return L[0]


def fileRead(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
           print line
    return data


def main():
    data = fileRead("funding.csv")
    print "MAIN: ", data
    print "DONE: "


if __name__ == '__main__':
    main()
