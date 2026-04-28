import os
import sys
from PyQt6.QtWidgets import (
    QMainWindow, QMessageBox, QStatusBar, QDialog,
    QVBoxLayout, QTextBrowser, QWidget, QSplitter
)
from PyQt6.QtCore import QUrl, Qt, QFile, QTextStream, QIODevice, QStringConverter
from PyQt6.QtGui import QFont

from ui.central.central_widget import CentralWidget
from ui.actions import ActionManager
from ui.menus import MenuBuilder
from ui.toolbar import ToolbarBuilder

from L2.integration import run_scanner
from L2.navigation import navigate_to_error
from ANTLR.antlr_handler import execute_antlr_analysis

def get_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()

        self.labels_ru = {
            "file": "Файл", "edit": "Правка", "text": "Текст", "run": "Пуск",
            "help": "Справка", "localization": "Локализация", "view": "Вид",
            "font_size": "Размер шрифта", "new": "Создать", "open": "Открыть",
            "save": "Сохранить", "save_as": "Сохранить как", "exit": "Выход",
            "undo": "Отменить", "redo": "Повторить", "cut": "Вырезать",
            "copy": "Копировать", "paste": "Вставить", "delete": "Удалить",
            "select_all": "Выделить всё", "task": "Постановка задачи",
            "grammar": "Грамматика", "grammar_class": "Классификация грамматики",
            "method": "Метод анализа", "example": "Тестовый пример",
            "literature": "Список литературы", "source": "Исходный код программы",
            "about": "О программе", "info_title": "Информация",
            "error_label": "Ошибка", "forbidden_word": "Ошибка",
            "line_word": "строка", "pos_word": "позиция",
            "no_errors": "Ошибок не найдено.", "help_text": "Справка",
            "about_text": "О программе", "save_title": "Сохранить файл?",
            "save_text": "Сохранить изменения в файле", "yes": "Да", "no": "Нет",
            "cancel": "Отмена", "status_lang": "Язык", "status_size": "Размер",
            "status_lines": "Строк", "build": "Сборка", "errors": "Ошибки",
        }

        self.labels_en = {
            "file": "File", "edit": "Edit", "text": "Text", "run": "Run",
            "help": "Help", "localization": "Language", "view": "View",
            "font_size": "Font size", "new": "New", "open": "Open",
            "save": "Save", "save_as": "Save As", "exit": "Exit",
            "undo": "Undo", "redo": "Redo", "cut": "Cut", "copy": "Copy",
            "paste": "Paste", "delete": "Delete", "select_all": "Select All",
            "task": "Task", "grammar": "Grammar", "grammar_class": "Grammar classification",
            "method": "Parsing method", "example": "Example", "literature": "References",
            "source": "Source code", "about": "About", "info_title": "Information",
            "error_label": "Error", "forbidden_word": "Error", "line_word": "line",
            "pos_word": "position", "no_errors": "No errors found.",
            "help_text": "Help", "about_text": "About", "save_title": "Save file?",
            "save_text": "Save changes to file", "yes": "Yes", "no": "No",
            "cancel": "Cancel", "status_lang": "Lang", "status_size": "Size",
            "status_lines": "Lines", "build": "Build", "errors": "Errors",
        }

        self.labels = self.labels_ru
        self.language = "ru"
        self.font_menu = None

        self.setWindowTitle("Текстовый редактор")
        self.resize(1000, 700)
        self.menuBar().setNativeMenuBar(False)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.central = CentralWidget()

        splitter = QSplitter(Qt.Orientation.Vertical)
        splitter.addWidget(self.central.editor_area)
        splitter.addWidget(self.central.results_area)
        splitter.setSizes([600, 300])
        splitter.setHandleWidth(6)

        container = QWidget()
        container.setObjectName("main_container")
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(splitter)

        self.error_status = QStatusBar()
        layout.addWidget(self.error_status)

        self.setCentralWidget(container)

        self.actions = ActionManager(self, controller)
        self.menu_builder = MenuBuilder(self, self.actions)
        ToolbarBuilder(self, self.actions)

        self._build_font_menu()
        self.central.editor.textChanged.connect(self.update_status_bar)

        self.setStyleSheet("""
            QMainWindow, QWidget#main_container { background-color: white; }
            QMenuBar { background-color: white; color: black; border-bottom: 1px solid #dcdcdc; }
            QMenuBar::item:selected { background-color: #e0e0e0; }
            QMenu { background-color: white; color: black; border: 1px solid #dcdcdc; }
            QMenu::item:selected { background-color: #0078d7; color: white; }
            QStatusBar { background-color: white; color: black; border-top: 1px solid #dcdcdc; }
            QSplitter::handle { background-color: #f0f0f0; }
        """)

    def set_language(self, lang):
        self.labels = self.labels_en if lang == "en" else self.labels_ru
        self.language = lang
        self.actions.update_texts()
        self.menu_builder.update_menu_titles()
        if self.font_menu:
            self.font_menu.setTitle(self.labels["font_size"])
        self.update_ui_language()
        self.update_status_bar()

    def update_ui_language(self):
        if hasattr(self.central, 'build_btn'): self.central.build_btn.setText(self.labels["build"])
        if hasattr(self.central, 'err_btn'): self.central.err_btn.setText(self.labels["errors"])
        headers = ["Code", "Type", "Lexeme", "Location"] if self.language == "en" else ["Код", "Тип", "Лексема", "Местоположение"]
        self.central.table.setHorizontalHeaderLabels(headers)

    def set_font_size(self, size):
        editor = self.get_editor()
        if editor:
            font = editor.font()
            font.setPointSize(size)
            editor.setFont(font)

    def run_scanner_action(self):
        editor = self.central.editor
        token_rows, error_rows = run_scanner(editor)
        self.central.set_results(token_rows, error_rows)
        self.error_status.showMessage(f"Ошибок: {len(error_rows)}")
        self._connect_table_navigation(editor)

    def run_antlr_action(self):
        editor = self.central.editor
        text = editor.toPlainText()
        token_rows, all_errors = execute_antlr_analysis(text)
        self.central.set_results(token_rows, all_errors)
        self.error_status.showMessage(f"Ошибок ANTLR: {len(all_errors)}")
        self._connect_table_navigation(editor)

    def _connect_table_navigation(self, editor):
        def on_click(item):
            row = item.row()
            rows = self.central.token_rows if self.central.output_mode == "build" else self.central.error_rows
            if 0 <= row < len(rows):
                navigate_to_error(editor, rows[row]["line"], rows[row]["col"])
        try:
            self.central.table.itemClicked.disconnect()
        except:
            pass
        self.central.table.itemClicked.connect(on_click)

    def _show_html_dialog(self, title_key, file_name):
        dlg = QDialog(self)
        dlg.setWindowTitle(self.labels.get(title_key, "Info"))
        dlg.resize(1000, 800)
        layout = QVBoxLayout(dlg)
        browser = QTextBrowser()
        layout.addWidget(browser)
        path = get_path(f"ui/html files/{file_name}")
        file = QFile(path)
        if file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            stream = QTextStream(file)
            stream.setEncoding(QStringConverter.Encoding.Utf8)
            content = stream.readAll()
            file.close()
            browser.setHtml(content)
        dlg.exec()

    def show_help(self): self._show_html_dialog("help_text", "user_guide.html")
    def show_grammar(self): self._show_html_dialog("grammar", "Grammar.html")
    def show_grammar_class(self): self._show_html_dialog("grammar_class", "ClassificationOfGrammar.html")
    def show_method(self): self._show_html_dialog("method", "MethodOfAnalysis.html")
    def show_test_example(self): self._show_html_dialog("example", "Test.html")
    def show_references(self): self._show_html_dialog("literature", "References.html")
    def show_source_code(self): self._show_html_dialog("source", "Program.html")
    def show_problem_statement(self): self._show_html_dialog("task", "problemStatement.html")

    def _build_font_menu(self):
        view_menu = None
        for act in self.menuBar().actions():
            if act.text() == self.labels["view"] or (act.menu() and act.menu().title() == self.labels["view"]):
                view_menu = act.menu()
                break
        if not view_menu: return
        self.font_menu = view_menu.addMenu(self.labels["font_size"])
        for size in [8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 48, 72]:
            action = self.font_menu.addAction(str(size))
            action.triggered.connect(lambda _, s=size: self.set_font_size(s))

    def update_status_bar(self):
        text = self.central.editor.toPlainText()
        size = len(text.encode("utf-8"))
        lines = text.count("\n") + 1
        self.status.showMessage(f"{self.labels['status_lang']}: {self.language.upper()} | {self.labels['status_size']}: {size} B | {self.labels['status_lines']}: {lines}")

    def get_editor(self): return self.central.editor
    def get_output(self): return self.central.table