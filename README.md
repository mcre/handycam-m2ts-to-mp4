handycam-m2ts-to-mp4
=======================

Sony Handycamの`.m2ts`ファイルを、緯度経度情報を引き継いだうえで`.mp4`ファイルに変換します。

## 環境

* Docker
* Sony Handycam (HDR-CX560)
    - 他の機種のファイルも使えるかもしれませんが未確認です
    - ファイル名は`YYYYMMDDHHMMSS.m2ts`を想定しています。

## 使い方

`./input` 以下に`.m2ts`ファイルを配置しておきます。複数配置してもサブフォルダ以下に配置してもかまいません。同名の`.m2ts.modd`ファイルがある場合は、`.mp4`ファイルのmetatagとして緯度経度情報、タイムスタンプが反映されます。

```
docker build -t ffmpeg-python .  # 最初の一度だけ実行
docker run --rm -v $(pwd):$(pwd) -w $(pwd) ffmpeg-python /bin/sh -c "python main.py"
```

`./output`に`.mp4`ファイルが出力されます。

## 連絡先

* [twitter: @m_cre](https://twitter.com/m_cre)

## License

* MIT
  + see LICENSE
