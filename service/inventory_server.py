import grpc
import logging
from service import inventoryservice_pb2 as pb2
from service import inventoryservice_pb2_grpc as pb2_grpc
from concurrent import futures

# Hard coding a couple of book entries for
# the purpose of querying.
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

        # If a book with the same isbn sent in the request
        # exist already, respond with a BAD REQUEST status code.
        for book in bookList:
            if request.book.isbn == book.isbn:
                print("Book by this ISBN exists already. Try again.")
                return pb2.CreateBookResponse(statusCode=400)

        # Create a new book based on the request.
        newBook = pb2.Book(
            isbn=request.book.isbn,
            title=request.book.title,
            author=request.book.author,
            year=request.book.year,
            genre=request.book.genre
        )

        # Add the book to the hard coded database and send
        # a 201 CREATED status code in the response.
        bookList.append(newBook)
        print("Book added to the database.")
        return pb2.CreateBookResponse(statusCode=201)

    def GetBook(self, request, context):
        # Retrieves a book object based on the isbn
        # coming in the request.
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
