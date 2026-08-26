import sys
import os
from pypdf import PdfWriter, PdfReader
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QListWidget, QListWidgetItem
from PySide6.QtCore import Qt

class PDFMergerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)

        self.setWindowTitle("俺のためのPDF結合マン")
        self.resize(700, 500)
        self.label = QLabel("ここに結合したいPDFファイルをドラッグ&ドロップ")
        self.recognition_label = QLabel("選択したファイルをドラッグし順番を入れ替えることができます")
        self.list_widget = QListWidget()
        self.list_widget.setDragDropMode(QListWidget.InternalMove)
        self.add_button = QPushButton("ファイルを追加する")
        self.delete_button = QPushButton("選択したファイルを削除する")
        self.merge_button = QPushButton("選択したファイルを結合する")
        self.delete_button.clicked.connect(self.on_delete_clicked)
        self.add_button.clicked.connect(self.on_button_clicked)
        self.merge_button.clicked.connect(self.on_merge_clicked)

        self.target_files = []

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.recognition_label)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.add_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.merge_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_file_to_list(self, path):
        if path.lower().endswith('.pdf'):
            item = QListWidgetItem(os.path.basename(path))
            item.setData(Qt.UserRole, path)
            self.list_widget.addItem(item)
        else:
            print(f"スキップされました。{path}はPDFではありません。")

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            self.add_file_to_list(path)

    def on_button_clicked(self):
        self.label.setText("ファイルを追加")
        print("ボタン押下を検知")
        file_paths, _ = QFileDialog.getOpenFileNames(self, "ファイルを開く", "", "PDFファイル (*.pdf)")
        print(file_paths)
        for path in file_paths:
            self.add_file_to_list(path)

    def on_delete_clicked(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            row = self.list_widget.row(item)
            self.list_widget.takeItem(row)


    def on_merge_clicked(self):
        count = self.list_widget.count()
        if count < 2:
            print("エラー:結合する対象ファイルは2つ以上必要です.")
            self.label.setText("ファイルが足りません!")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "保存先を選択する", "merged.pdf", "PDFファイル (*.pdf)")

        if save_path:
            merger = PdfWriter()

            for i in range(count):
                item = self.list_widget.item(i)
                path = item.data(Qt.UserRole)
                reader = PdfReader(path)
                merger.append(reader)

            merger.write(save_path)

            merger.close()

            self.label.setText(f"ファイル結合完了！: {os.path.basename(save_path)}")
            print(f"保存完了: {save_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFMergerApp()
    window.show()
    sys.exit(app.exec())
