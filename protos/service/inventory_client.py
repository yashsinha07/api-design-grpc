import grpc
import logging
import inventoryservice_pb2 as pb2
import inventoryservice_pb2_grpc as pb2_grpc
from google.protobuf.json_format import MessageToDict


def run():

    book = pb2.Book(
        isbn="1002",
        title="Twilight",
        author="Nobody Cares",
        year=2007,
        genre=pb2.ROMANCE
    )

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.InventoryServiceStub(channel)
        response1 = stub.GetBook(pb2.GetBookRequest(isbn='1001'))

        response2 = stub.CreateBook(pb2.CreateBookRequest(book=book))

    dict_obj1 = MessageToDict(response1)
    print(f'Client request received: {dict_obj1}')
    dict_obj2 = MessageToDict(response2)
    print(f'Client request received: {dict_obj2}')


if __name__ == '__main__':
    logging.basicConfig()
    run()
