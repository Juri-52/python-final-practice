# 課題1：成績レポート

学校の成績データから、合格した学生を調べるプログラムを作ります。架空の学生50人分の名前と点数がJSONファイルに用意されています。利用者が合格点を入力すると、条件を満たす学生の名前と人数を表示します。

JSON、リスト、データクラス、関数、例外処理を組み合わせます。

## 作るものと順番

| 順番 | ファイル | 実装する内容 |
| --- | --- | --- |
| 1 | student_result.py | StudentResultのフィールド |
| 2 | result_storage.py | load_results() |
| 3 | main.py | get_passed_names()とread_passing_score() |

scores.jsonとmain()の表示処理は完成済みです。書き換える必要はありません。

## 1. StudentResult

@dataclassを使い、次のフィールドを定義します。

| フィールド | 型 | 意味 |
| --- | --- | --- |
| name | str | 学生の名前 |
| score | int | 0〜100の点数 |

## 2. load_results(filename)

指定したJSONファイルをUTF-8で読み込み、**StudentResultのリスト**を返します。辞書のリストのまま返さないでください。

普通のopenとjson.loadを使います。ファイルのデータは正しいものとし、ファイルがない場合やJSONが壊れている場合の処理は不要です。

## 3. get_passed_names(results, passing_score)

- 点数がpassing_score**以上**の学生の名前を返します。
- 戻り値はlist[str]です。オブジェクト自体や点数は返しません。
- 元の並び順を保ち、元のリストや点数は変更しません。
- 該当者がいなければ空のリストを返します。

## 4. read_passing_score()

「合格点（0〜100）: 」と表示して入力を受け取り、intで整数に変換します。

| 入力 | 動作 |
| --- | --- |
| 0〜100の整数 | その整数を返す |
| abcなど、整数に変換できない値 | ValueErrorを処理し、「整数を入力してください。」と表示してNoneを返す |
| -1、101など、範囲外の整数 | 「0〜100で入力してください。」と表示してNoneを返す |

再入力のループは不要です。Noneの場合、準備されたmain()が終了します。

## 実行と確認

このフォルダー内で実行します。

```bash
python3 main.py
```

60を入力した場合：

```text
合格点（0〜100）: 60
合格基準: 60点
合格者: Akira, Ren, Yui, Yuto, Aoi, Sota, Riko, Kaito, Mio, Riku, Mei, Hayato, Ayaka, Takumi, Honoka, Minato, Yuna, Naoki, Misaki, Ryosuke, Kaori, Tsubasa, Nao, Kohei, Reina, Hiroki, Nozomi, Keita, Ayumi, Tomoya
合格者数: 30人
```

| 入力 | 確認する結果 |
| --- | --- |
| 60 | 30人。元の順番を保ち、60点のRenも含む |
| 0 | 元の順番で50人全員 |
| 100 | 「合格者: なし」「合格者数: 0人」 |
| abc | 整数のエラーメッセージを表示して終了 |
| 101 | 範囲のエラーメッセージを表示して終了 |

合格基準を変えてもscores.jsonの内容は変更しません。この課題ではテストファイルの作成は不要です。
