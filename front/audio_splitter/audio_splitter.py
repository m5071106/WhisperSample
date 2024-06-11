from pydub import AudioSegment
from pydub.silence import split_on_silence
from pathlib import Path

import datetime
import os

def split_audio(max_file_size, min_silence_len, keep_silence, silence_thresh):
    """
    max_file_size (int): 出力される音声ファイルの最大サイズ (単位: Byte) ※ wav 以外は割と適当
    min_silence_len (int): 無音として識別される最小の持続時間
    keep_silence (int): 音声が無音部分で分割された後、各チャンクの先頭または末尾に保持する無音の持続時間
    silence_thresh (int): 無音として識別される音量の閾値
    """

    # 対象拡張子の読み込み
    with open('./resources/extensions.txt', 'r') as file:
        extensions = file.read().splitlines()

    source_dir = Path('./resources/source.txt').read_text().strip()
    result_dir = Path('./resources/result.txt').read_text().strip()
    backup_dir = "./backup"

    # sourceディレクトリ内のファイル一覧を取得
    file_list = os.listdir(source_dir)

    # 認識対象の拡張子のファイルのみを抽出し、変換を行う
    for filename in file_list:
        if any(extension in filename for extension in extensions):
            print(f'{filename}の無音除去を開始')
            # 変換時刻を取得
            datetimenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            converted_filename = ''.join(c for c in filename if c not in extensions)

            sound = AudioSegment.from_file(source_dir + "/" + filename)
            total_length = len(sound)
            total_size = os.path.getsize(source_dir + "/" + filename)
            max_length = total_length * (max_file_size / total_size)
            # print(total_length, total_size)
            # print(max_length)

            # 無音部分をカットして分割
            chunks = split_on_silence(
                sound,
                min_silence_len=min_silence_len,
                silence_thresh=silence_thresh,
                keep_silence=keep_silence,
            )

            # 分割したチャンクをmax_lengthごとに結合
            current_chunk = None
            file_count = 1
            for i, c in enumerate(chunks):
                if current_chunk is None:
                    current_chunk = c
                    continue
                temp_chunk = current_chunk + c
                outFilePath = f"{result_dir}/{converted_filename}_{(file_count):03d}.mp3"
                if len(temp_chunk) > max_length:
                    current_chunk.export(outFilePath, format="mp3")
                    current_chunk = c
                    file_count += 1
                else:
                    if i == len(chunks) - 1:
                        temp_chunk.export(outFilePath, format="mp3")
                    else:
                        current_chunk += c
            print(f'{filename}の無音除去を終了')

            # 処理したファイルをバックアップディレクトリに移動
            os.rename(f'{source_dir}/{filename}', f'{backup_dir}/{filename}')
            # バックアップディレクトリに移動したファイルに年月日時分秒をつけてリネーム
            os.rename(f'{backup_dir}/{filename}', f'{backup_dir}/{filename}.{datetimenow}')


if __name__ == '__main__':
    normal = -35
    high = -40
    very_high = -45
    split_audio(200000, 100, 100, very_high)
