## Whisper sample program with MacBook Pro 2023, m3, 16GB, macOS 14.5, Python 3.10.14

### 簡易版 (sound_trans.py をターミナルで実行する)

1. sound_trans.py 冒頭のコメントをもとに必要なモジュールを準備してください
2. sourceフォルダに音声ファイルを格納してください。対象拡張子はextensions.txtで制御します。
3. python3 sound_trans.py [model1] [model2] ...
   で変換を開始します。modelには、tiny, base, small, medium, large を指定します。並べた数だけ変換されます。
4. resultフォルダに音声ファイル名+モデル名のテキストが格納されます。

### Web版 (front_web.py をターミナルで実行後、Web Browser で http://[hostname]:5001/でアクセス)

1. sound_trans.py 冒頭のコメントをもとに必要なモジュールを準備してください
2. python3 front_web.py でwebを起動します。サンプルはsmallモデルに限定しています。
3. http://[hostname]:5001/ でアクセスします。
4. ファイルをアップロードし、モデルを選択後、変換ボタン選択で処理が始まります。
5. 結果がWeb上に表記されます。./result/フォルダを別の静的webでディレクトリが見られるよう設定することで変換結果をダウンロードします。
