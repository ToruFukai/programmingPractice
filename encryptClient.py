import socket
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "localhost"

port = 5002

# connection to hostname on the port.
s.connect((host, port))

msg = input()

def encrypt(msg):
    d = {}
    for c in (65, 97):#ASCIIコード表で検索
        for i in range(26):#アルファベットの数
            d[chr(i + c)] = chr((i + 13) % 26 + c)#文字をずらす
    return "".join([d.get(c, c) for c in msg])

enmsg = encrypt(msg)

s.send(enmsg.encode('ascii'))

response = s.recv(1024) #レシーブは適当な2進数にします（大きすぎるとダメ）
response = response.decode('ascii') #ここで変数の更新を行っている

print(response) #ここにresponse.decode('ascii')と入れても同じ結果となる

s.close()

#(1)クライアントでエンコードしてサーバーで出コードして戻す
#(2)bはバイナリー
#(3)変数の中身を変えるために変数を更新することを忘れないように
#(4)bと出てるときはバイナリのままなので↑のことに注意すること