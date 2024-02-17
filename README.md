# 事前準備
googletrans<br>
MeCab<br>
speech_recognition<br>
pyaudio<br>
以下のものをインストールしておいてください<br>
# 使い方
Quadrilingual.pyをダウンロードしてください。<br>
ダウンロードしたファイルを実行してください。<br>
マイクの許可が求められるので、許可してください。<br>
すると、下のようなものが出てきます。<br>
{'index': 0, 'structVersion': 2, 'name': 'マイク', 'hostApi': 0, 'maxInputChannels': 1, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.034520833333333334, 'defaultLowOutputLatency': 0.01, 'defaultHighInputLatency': 0.043854166666666666, 'defaultHighOutputLatency': 0.1, 'defaultSampleRate': 48000.0}<br>
これは、マイクやスピーカーなどの情報です。<br>
nameと書いているところで、自分のマイクだと思うもののindexの部分の数字を覚えててください。<br>
大体は初期設定のままでいけますが、コードの「INPUT_DEVICE_INDEX」に先ほどの数字を入れてください。<br>
そしたら、再実行してください。<br>
「リアルタイム変換を行います」の文字が出ますので、出たら何か喋ってみてください。<br>
すると、原文とエセクァドリンガルの文が出力されます。<br>
これでエセクァドリンガルになれます。<br>
ちなみに言語は、日本語、英語、中国語、韓国語で構成されています。<br>
終了機能はないので、Ctrl-Cをしてください。
# バグ
リアルタイム変換が遅すぎる。<br>
文がとても短くなる。<br>
たまにマイクチャンネルを変えた際にエラーが出る。<br>
