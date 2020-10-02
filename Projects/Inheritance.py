# abc - abstract base class
from abc import ABC, abstractmethod


# Create a custom exceptions which is not built-in in Python
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    # define open method
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    # define close method
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    # if the class derives from a stream class it has to implement
    # this method (read) otherwise that class will also be concidered abstract
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory.")


stream = MemoryStream()
stream.open()
