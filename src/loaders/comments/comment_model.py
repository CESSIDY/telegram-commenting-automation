from dataclasses import dataclass
from enum import Enum


class FileTypes(Enum):
    VIDEO = 1
    TEXT_DOCUMENT = 2  # txt, csv, doc...
    APPLICATION_DOCUMENT = 3  # zip, pdf...
    IMAGE = 4


@dataclass
class CommentLoaderModel:
    message: str
    file_path: [str, None]
    file_type: [FileTypes, None]

    def __init__(self, message: str, file_path: [str, None], file_type: [FileTypes, None]):
        self.message = message
        self.file_path = file_path
        self.file_type = file_type
