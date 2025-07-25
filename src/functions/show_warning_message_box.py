from PyQt5.QtWidgets import QMessageBox

def show_warning_message_box(text_message:str):
    message = QMessageBox()
    message.setIcon(QMessageBox.Icon.Warning)
    message.setText(text_message)
    message.setStandardButtons(QMessageBox.StandardButton.Close)
    message.exec()