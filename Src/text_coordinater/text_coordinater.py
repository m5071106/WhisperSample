from pathlib import Path

import os
import datetime


def text_concater():

    # 現在のディレクトリを取得
    current_dir = os.path.dirname(__file__)

    # 結果出力配列
    resultarray = []
    resultfilearray = []

    # 改行区切りの対象単語リストを取得
    with open(current_dir + '/resources/append_returnwords.txt', mode='r', encoding='utf-8') as f:
        append_returnwords = f.read().splitlines()

    # 置換対象単語リストを取得
    with open(current_dir + '/resources/replace_words.txt', mode='r', encoding='utf-8') as f:
        replace_words = f.read().splitlines()

    # 入出力ディレクトリのパス
    source_dir = current_dir + '/' + Path(current_dir + '/resources/source.txt').read_text().strip()
    result_dir = current_dir + '/' + Path(current_dir + '/resources/result.txt').read_text().strip()
    backup_dir = current_dir + '/backup'

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
        print(f'{filename} concatenation started.')
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
    with open(f'{result_dir}/temporary.txt', mode='w+', encoding='utf-8') as f:
        for i in resultarray:
            f.write(i)

    # 改行を追加する処理の開始
    with open(f'{result_dir}/temporary.txt', mode='r', encoding='utf-8') as f:
        file_contents = f.read()
    result = file_contents.replace(' ', '')

    # append_returnwordsに含まれる単語の後ろに改行を追加
    for word in append_returnwords:
        result = result.replace(word, word + '\n')

    # replace_wordsに含まれる単語を置換
    for word in replace_words:
        words = word.split(',')
        result = result.replace(words[0], words[1])

    # 変換結果をファイルに書き込む
    with open(f'{result_dir}/result.txt', mode='w+', encoding='utf-8') as f:
        f.write(result)

    # 一時ファイルの削除
    os.remove(f'{result_dir}/temporary.txt')

    return resultfilearray, resultarray, result


if __name__ == '__main__':
    # テキスト結合
    resultfilearray, resultarray, result = text_concater()
    print('Text concatenation completed.')

