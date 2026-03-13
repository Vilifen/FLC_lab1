from .scanner import Scanner
from .parser import Parser
from .results_table import build_table_rows


def run_scanner(editor):
    text = editor.toPlainText()

    scanner = Scanner()
    tokens, lex_errors = scanner.scan(text)

    parser = Parser(tokens)
    syntax_errors = parser.parse()

    all_errors = lex_errors + syntax_errors
    token_rows, error_rows = build_table_rows(tokens, all_errors)

    return token_rows, error_rows
