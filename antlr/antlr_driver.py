from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from antlr.WhileLangLexer import WhileLangLexer
from antlr.WhileLangParser import WhileLangParser


class CollectingErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        fragment = offendingSymbol.text if offendingSymbol else ""
        self.errors.append({
            "fragment": fragment,
            "line": line,
            "col": column + 1,
            "description": f"Синтаксическая ошибка: {msg}"
        })


def run_antlr_syntax(text: str):
    input_stream = InputStream(text)
    lexer = WhileLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WhileLangParser(token_stream)

    listener = CollectingErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(listener)

    parser.program()

    return listener.errors
