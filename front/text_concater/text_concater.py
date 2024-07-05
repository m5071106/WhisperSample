import os
import datetime

from pathlib import Path


def text_concater():
    # 結果出力配列
    resultarray = []
    resultfilearray = []

    # 入出力ディレクトリのパス
    source_dir = Path('./resources/source.txt').read_text().strip()
    result_dir = Path('./resources/result.txt').read_text().strip()
    backup_dir = './backup'

    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # sourceディレクトリ内のファイル一覧を取得
    file_list = os.listdir(source_dir)

    # 認識対象の拡張子のファイルのみを抽出し、変換を行う
    for filename in file_list:
        print(f'{filename} concatenation started.')
        # 変換時刻を取得
        datetimenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        # 変換
        with open(f'{source_dir}/{filename}', mode='r', encoding='utf-8') as f:
            result = f.read()
        # 結果出力配列に変換後データを追加
        resultarray.append(result)
        # 変換後のファイル名を作成
        converted_filename = filename
        # 結果出力配列に変換後のファイル名を追加
        resultfilearray.append(f'{converted_filename}_{datetimenow}.txt')

        # 処理したファイルをバックアップディレクトリに移動
        os.rename(f'{source_dir}/{filename}', f'{backup_dir}/{filename}')
        # バックアップディレクトリに移動したファイルに年月日時分秒をつけてリネーム
        os.rename(f'{backup_dir}/{filename}', f'{backup_dir}/{filename}.{datetimenow}')

    # 結果の書き込み
    with open(f'{result_dir}/result.txt', mode='w+', encoding='utf-8') as f:
        for i in resultarray:
            f.write(i)

    with open(f'{result_dir}/result.txt', mode='r', encoding='utf-8') as f:
        file_contents = f.read()

    # 変換処理
    result = file_contents.replace(' ', '')
    replace_words = ['。', '?', '？', '！', 'ありがとうございます', 'になります', 
                     'あります', '思っています', 'しています', 'している', 'していた', 'しました', 'しません', 'しませんでした', 
                     '終わりました', '大丈夫です', 'はい', 'いいえ', 'お願いします', 'お願いいたします', 'ですね']
    for word in replace_words:
        result = result.replace(word, word + '\n')

    # 変換結果をファイルに書き込む
    with open(f'{result_dir}/result2.txt', mode='w+', encoding='utf-8') as f:
        f.write(result)

    return resultfilearray, resultarray, result


if __name__ == '__main__':
    # テキスト結合
    resultfilearray, resultarray, result = text_concater()
    print('Text concatenation completed.')

