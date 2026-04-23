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
            self._skip_junk()
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

    def _skip_junk(self):
        while not self._eof():
            tok = self.tokens[self.pos]
            if tok.type == TokenType.WHITESPACE:
                self.pos += 1
            elif tok.type == TokenType.UNKNOWN:
                self.errors.append(ScanError(
                    ERROR_CODES["INVALID_STRUCTURE"],
                    "Ошибка: недопустимый символ",
                    tok.line, tok.column, tok.value
                ))
                self.pos += 1
            else:
                break

    def _match(self, expected_val, error_msg):
        self._skip_junk()
        if self._eof():
            self._error(f"Ожидалось {error_msg}")
            return False
        tok = self.tokens[self.pos]
        if tok.value == expected_val or (isinstance(expected_val, list) and tok.value in expected_val):
            self.pos += 1
            return True
        self._error(error_msg)
        self.pos += 1
        return False

    def parse_while_stmt(self):
        if self.tokens[self.pos].value != "while":
            self._error("ключевое слово 'while'")
            while not self._eof() and self.tokens[self.pos].value not in ["(", "{"]:
                self._skip_junk()
                if self._eof() or self.tokens[self.pos].value in ["(", "{"]: break
                self.pos += 1
        else:
            self.pos += 1

        self._match("(", "'('")
        self._skip_junk()
        if not self._eof() and self.tokens[self.pos].type == TokenType.IDENTIFIER:
            self.pos += 1
        else:
            self._error("переменная '$id'")
            if not self._eof() and self.tokens[self.pos].value not in ["<", ">", "==", "!=", "<=", ">="]:
                self.pos += 1

        self._match(["<", ">", "==", "!=", "<=", ">="], "оператор сравнения")
        self._skip_junk()
        if not self._eof() and (self.tokens[self.pos].type in [TokenType.NUMBER, TokenType.IDENTIFIER]):
            self.pos += 1
        else:
            self._error("число или переменная")
            if not self._eof() and self.tokens[self.pos].value != ")":
                self.pos += 1

        self._match(")", "')'")
        self._match("{", "'{'")

        while not self._eof() and self.tokens[self.pos].value != "}":
            self._skip_junk()
            if self._eof() or self.tokens[self.pos].value == "}": break
            if self.tokens[self.pos].type == TokenType.IDENTIFIER:
                self.pos += 1
                self._match(["++", "--"], "++ или --")
                self._match(";", "';'")
            else:
                self._error("инструкция")
                self.pos += 1

        self._match("}", "'}'")
        self._match(";", "';'")

    def _eof(self):
        return self.pos >= len(self.tokens) or self.tokens[self.pos].type == TokenType.EOF