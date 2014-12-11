""" An example of how to insert a document """
import sys
from datetime import datetime
from pymongo import Connection
from pymongo.errors import ConnectionFailure


def main():
    try:
        c = Connection(host="localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Connection ERROR: %s" % e)
        sys.exit(1)
    dbh = c["test"]
    assert dbh.connection == c

    user_doc = {
        "username": "shreyansh bhushan",
        "firstname": "shreyansh",
        "surname": "bhushan",
        "dateofbirth": datetime(2013, 1, 8),
        "email": "manibhushan.cs@gmail.com",
        "score": 0
    }
    dbh.test.insert(user_doc, safe=True)
    print "Successfully inserted document: %s" % user_doc

if __name__ == '__main__':
    main()
