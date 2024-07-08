from moviepy.editor import *
from pathlib import Path

import os
import datetime

def convert_mp4_to_mp3():

    # ファイルのパスを取得
    current_dir = os.path.dirname(__file__)

    # 対象拡張子の読み込み
    with open(current_dir + '/resources/extensions.txt', 'r') as file:
        extensions = file.read().splitlines()

    source_dir = current_dir + '/' + Path(current_dir + '/resources/source.txt').read_text().strip()
    result_dir = current_dir + '/' + Path(current_dir + '/resources/result.txt').read_text().strip()
    backup_dir = current_dir + "/backup"

    # ディレクトリが存在しない場合は作成
    if not os.path.exists(f"{source_dir}"):
        os.makedirs(f"{source_dir}")
    if not os.path.exists(f"{result_dir}"):
        os.makedirs(f"{result_dir}")
    if not os.path.exists(f"{backup_dir}"):
        os.makedirs(f"{backup_dir}")

    # sourceディレクトリ内のファイル一覧を取得
    file_list = os.listdir(f"{source_dir}")

    # 変換時刻を取得
    datetimenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    # 認識対象の拡張子のファイルのみを抽出し、変換を行う
    for filename in file_list:
        print(f'{filename}のmp4からmp3への変換を開始')
        # 変換後のファイル名作成
        converted_filename = ''.join(c for c in filename if c not in extensions)
        outFilePath = f"{result_dir}/{converted_filename}.mp3"

        video = VideoFileClip(f'{source_dir}/{filename}')
        audio = video.audio
        audio.write_audiofile(outFilePath)

        # ファイルを閉じる
        audio.close()
        video.close()

        # 処理したファイルをバックアップディレクトリに移動
        os.rename(f'{source_dir}/{filename}', f'{backup_dir}/{filename}')
        # バックアップディレクトリに移動したファイルに年月日時分秒をつけてリネーム
        os.rename(f'{backup_dir}/{filename}', f'{backup_dir}/{filename}.{datetimenow}')

if __name__ == '__main__':
    convert_mp4_to_mp3()