import grpc
import logging
from protos.service import inventoryservice_pb2 as pb2
from protos.service import inventoryservice_pb2_grpc as pb2_grpc
from concurrent import futures

book1 = pb2.Book(
    isbn="1001",
    title="Harry Potter",
    author="J K Rowling",
    year=1999,
    genre=pb2.FICTION
)

book2 = pb2.Book(
    isbn="1002",
    title="Fault In Our Stars",
    author="John Green",
    year=2012,
    genre=pb2.ROMANCE
)

bookList = [book1, book2]


class InventoryServicer(pb2_grpc.InventoryServiceServicer):

    def CreateBook(self, request, context):

        for book in bookList:
            if request.book.isbn == book.isbn:
                print("Book by this ISBN exists already. Try again.")
                return pb2.CreateBookResponse(statusCode=400)

        newBook = pb2.Book(
            isbn=request.book.isbn,
            title=request.book.title,
            author=request.book.author,
            year=request.book.year,
            genre=request.book.genre
        )

        bookList.append(newBook)
        print("Book added to the database.")
        return pb2.CreateBookResponse(statusCode=201)

    def GetBook(self, request, context):

        for book in bookList:
            if request.isbn == book.isbn:
                return pb2.GetBookResponse(book=book)

        return pb2.GetBookResponse()


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_InventoryServiceServicer_to_server(InventoryServicer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
