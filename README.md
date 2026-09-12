# Study Log
大学及び個人での学習を通じて
情報工学・AI・Pythonなどを学んだ過程を記録しています。

# About
このリポジトリは、大学での学習や個人的な学習において学んだ内容・実装したコード・考えたことを記録するためのStudy Logです。
単にコードを保存するだけでなく、「なぜその技術を使うのか/自分はどのように理解したか/実際にコードとしてどう実装したか」を残すことを意識しています。

## What I'm Learning
現在、以下の分野を中心に学習を進めています。

### AI / Machine Learning
- 画像認識
- CNN
- PyTorch
- MobileNet
- 損失関数
- 勾配降下法
- 最適化アルゴリズム

### Python
- Pythonの基礎
- Pandas
- データ処理
- ファイル操作
- 自動化

### LLM
- LLMの基礎
- RAG
- Embedding
- ベクトル検索

### Software Development
- Git / Github
- REST API
- Flutter / Dart
- TypeScript
- React / Next.js
- Node.js

>※このリストは学習中の技術を含みます。

## Repository Structure
```text
study_for/
├── image_recognition_AI/
│   ├── dataset/
│   ├── dataset.py
│   ├── train.py
│   └── image_acquisition.py
│
├── stu_python/
│   ├── PDF_merger/
│   └── image_recognition_AI_study/
│       ├── study_1.py
│       ├── study_1_memo.txt
│       ├── study_2.py
│       └── ...
│
└── README.md
```

**image_recognition_AI**
画像認識AIの実装,ロボット作成に使用する部品をWebカメラで識別し関連情報やすよう方法を確認できるツールを作成中。

**stu_python**
pythonを中心とした学習記録。

**image_recognition_AI_study**
画像認識AIを学習する過程で作成したコードと自分なりの理解をまとめたメモ。

## Learnong Phylosophy
「ライブラリを使って動かせる」で終わらせず、その処理がなぜその働きをするのかを理解することを意識しています。例えば画像認識AI学習では、
数式 -> アルゴリズム -> コード -> 実際のモデル
という流れを意識して学習しています
学習中に生まれた疑問や自分なりの解釈を'.txt'ファイルにメモとして残しています。
また、大学で学んだ線形代数,微分方程式,確率,最適化などが実際のAI技術のなかでどのように使われているのかを確認しながら学習しています。

## Future Plans
今後は学習した知識を実際のアプリケーションやハードウェアと組み合わせることを目標としています。

- 画像認識AIのリアルタイム推論
- 実際のロボット部品を対象とした画像認識
- Pandasを利用したデータ分析
- AIを利用したアプリケーション開発
- LLM / RAGを利用したシステム開発
- AIとロボットを組み合わせた開発

学習だけで終わらせず、「実際に使えるものを作る」ことを意識して開発を進めていきます。

## Note
このリポジトリには学習途中のコードも含まれています。そのためコード尾の中には実験的な実装や後から修正される可能性のある内容が含まれます。学習の過程そのものを記録することを目的としているため、完成されたライブラリや部品コードとは異なる構成になっています。