import os


def extractTitles(line):
    titles = line.split(",")
    # print titles
    return [t.strip() for t in titles]


def getDict(line, keys):
    vals = line.split(",")
    values = [v.strip() for v in vals]
    D = {}
    for i in range(len(keys)):
        D[keys[i]] = values[i]

    return D


def parseFile(datafile):
    data = []
    titles = []
    first = True
    count = 0
    f = open(datafile, 'r')
    while True:
        line = f.readline()
        if first:
            titles = extractTitles(line)
            first = False
        elif count < 10:
            data.append(getDict(line, titles))
            count += 1
        else:
            break

    return data


def main():
    dataDir = ""
    # fileName = "funding.csv"
    # fileName = "beatles-1.csv"
    fileName = "beatles-diskography.csv"
    dataFilePath = os.path.join(dataDir, fileName)
    # print "FILE PATH: ", dataFilePath
    D = parseFile(dataFilePath)
    if D:
        print "Length of parsed file: ", len(D)
        for i in range(len(D)):
            print D[i]
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1',
                 'Label': 'Parlophone(UK)', 'Released': '22 March 1963',
                 'US Chart Position': '-', 'RIAA Certification': 'Platinum',
                 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1',
                 'Label': 'Parlophone(UK)', 'Released': '10 July 1964',
                 'US Chart Position': '-', 'RIAA Certification': '',
                 'BPI Certification': 'Gold'}

    assert D[0] == firstline
    print tenthline
    assert D[9] == tenthline


if __name__ == '__main__':
    main()
