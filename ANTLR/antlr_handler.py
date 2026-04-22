import sys
from antlr4 import *

try:
    from .WhileLangLexer import WhileLangLexer
    from .WhileLangParser import WhileLangParser
except ImportError:
    pass

from .error_listener import MyErrorListener


def execute_antlr_analysis(text):
    input_stream = InputStream(text)

    lexer = WhileLangLexer(input_stream)
    lexer_listener = MyErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(lexer_listener)

    stream = CommonTokenStream(lexer)

    parser = WhileLangParser(stream)
    parser_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(parser_listener)

    tree = parser.program()

    token_rows = []
    stream.fill()
    for token in stream.tokens:
        if token.type != Token.EOF:
            token_rows.append({
                "code": token.type,
                "type": lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else "UNKNOWN",
                "lexeme": token.text,
                "line": token.line,
                "col": token.column
            })
    all_errors = lexer_listener.errors + parser_listener.errors

    error_output = []
    for err in all_errors:
        error_output.append({
            "code": err["code"],
            "type": err["type"],
            "lexeme": err["lexeme"],
            "location": err["location"],
            "description": err["msg"],
            "line": err["line"],
            "col": err["col"]
        })

    return token_rows, error_output