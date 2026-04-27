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
        self.tokens = [t for t in self.tokens if t.type != TokenType.WHITESPACE]
        self.parse_start()
        return self.errors

    def _error(self, msg, tok):
        if self.errors and self.errors[-1].line == tok.line and self.errors[-1].column == tok.column:
            return
        self.errors.append(ScanError(
            ERROR_CODES["INVALID_STRUCTURE"],
            f"Ошибка: {msg}",
            tok.line, tok.column, tok.value
        ))

    def _sync_expect(self, condition, error_msg, next_condition):
        tok = self.tokens[self.pos]

        is_match = False
        if callable(condition):
            is_match = condition(tok)
        elif isinstance(condition, list):
            is_match = tok.value in condition or tok.type in condition
        else:
            is_match = tok.value == condition or tok.type == condition

        if is_match:
            self.pos += 1
            return True

        self._error(error_msg, tok)

        while not self._eof():
            tok = self.tokens[self.pos]

            is_match = False
            if callable(next_condition):
                is_match = next_condition(tok)
            elif isinstance(next_condition, list):
                is_match = tok.value in next_condition or tok.type in next_condition
            else:
                is_match = tok.value == next_condition or tok.type == next_condition

            if is_match:
                return True

            self.pos += 1

        return False

    def parse_start(self):
        if self._sync_expect("while", "Ожидалось ключевое слово while", "("):
            self.parse_keyword_while()

    def parse_keyword_while(self):
        if self._sync_expect("(", "Ожидалась '('", TokenType.IDENTIFIER):
            self.parse_left_brace()

    def parse_left_brace(self):
        if self._sync_expect(TokenType.IDENTIFIER, "Ожидался идентификатор", ["<", ">", "==", "!=", "<=", ">="]):
            self.parse_identifier()

    def parse_identifier(self):
        if self._sync_expect(["<", ">", "==", "!=", "<=", ">="], "Ожидался оператор сравнения", [TokenType.NUMBER, TokenType.IDENTIFIER]):
            self.parse_expression()

    def parse_expression(self):
        if self._sync_expect([TokenType.NUMBER, TokenType.IDENTIFIER], "Ожидалось число или идентификатор", ["&&", "||", ')']):
            self.parse_right_operand()

    def parse_right_operand(self):
        tok = self.tokens[self.pos]
        if tok.value == "&&" or tok.value == "||":
            self.pos+=1;
            self.parse_left_brace()
        elif tok.value == ')':
            self.pos+=1;
            self.parse_right_brace()
        else:
            tmp_pos = self.pos
            while tok.value != '{' and not self._eof():
                tok = self.tokens[self.pos]
                self.pos+=1;
            if (tok.value == "{" or self._eof()):
                self._error("Ожидалась ')'", self.tokens[tmp_pos])
            self.parse_right_brace()

    def parse_right_brace(self):
        if self._sync_expect("{", "Ожидалась '{'", TokenType.IDENTIFIER):
            self.parse_left_curly_brace()

    def parse_left_curly_brace(self):
        if self._sync_expect(TokenType.IDENTIFIER, "Ожидался идентификатор", ["++", "--"]):
            self.parse_id_in()

    def parse_id_in(self):
        if self._sync_expect(["++", "--"], "Ожидался оператор изменения", ";"):
            self.parse_operator_change()

    def parse_operator_change(self):
        if self._sync_expect(";", "Ожидалась ';'", [TokenType.IDENTIFIER, "}"]):
            self.parse_semicolon_in()

    def parse_semicolon_in(self):
        tok = self.tokens[self.pos]
        if tok.type == TokenType.IDENTIFIER:
            self.pos+=1;
            self.parse_id_in()
        elif tok.value == '}':
            self.pos+=1;
            self.parse_right_curly_brace()
        else:
            tmp_pos = self.pos
            while tok.value != ';' and not self._eof():
                tok = self.tokens[self.pos]
                self.pos+=1;
            if (tok.value == ";" or self._eof()):
                self._error("Ожидалась '}'", self.tokens[tmp_pos])
            self.parse_right_curly_brace()

    def parse_right_curly_brace(self):
        if self._sync_expect(";", "Ожидалась ';'", ";"):
            if not self._eof():
                self.parse_start()

    def _eof(self):
        return self.pos >= len(self.tokens) or self.tokens[self.pos].type == TokenType.EOF