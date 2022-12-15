import grpc

from service import inventoryservice_pb2 as pb2
from service import inventoryservice_pb2_grpc as pb2_grpc


class InventoryClient:
    def __init__(self, serverAddress):
        self.serverAddress = serverAddress

    # setting up the client address
    def getBookTitle(self, isbnList):
        with grpc.insecure_channel(self.serverAddress) as channel:
            stub = pb2_grpc.InventoryServiceStub(channel)

            result = []
            for isbn in isbnList:
                response = stub.GetBook(pb2.GetBookRequest(isbn=isbn))
                result.append(response.book.title)

            return result
