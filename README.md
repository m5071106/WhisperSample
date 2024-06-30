## Whisper sample program with m3, macOS 14.5, Python 3.10.14

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

Installation instructions:
for macOS:
  Install homebrew
    https://brew.sh/ja/
  brew install python@3.10
  pip3 install -U openai-whisper
  brew install ffmpeg
  pip3 install ffmpeg-python
for Ubuntu:

for Windows:
  pip3 install -U openai-whisper
  Install ffmpeg
    https://taziku.co.jp/blog/windows-ffmpeg
      https://github.com/BtbN/FFmpeg-Builds/releases
        ffmpeg-master-latest-win640gpl.zip
  pip3 install ffmpeg-python
  pip3 install torch
  pip3 install torchvision
  pip3 install torchaudio
  pip3 uninstall numpy # 2.0.0 is not acceptable
  pip3 install numpy<2
  
  
