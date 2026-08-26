import sys
import os
from pypdf import PdfWriter, PdfReader
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QFileDialog, QListWidget

class PDFMergerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("俺のためのPDF結合マン")
        self.resize(400, 300)
        self.label = QLabel("ここに結合したいPDFファイルをドラッグ&ドロップ")
        self.list_widget = QListWidget()
        self.add_button = QPushButton("ファイルを追加する")
        self.merge_button = QPushButton("選択したファイルを結合する")
        self.add_button.clicked.connect(self.on_button_clicked)
        self.merge_button.clicked.connect(self.on_merge_clicked)

        self.target_files = []

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.add_button)
        layout.addWidget(self.merge_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_clicked(self):
        self.label.setText("ファイルを追加")
        print("ボタン押下を検知")
        file_paths, _ = QFileDialog.getOpenFileNames(self, "ファイルを開く", "", "PDFファイル (*.pdf)")
        print(file_paths)
        for path in file_paths:
            self.target_files.append(path)
            self.list_widget.addItem(os.path.basename(path))

    def on_merge_clicked(self):
        if len(self.target_files) < 2:
            print("エラー:結合する対象ファイルは2つ以上必要です.")
            self.label.setText("ファイルが足りません!")
            return

        save_path, _ = QFileDialog.getSaveFileName(self, "保存先を選択する", "merged.pdf", "PDFファイル (*.pdf)")

        if save_path:
            merger = PdfWriter()

            for path in self.target_files:
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
