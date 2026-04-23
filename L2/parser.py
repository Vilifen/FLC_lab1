from .scan_error import ScanError
from .error_codes import ERROR_CODES
from .token_types import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.errors = []

    def parse(self, scanner_errors=None):
        self.pos = 0
        self.errors = []
        while not self._eof():
            self._skip_junk(check_semicolon=True)
            if self._eof(): break
            self.parse_while_stmt()
        return self.errors

    def _error(self, msg, tok=None):
        target = tok if tok else (self.tokens[self.pos] if not self._eof() else self.tokens[-1])
        if not target: return
        self.errors.append(ScanError(
            ERROR_CODES["INVALID_STRUCTURE"],
            f"Ошибка: {msg}",
            target.line, target.column, target.value
        ))

    def _skip_junk(self, check_semicolon=False):
        while not self._eof():
            tok = self.tokens[self.pos]
            if tok.type == TokenType.WHITESPACE:
                self.pos += 1
            elif tok.type == TokenType.UNKNOWN:
                self._error("недопустимый символ", tok)
                self.pos += 1
            elif check_semicolon and tok.value == ";":
                self._error("недопустимый символ", tok)
                self.pos += 1
            else:
                break

    def _match(self, expected_val, error_msg, check_semicolon=False):
        self._skip_junk(check_semicolon=check_semicolon)
        if self._eof():
            self._error(f"Ожидалось {error_msg}")
            return False

        tok = self.tokens[self.pos]
        if tok.value == expected_val or (isinstance(expected_val, list) and tok.value in expected_val):
            self.pos += 1
            return True

        if tok.type != TokenType.UNKNOWN:
            self._error(error_msg)
            self.pos += 1
        return False

    def parse_while_stmt(self):
        self._skip_junk(check_semicolon=True)
        if self._eof(): return

        if self.tokens[self.pos].value != "while":
            if self.tokens[self.pos].type != TokenType.UNKNOWN:
                self._error("ключевое слово 'while'")
            while not self._eof() and self.tokens[self.pos].value not in ["(", "{"]:
                self.pos += 1
                self._skip_junk(check_semicolon=True)
        else:
            self.pos += 1

        self._match("(", "'('", check_semicolon=True)
        self._skip_junk(check_semicolon=True)

        if not self._eof() and self.tokens[self.pos].type == TokenType.IDENTIFIER:
            self.pos += 1
        else:
            if not self._eof() and self.tokens[self.pos].type != TokenType.UNKNOWN:
                self._error("переменная '$id'")
                if self.tokens[self.pos].value not in ["<", ">", "==", "!=", "<=", ">="]:
                    self.pos += 1

        self._match(["<", ">", "==", "!=", "<=", ">="], "оператор сравнения", check_semicolon=True)
        self._skip_junk(check_semicolon=True)

        if not self._eof() and (self.tokens[self.pos].type in [TokenType.NUMBER, TokenType.IDENTIFIER]):
            self.pos += 1
        else:
            if not self._eof() and self.tokens[self.pos].type != TokenType.UNKNOWN:
                self._error("число или переменная")
                if self.tokens[self.pos].value != ")":
                    self.pos += 1

        self._match(")", "')'", check_semicolon=True)
        self._match("{", "'{'", check_semicolon=True)

        while not self._eof() and self.tokens[self.pos].value != "}":
            self._skip_junk(check_semicolon=True)
            if self._eof() or self.tokens[self.pos].value == "}": break

            if self.tokens[self.pos].type == TokenType.IDENTIFIER:
                self.pos += 1
                self._match(["++", "--"], "++ или --", check_semicolon=True)
                self._match(";", "';'")  # Здесь ';' законна
            else:
                if self.tokens[self.pos].type != TokenType.UNKNOWN and self.tokens[self.pos].value != ";":
                    self._error("инструкция")
                elif self.tokens[self.pos].value == ";":
                    self._error("недопустимый символ")
                self.pos += 1

        self._match("}", "'}'", check_semicolon=True)
        self._match(";", "';'")  # Здесь ';' законна

    def _eof(self):
        return self.pos >= len(self.tokens) or self.tokens[self.pos].type == TokenType.EOF