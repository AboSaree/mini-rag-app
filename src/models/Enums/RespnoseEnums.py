from enum import Enum
class ResponseEnums(Enum):
    SUCCESS = "Success"
    SIZE_EXCEEDED = "File size exceeded the maximum limit."
    INVALID_TYPE = "Invalid file type."
    PROCESS_ERROR = "Error processing the file."