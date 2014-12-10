""" An example of how to get a Python handle to a MongoDB database """
import sys
from pymongo import Connection
from pymongo.errors import ConnectionFailure


def main():

    """ connect to mongo db """
    try:

        c = Connection("localhost", port=27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    dbh = c["unicorns"]
    # Demonstrate the db.connection property to retrieve a reference to the
    # Connection object should it go out of scope. In most cases, keeping a
    # reference to the Database object for the lifetime of your program should
    # be sufficient.
    assert dbh.connection == c
    print "Successfully set up a database handle!"

if __name__ == '__main__':
    main()
