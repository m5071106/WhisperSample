# MacBook Pro 2023, m3, 16GB, macOS 14.5, Python 3.10.14 にて動作確認
# 事前準備
# homebrew インストール
#   https://brew.sh/ja/
#   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# python 3.10.x をインストール後、homebrew へのパスを通す
#   brew install python@3.10
#   export PATH="/opt/homebrew/bin/:$PATH"
# 関連モジュールのインストール
#   pip3 install -U openai-whisper
#   brew install ffmpeg
#   pip3 install ffmpeg-python
# 音声認識対象のファイルをsourceディレクトリに格納(拡張子はm4aまたはmp3など、ffmpegで変換可能なもの[プログラム内で指定]
import whisper
import os

# 対象拡張子
extensions = ('mp3','m4a')
modelarray = ['base', 'small']  # Whisperモデルの配列. 右記から変換したい形式を指定 ['tiny', 'base', 'small', 'medium', 'large']
resultarray = []
resultfilearray = []

# 入出力ディレクトリのパス
source_dir = './source'
result_dir = './result'
# sourceディレクトリ内のファイル一覧を取得
file_list = os.listdir(source_dir)

# 認識対象の拡張子のファイルのみを抽出し、変換を行う
for filename in file_list:
    if any(extension in filename for extension in extensions):
        print(f'{filename}の音声認識を開始')
        # modelarray分繰り返す
        for currentmodel in modelarray:
            print(f'Using the {currentmodel} model')
            # Whisperモデルをロードする
            model = whisper.load_model(currentmodel)
            # 変換
            result = model.transcribe(f'{source_dir}/{filename}')
            # 結果出力配列に変換後データを追加
            resultarray.append(f'----------- {filename}' + '-' + f'{currentmodel} -----------' + '\n' + result['text'])
            # 変換後のファイル名を作成
            converted_filename = filename
            for extension in extensions:
                converted_filename = converted_filename.replace('.' + extension, '')
            # 結果出力配列に変換後のファイル名を追加
            resultfilearray.append(f'{converted_filename}-{currentmodel}.txt')

# 結果出力
index = 0
for i in resultarray:
    print(resultfilearray[index])
    print(i)
    # resultフォルダ内にファイルを作成し、結果を書き込む(ファイル名-Whisperモデル名.txt)
    with open(f'{result_dir}/{resultfilearray[index]}', mode='w+') as f:
        f.write(i)
    index += 1
