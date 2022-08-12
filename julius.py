import socket
import time
import re

#sub.test()

# ローカル環境のIPアドレス
host = '127.0.0.1'
# Juliusとの通信用ポート番号
port = 10500

# Juliusにソケット通信で接続
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
time.sleep(2)

# 正規表現で認識された言葉を抽出
extracted_word = re.compile('WORD="([^"]+)"')
data = ""

try:
    print("起動中")
    file = open("untitle.txt", "w") 
    while True:
        while (data.find("</RECOGOUT>\n.") == -1):
            data += str(client.recv(1024).decode('shift_jis'))

        # 単語を抽出
        recog_text = ""
        for word in filter(bool, extracted_word.findall(data)):
            recog_text += word

        # 単語を表示
        print("認識結果: " + recog_text)
        file.write("recog_text")
        word=recog_text
        if recog_text=="終了。":
            client.close()
            break
        elif time.sleep(2):
            if word==recog_text:
                file.write("\n")
            elif word!=recog_text:
                word=recog_text

except:
    print('PROCESS END')
    client.send("DIE".encode('shift_jis'))
    client.close()
