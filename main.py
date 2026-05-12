import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtCore import Qt
from ui_main import TodoUI
from logic import TodoLogic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Configurar la Interfaz
        self.ui = TodoUI()
        self.ui.setupUi(self)
        
        # 2. Configurar la Lógica
        self.logic = TodoLogic()

        # 3. Conectar Botones y Eventos
        self.ui.add_button.clicked.connect(self.handle_add_task)
        self.ui.task_input.returnPressed.connect(self.handle_add_task)
        self.ui.delete_button.clicked.connect(self.handle_delete_completed)
        
        # Conectar el cambio de estado (check/uncheck)
        self.ui.task_list.itemChanged.connect(self.handle_status_change)

    def handle_add_task(self):
        text = self.ui.task_input.text().strip()
        task = self.logic.add_task(text)
        
        if task:
            # Bloqueamos señales para que añadir el item no dispare 'itemChanged' accidentalmente
            self.ui.task_list.blockSignals(True)
            
            item = QListWidgetItem(task["text"])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            self.ui.task_list.addItem(item)
            
            self.ui.task_list.blockSignals(False)
            self.ui.task_input.clear()

    def handle_status_change(self, item):
        # Sincronizar con la lógica
        index = self.ui.task_list.row(item)
        if index < len(self.logic.tasks):
            is_checked = item.checkState() == Qt.Checked
            self.logic.tasks[index]["completed"] = is_checked
            
            # Efecto visual de tachado
            font = item.font()
            font.setStrikeOut(is_checked)
            item.setFont(font)
            item.setForeground(Qt.gray if is_checked else Qt.white)

    def handle_delete_completed(self):
        # Limpiar lógica
        self.logic.clear_completed()
        
        # Limpiar UI (recorremos de atrás hacia adelante para no romper los índices)
        self.ui.task_list.blockSignals(True)
        for i in range(self.ui.task_list.count() - 1, -1, -1):
            if self.ui.task_list.item(i).checkState() == Qt.Checked:
                self.ui.task_list.takeItem(i)
        self.ui.task_list.blockSignals(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())