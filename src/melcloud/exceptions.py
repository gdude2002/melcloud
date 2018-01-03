# coding=utf-8
__author__ = "Gareth Coles"


class MELCloudError(Exception):
    """
    Raised during a request to MELCloud, when an error is present in the returned data

    :ivar error_number: Error numeric returned by MELCloud
    :vartype error_number: int

    :ivar error_message: Error message returned by MELCloud
    :vartype error_message: int
    """

    def __init__(self, num: int, message: str, *args):
        self.error_number = num
        self.error_message = message
        super(MELCloudError, self).__init__(f"(Error {num}) {message}", *args)


class NotLoggedInError(Exception):
    def __init__(self, *args):
        super().__init__("Not logged in", *args)
