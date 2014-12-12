import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure


def mdbConnect(dbname):
    """ connect to mongo db """
    try:
        c = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    dbh = c[dbname]

    assert dbh.connection == c
    print "MongoDB connection SUCCESS!"
    return dbh


def readInput():
    name = raw_input("Enter name to be searched: ")
    return name.strip()


def main():
    dbname = "unicorns"
    dbh = mdbConnect(dbname)
    # name = readInput()
    user_doc = dbh.unicorns.find({"name": "Dunx"})
    if user_doc:
        print "DOC found in DB!"
        for x in user_doc:
            print x \
        # print u['_id']
    else:
        print "DOC Not Found in DB!"

if __name__ == '__main__':
    main()
