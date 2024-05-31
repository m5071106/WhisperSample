Whisper sample program with MacBook Pro 2023, m3, 16GB, macOS 14.5, Python 3.10.14
簡易版 (WhisperSample.py をターミナルで実行する)
1. WhisperSample.py 冒頭のコメントをもとに必要なモジュールを準備してください
2. sourceフォルダに音声ファイルを格納してください。対象拡張子はextensions.txtで制御します。
3. python3 WhisperSample.py [model1] [model2] ...
   で変換を開始します。modelには、tiny, base, small, medium, large を指定します。並べた数だけ変換されます。
4. resultフォルダに音声ファイル名+モデル名のテキストが格納されます。