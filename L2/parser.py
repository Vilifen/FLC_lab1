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
            self._skip_noise()
            if self._eof(): break
            self.parse_while_stmt()
        return self.errors

    def _error(self, msg, tok):
        if self.errors and self.errors[-1].line == tok.line and self.errors[-1].column == tok.column:
            return
        self.errors.append(ScanError(
            ERROR_CODES["INVALID_STRUCTURE"],
            f"Ошибка: {msg}",
            tok.line, tok.column, tok.value
        ))

    def _skip_noise(self):
        while not self._eof() and self.tokens[self.pos].type == TokenType.WHITESPACE:
            self.pos += 1

    def _sync_expect(self, condition, error_msg):
        self._skip_noise()
        first_error_reported = False

        while not self._eof():
            tok = self.tokens[self.pos]

            is_match = False
            if callable(condition):
                is_match = condition(tok)
            elif isinstance(condition, list):
                is_match = tok.value in condition
            else:
                is_match = tok.value == condition or tok.type == condition

            if is_match:
                self.pos += 1
                return True

            if not first_error_reported:
                if tok.type == TokenType.UNKNOWN or tok.value == ";":
                    self._error("недопустимый символ", tok)
                else:
                    self._error(error_msg, tok)
                first_error_reported = True

            self.pos += 1
            self._skip_noise()

        return False

    def parse_while_stmt(self):
        self._sync_expect("while", "ключевое слово 'while'")
        self._sync_expect("(", "'('")

        self._skip_noise()
        if not self._eof():
            tok = self.tokens[self.pos]
            if tok.type == TokenType.IDENTIFIER:
                if not tok.value.startswith("$") or tok.value == "$":
                    self._error("переменная вида $i", tok)
                    self.pos += 1
                else:
                    self.pos += 1
            else:
                self._error("переменная вида $i", tok)
                if tok.value not in ["<", ">", "==", "!=", "<=", ">="]:
                    self.pos += 1

        self._sync_expect(["<", ">", "==", "!=", "<=", ">="], "оператор сравнения")

        self._skip_noise()
        if not self._eof():
            tok = self.tokens[self.pos]
            if tok.type in [TokenType.NUMBER, TokenType.IDENTIFIER]:
                self.pos += 1
            else:
                self._error("число или переменная", tok)
                if tok.value != ")":
                    self.pos += 1

        self._sync_expect(")", "')'")
        self._sync_expect("{", "'{'")

        while not self._eof():
            self._skip_noise()
            if self._eof() or self.tokens[self.pos].value == "}":
                break

            tok = self.tokens[self.pos]
            if tok.type == TokenType.IDENTIFIER:
                self.pos += 1
                self._skip_noise()
                next_tok = self.tokens[self.pos]
                if not self._eof() and next_tok.value in ["++", "--"]:
                    self.pos += 1
                else:
                    self._error("отсутствие инструкции ++ или --", next_tok)
                    if not self._eof() and next_tok.value != ";" and next_tok.type != TokenType.SEPARATOR:
                        self.pos += 1
                self._sync_expect(";", "';'")
            elif tok.value in ["++", "--"]:
                self._error("отсутствие переменной вида $i", tok)
                self.pos += 1
                self._sync_expect(";", "';'")
            else:
                self._error(
                    "недопустимый символ" if tok.type == TokenType.UNKNOWN or tok.value == ";" else "инструкция", tok)
                self.pos += 1

        self._sync_expect("}", "'}'")
        self._sync_expect(";", "';'")

    def _eof(self):
        return self.pos >= len(self.tokens) or self.tokens[self.pos].type == TokenType.EOF