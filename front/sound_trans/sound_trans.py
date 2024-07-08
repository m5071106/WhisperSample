from pathlib import Path

import whisper
import os
import sys
import datetime


def sound_transcription(modelarray=['medium']):

    # 現在のディレクトリを取得
    current_dir = os.path.dirname(__file__)

    # 対象拡張子の読み込み
    with open(current_dir + '/resources/extensions.txt', 'r') as file:
        extensions = file.read().splitlines()

    # 結果出力配列
    resultarray = []
    resultfilearray = []

    # 入出力ディレクトリのパス
    source_dir = current_dir + '/' + Path(current_dir + '/resources/source.txt').read_text().strip()
    result_dir = current_dir + '/' + Path(current_dir + '/resources/result.txt').read_text().strip()
    backup_dir = current_dir + '/backup'

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # sourceディレクトリ内のファイル一覧を取得
    file_list = os.listdir(source_dir)

    # 変換時刻を取得
    datetimenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    # 認識対象の拡張子のファイルのみを抽出し、変換を行う
    for filename in file_list:
        if any(extension in filename for extension in extensions):
            print(f'{filename} conversion started.')
            # modelarray分繰り返す
            for currentmodel in modelarray:
                print(f'Using the {currentmodel} model')
                # Whisperモデルをロードする
                model = whisper.load_model(currentmodel)
                # 変換
                result = model.transcribe(f'{source_dir}/{filename}')
                # 結果出力配列に変換後データを追加
                resultarray.append(result['text'])
                # 変換後のファイル名を作成
                converted_filename = filename
                for extension in extensions:
                    converted_filename = converted_filename.replace('.' + extension, '')
                # 結果出力配列に変換後のファイル名を追加
                resultfilearray.append(f'{converted_filename}_{currentmodel}_{datetimenow}.txt')

            # 処理したファイルをバックアップディレクトリに移動
            os.rename(f'{source_dir}/{filename}', f'{backup_dir}/{filename}')
            # バックアップディレクトリに移動したファイルに年月日時分秒をつけてリネーム
            os.rename(f'{backup_dir}/{filename}', f'{backup_dir}/{filename}.{datetimenow}')

    # 結果の書き込み
    index = 0
    for i in resultarray:
        # resultフォルダ内にファイルを作成し、結果を書き込む(ファイル名-Whisperモデル名.txt)
        with open(f'{result_dir}/{resultfilearray[index]}', mode='w+', encoding='utf-8') as f:
            f.write(i)
        index += 1
    return resultfilearray, resultarray

if __name__ == '__main__':
    # 引数があれば、そのモデルのみを対象とする. なければ、mediumのモデルを対象とする
    modelarray = sys.argv[1:] if len(sys.argv) > 1 else ['medium']
    valid_models = ['tiny', 'base', 'small', 'medium', 'large']
    modelarray = [model for model in modelarray if model in valid_models]
    resultfilearray, resultarray = sound_transcription(modelarray)
    # 結果出力
    index = 0
    for i in resultarray:
        print(resultfilearray[index])
        print(i)
        index += 1
