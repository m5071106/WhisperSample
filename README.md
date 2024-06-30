## Whisper sample program with m3, macOS 14.5, Python 3.10.14

### 簡易版 (sound_trans.py をターミナルで実行する)

1. sourceフォルダに音声ファイルを格納してください。対象拡張子はextensions.txtで制御します。
1. python3 sound_trans.py [model1] [model2] ...
   で変換を開始します。modelには、tiny, base, small, medium, large を指定します。並べた数だけ変換されます。
1. resultフォルダに音声ファイル名+モデル名のテキストが格納されます。

### Web版 (front_web.py をターミナルで実行後、Web Browser で http://[hostname]:5001/でアクセス)

1. python3 front_web.py でwebを起動します。サンプルはsmallモデルに限定しています。
1. http://[hostname]:5001/ でアクセスします。
1. ファイルをアップロードし、モデルを選択後、変換ボタン選択で処理が始まります。
1. 結果がWeb上に表記されます。./result/フォルダを別の静的webでディレクトリが見られるよう設定することで変換結果をダウンロードします。

### Installation instructions:
#### for macOS:
  1. Install homebrew (https://brew.sh/ja/)
  1. brew install python@3.10
  1. pip3 install -U openai-whisper
  1. brew install ffmpeg
  1. pip3 install ffmpeg-python
  1. pip3 install torch
  1. pip3 install torchvision
  1. pip3 install torchaudio

#### for Ubuntu:
  1. pip3 install whisper
  1. pip3 install git+https://github.com/openai/whisper.git
  1. pip3 install ffmpeg-python
  1. pip3 install -U openai-whisper
  1. sudo apt install ffmpeg (https://github.com/openai/whisper#)
  1. pip3 --no-cache-dir install torch (通常だとkilledされる)
  1. pip3 install torchvision

#### for Windows:
  1. pip3 install -U openai-whisper
  1. Install ffmpeg (https://github.com/BtbN/FFmpeg-Builds/releases)
  1. pip3 install ffmpeg-python
  1. pip3 install torch
  1. pip3 install torchvision
  1. pip3 install torchaudio
  1. pip3 uninstall numpy # 2.0.0 is not acceptable
  1. pip3 install numpy<2
  
  
