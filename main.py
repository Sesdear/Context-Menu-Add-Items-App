import sys
from PyQt6.QtWidgets import QApplication, QFrame, QMessageBox
import ContextMenuUI
import winreg as reg


class Window(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = ContextMenuUI.Ui_Frame()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.saveButton_click)

        self.folderWinregPath = r"Folder\shell"
        self.forallFilesWinregPath = r"*\shell"
        self.desktopWinregPath = r"Directory\Background\shell"
        self.driveWinregPath = r"Drive\shell"

    def saveButton_click(self):
        element_name = self.ui.elementNameLineEdit.text()
        command = self.ui.commandLineEdit.text()
        icon_path = self.ui.iconPathLineEdit.text()
        position = self.ui.positionLineEdit.text()
        location_index = self.ui.typeDirComboBox.currentIndex()

        if location_index == 0:
            path = self.folderWinregPath
        elif location_index == 1:
            path = self.forallFilesWinregPath
        elif location_index == 2:
            path = self.desktopWinregPath
        elif location_index == 3:
            path = self.driveWinregPath
        else:
            QMessageBox.warning(self, "Ошибка", "Не указано местоположение или расширение файла.")
            return

        try:
            reg_key = reg.CreateKeyEx(reg.HKEY_CLASSES_ROOT, f"{path}\\{element_name}", 0, reg.KEY_WRITE)
            reg.SetValueEx(reg_key, "MUIVerb", 0, reg.REG_SZ, element_name)

            if icon_path:
                reg.SetValueEx(reg_key, "Icon", 0, reg.REG_SZ, icon_path)
            if position:
                reg.SetValueEx(reg_key, "Position", 0, reg.REG_SZ, position)

            command_key = reg.CreateKeyEx(reg_key, "command", 0, reg.KEY_WRITE)
            reg.SetValueEx(command_key, "", 0, reg.REG_SZ, command)

            reg.CloseKey(command_key)
            reg.CloseKey(reg_key)

            QMessageBox.information(self, "Успех", "Элемент успешно добавлен в контекстное меню.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить элемент: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())