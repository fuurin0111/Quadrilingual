# 事前準備
googletrans
MeCab
speech_recognition
pyaudio
以下のものをインストールしておいてください
# 使い方
Quadrilingual.pyをダウンロードしてください。
ダウンロードしたファイルを実行してください。
マイクの許可が求められるので、許可してください。
すると、下のようなものが出てきます。
{'index': 0, 'structVersion': 2, 'name': 'マイク', 'hostApi': 0, 'maxInputChannels': 1, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.034520833333333334, 'defaultLowOutputLatency': 0.01, 'defaultHighInputLatency': 0.043854166666666666, 'defaultHighOutputLatency': 0.1, 'defaultSampleRate': 48000.0}
自分のマイクだと思うもののindexの部分の数字を覚えててください。
大体は初期設定のままでいけますが、コードの「INPUT_DEVICE_INDEX」に先ほどの数字を入れてください。
そしたら、再実行してください。
「リアルタイム変換を行います」の文字が出ますので、出たら何か喋ってみてください。
すると、原文とエセクァドリンガルの文が出力されます。
これでエセクァドリンガルになれます。
ちなみに言語は、日本語、英語、中国語、韓国語で構成されています。
# バグ
リアルタイム変換が遅すぎる。
文がとても短くなる。
たまにマイクチャンネルを変えた際にエラーが出る。
