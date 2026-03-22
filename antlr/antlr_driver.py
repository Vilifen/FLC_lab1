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
            "description": msg
        })


def normalize_errors(errors):
    has_missing_semicolon = any(
        "missing ';'" in e["description"] or "missing ';' at '<EOF>'" in e["description"]
        for e in errors
    )

    normalized = []

    for e in errors:
        desc = e["description"]

        if "missing ';'" in desc or "missing ';' at '<EOF>'" in desc:
            normalized.append({
                "fragment": e["fragment"],
                "line": e["line"],
                "col": e["col"],
                "description": "Синтаксическая ошибка: missing ';' after '}'"
            })
            return normalized

        if "extraneous input '}'" in desc and has_missing_semicolon:
            continue

        normalized.append({
            "fragment": e["fragment"],
            "line": e["line"],
            "col": e["col"],
            "description": f"Синтаксическая ошибка: {desc}"
        })

    return normalized


def run_antlr_syntax(text: str):
    input_stream = InputStream(text)
    lexer = WhileLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WhileLangParser(token_stream)

    listener = CollectingErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(listener)

    parser.program()

    return normalize_errors(listener.errors)
