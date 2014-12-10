import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure


def main():
    ''' connect to mongo db '''
    try:
        c = Connection(host="localhost", port=27017)
        print 'Successful Connection!'
        print "HOST: ", c.HOST
        print "PORT: ", c.PORT
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to Mongo DB: %s" % e)


if __name__ == '__main__':
    main()
