import logging
from inventory_client import InventoryClient


def getBookDetails(client, isbns):
    print(client.getBookTitle(isbns))


if __name__ == '__main__':
    logging.basicConfig()

    # Encapsulating the Inventory Client
    # and sending a hard coded list of isbns based on which
    # the hard coded database will be queried.
    inventoryClient = InventoryClient('localhost:50051')
    isbnList = ["1001", "1002"]
    getBookDetails(inventoryClient, isbns=isbnList)

