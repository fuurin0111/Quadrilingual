from googletrans import Translator
import MeCab
import random
import speech_recognition as sr
import time
import pyaudio

FORMAT        = pyaudio.paInt16
SAMPLE_RATE   = 44100        # サンプリングレート
CHANNELS      = 1            # モノラルかバイラルか
INPUT_DEVICE_INDEX = 0       # マイクのチャンネル
CALL_BACK_FREQUENCY = 3      # コールバック呼び出しの周期[sec]

mecab = MeCab.Tagger("-Owakati")
translator = Translator()

select_conditions = ['助詞', '助動詞']
mecab.parse('')

#textから助詞と助動詞を除ける
def wakati_text(text):
    node = mecab.parseToNode(text)
    terms = []
    while node:
        term = node.surface
        pos = node.feature.split(',')[0]

        if not(pos in select_conditions):
            terms.append(term)

        node = node.next

    text_result = list(filter(lambda x: x != "", terms))
    return text_result

def trans(tekisuto):
    text = tekisuto
    text_tr = '' 
    text_not_tr = []
    random_num = 0
    splittedLine = mecab.parse(text).split()

    text_not = wakati_text(text)

    for i in text_not:
        random_num = random.randint(1,4)
        if random_num == 1:
            text_not_tr.append(i)
        elif random_num == 2:
            text_not_tr.append(translator.translate(i, dest='en', src='ja').text)
        elif random_num == 3:
            text_not_tr.append(translator.translate(i, dest='ko', src='ja').text)
        elif random_num == 4:
            text_not_tr.append(translator.translate(i, dest='zh-CN', src='ja').text)

    num = 0

    for i in splittedLine:
        if i in text_not:
            num += 1
            text_tr += text_not_tr[num-1]
        else:
            text_tr += i
    print(text_tr)

def look_for_audio_input():
    """
    デバイスうえでのオーディオ系の機器情報を表示する
    """
    pa = pyaudio.PyAudio()

    for i in range(pa.get_device_count()):
        print(pa.get_device_info_by_index(i))
        print()

    pa.terminate()


def callback(in_data, frame_count, time_info, status):
    """
    コールバック関数の定義
    """
    
    global sprec # speech_recognitionオブジェクトを毎回作成するのではなく、使いまわすために、グローバル変数で定義しておく

    try:
        audiodata  = sr.AudioData(in_data, SAMPLE_RATE, 2)
        sprec_text = sprec.recognize_google(audiodata, language='ja-JP')
        
        print(sprec_text)    
        trans(sprec_text)
    
    except sr.UnknownValueError:
        pass
    
    except sr.RequestError as e:
        pass
    
    finally:
        return (None, pyaudio.paContinue)


def realtime_textise():
    global sprec # speech_recognitionオブジェクトを毎回作成するのではなく、使いまわすために、グローバル変数で定義しておく
    
    # speech recogniserインスタンスを生成
    sprec = sr.Recognizer() 
    
    # Audio インスタンス取得
    audio  = pyaudio.PyAudio() 
    
    # ストリームオブジェクトを作成
    stream = audio.open(format             = FORMAT,
                        rate               = SAMPLE_RATE,
                        channels           = CHANNELS,
                        input_device_index = INPUT_DEVICE_INDEX,
                        input              = True, 
                        frames_per_buffer  = SAMPLE_RATE*CALL_BACK_FREQUENCY, # CALL_BACK_FREQUENCY 秒周期でコールバック
                        stream_callback    = callback)
    
    stream.start_stream()
    
    while stream.is_active():
        time.sleep(0.1)
    
    stream.stop_stream()
    stream.close()
    audio.terminate()


def main():
    look_for_audio_input()
    print("リアルタイム変換を行います")
    realtime_textise()

if __name__ == '__main__':
    main()