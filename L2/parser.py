from .scan_error import ScanError
from .error_codes import ERROR_CODES
from .token_types import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.errors = []
        self.top_level_while_error_reported = False

    def parse(self):
        while not self._eof():
            self._skip_whitespace()
            if self._eof():
                break
            self._parse_top_level_statement()
        return self.errors

    def _parse_top_level_statement(self):
        tok = self._cur()

        if tok.type == TokenType.KEYWORD and tok.value == "while":
            self._advance()
            self._parse_while()
            return

        if not self.top_level_while_error_reported:
            self._error("Ожидалось ключевое слово 'while'")
            self.top_level_while_error_reported = True
        else:
            self._advance()

    def _parse_while(self):
        self._skip_whitespace()
        if not self._match(TokenType.SEPARATOR, "("):
            self._error("Ожидалась '(' после while")

        self._skip_whitespace()
        self._skip_expression()

        self._skip_whitespace()
        if not self._match(TokenType.SEPARATOR, ")"):
            self._error("Ожидалась ')' после условия while")

        self._skip_whitespace()
        if not self._match(TokenType.SEPARATOR, "{"):
            self._error("Ожидался '{' после while(...)")

        self._parse_block()

        self._skip_whitespace()
        if not self._match(TokenType.SEPARATOR, ";"):
            self._error("Ожидался ';' после блока while")

    def _parse_block(self):
        depth = 1
        while not self._eof() and depth > 0:
            self._skip_whitespace()
            tok = self._cur()

            if tok.type == TokenType.SEPARATOR and tok.value == "{":
                depth += 1
                self._advance()
                continue

            if tok.type == TokenType.SEPARATOR and tok.value == "}":
                depth -= 1
                self._advance()
                continue

            if depth == 1:
                self._parse_inner_statement()
            else:
                self._advance()

    def _parse_inner_statement(self):
        self._skip_whitespace()
        if self._eof():
            return

        tok = self._cur()

        if tok.type == TokenType.KEYWORD and tok.value == "while":
            self._advance()
            self._parse_while()
            return

        while not self._eof():
            tok = self._cur()

            if tok.type == TokenType.SEPARATOR and tok.value == ";":
                self._advance()
                return

            if tok.type == TokenType.SEPARATOR and tok.value == "}":
                self._error("Ожидался ';' перед '}'")
                return

            self._advance()

        self._error("Ожидался ';' в конце выражения")

    def _skip_expression(self):
        while not self._eof():
            tok = self._cur()
            if tok.type == TokenType.SEPARATOR and tok.value == ")":
                return
            self._advance()

    def _match(self, ttype, value=None):
        if self._eof():
            return False
        tok = self._cur()
        if tok.type == ttype and (value is None or tok.value == value):
            self._advance()
            return True
        return False

    def _skip_whitespace(self):
        while not self._eof() and self._cur().type == TokenType.WHITESPACE:
            self._advance()

    def _cur(self):
        return self.tokens[self.pos]

    def _advance(self):
        if not self._eof():
            self.pos += 1

    def _eof(self):
        return self.pos >= len(self.tokens) or self.tokens[self.pos].type == TokenType.EOF

    def _error(self, msg):
        tok = self._cur()
        code = ERROR_CODES["INVALID_STRUCTURE"]
        self.errors.append(ScanError(code, msg, tok.line, tok.column, tok.value))
        self._advance()
