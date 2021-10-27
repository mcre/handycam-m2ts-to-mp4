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

## 変換結果例

変換前

```
% docker run --rm -v $(pwd):$(pwd) -w $(pwd) ffmpeg-python /bin/sh -c "ffmpeg -i input/201203/20120323135331.m2ts"
# 中略
Input #0, mpegts, from 'input/201203/20120323135331.m2ts':
  Duration: 00:01:55.14, start: 1.033367, bitrate: 16591 kb/s
  Program 1 
    Stream #0:0[0x1011]: Video: h264 (HDMV / 0x564D4448), yuv420p(top first), 1920x1080 [SAR 1:1 DAR 16:9], 29.97 fps, 59.94 tbr, 90k tbn, 59.94 tbc
    Stream #0:1[0x1100]: Audio: ac3 (AC-3 / 0x332D4341), 48000 Hz, 5.1(side), fltp, 448 kb/s
    Stream #0:2[0x1200]: Subtitle: hdmv_pgs_subtitle ([144][0][0][0] / 0x0090), 1920x1080
```

変換後

```
% docker run --rm -v $(pwd):$(pwd) -w $(pwd) ffmpeg-python /bin/sh -c "ffmpeg -i output/201203/20120323135331.mp4"
# 中略
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'output/201203/20120323135331.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    creation_time   : 2012-03-23T04:53:31.000000Z
    date            : 2012-03-23T13:53:31+09:00
    encoder         : Lavf58.20.100
    location-eng    : +12.3456+123.4567/
    location        : +12.3456+123.4567/
  Duration: 00:01:55.16, start: 0.000000, bitrate: 9194 kb/s
    Stream #0:0(und): Video: h264 (avc1 / 0x31637661), yuv420p, 1920x1080 [SAR 1:1 DAR 16:9], 8794 kb/s, 29.97 fps, 29.97 tbr, 30k tbn, 59.94 tbc (default)
    Metadata:
      creation_time   : 2012-03-23T04:53:31.000000Z
      handler_name    : VideoHandler
    Stream #0:1(und): Audio: aac (mp4a / 0x6134706D), 48000 Hz, 5.1, fltp, 394 kb/s (default)
    Metadata:
      creation_time   : 2012-03-23T04:53:31.000000Z
      handler_name    : SoundHandler
```

## 連絡先

* [twitter: @m_cre](https://twitter.com/m_cre)

## License

* MIT
  + see LICENSE
