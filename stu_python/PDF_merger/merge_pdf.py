import os
from pypdf import PdfWriter

def merge_pdfs(pdf_list, output_path):
    merger = PdfWriter()
    
    print("--- PDF結合ツール ---")
    for pdf in pdf_list:
        if os.path.exists(pdf):
            merger.append(pdf)
            print(f"追加成功: {pdf}")
        else:
            print(f"エラー: '{pdf}' が見つかりません。ファイル名を確認してください。")
            return # エラーがあったら結合をストップする

    # 結合したPDFを保存
    merger.write(output_path)
    merger.close()
    print(f"\n結合が完了しました！ 🎉")
    print(f"保存先: {output_path}")

if __name__ == "__main__":
    # ==========================================
    # 設定エリア：ここを自分のファイル名に変更！
    # ==========================================
    
    # 結合したいPDFファイルの名前（パス）を順番にリストに書きます
    input_pdfs = [
        "a.pdf", 
        "b.pdf"
    ]
    
    # 完成したPDFの保存名
    output_pdf = "merged.pdf"
    
    # ==========================================
    
    merge_pdfs(input_pdfs, output_pdf)