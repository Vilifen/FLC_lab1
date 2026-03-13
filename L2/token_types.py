from enum import Enum, auto

class TokenType(Enum):
    KEYWORD = auto()
    IDENTIFIER = auto()
    NUMBER = auto()
    OPERATOR = auto()
    SEPARATOR = auto()
    WHITESPACE = auto()
    EOF = auto()
