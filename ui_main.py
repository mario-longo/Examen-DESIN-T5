from PySide6.QtWidgets import (QVBoxLayout, QHBoxLayout, QLineEdit, 
                             QPushButton, QListWidget, QWidget)
from PySide6.QtCore import Qt

class TodoUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
        MainWindow.setWindowTitle("Lista de Tareas")
        
        # Estilo Global Moderno
        MainWindow.setStyleSheet("""
            QMainWindow { background-color: #1e1e2e; }
            QWidget { color: #cdd6f4; font-family: 'Segoe UI', Arial; font-size: 14px; }
            QLineEdit { 
                background-color: #313244; border: 2px solid #45475a; 
                border-radius: 8px; padding: 10px; color: white;
            }
            QLineEdit:focus { border: 2px solid #89b4fa; }
            QPushButton { 
                background-color: #89b4fa; color: #11111b; 
                border-radius: 8px; padding: 10px; font-weight: bold; 
            }
            QPushButton:hover { background-color: #b4befe; }
            QPushButton#deleteBtn { background-color: #f38ba8; }
            QPushButton#deleteBtn:hover { background-color: #eba0ac; }
            QListWidget { 
                background-color: #313244; border-radius: 12px; 
                border: none; outline: none; padding: 5px;
            }
            QListWidget::item {
                background-color: #45475a; border-radius: 6px;
                margin: 4px; padding: 10px;
            }
        """)

        self.central_widget = QWidget(MainWindow)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)

        self.input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("¿Qué tienes pendiente?")
        self.add_button = QPushButton("Añadir")
        
        self.input_layout.addWidget(self.task_input)
        self.input_layout.addWidget(self.add_button)

        self.task_list = QListWidget()
        self.delete_button = QPushButton("Limpiar tareas completadas")
        self.delete_button.setObjectName("deleteBtn")

        self.layout.addLayout(self.input_layout)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.delete_button)

        MainWindow.setCentralWidget(self.central_widget)