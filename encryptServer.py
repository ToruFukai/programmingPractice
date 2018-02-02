import socket

host = "localhost"
port = 5002

serversoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversoket.bind((host,port)) #この方法はアドレスバインド(ホストネーム、ポート番号)ソケットに


# TCPクライアント接続を受け入れる(blocking)
serversoket.listen(5)

while True:
    clientsocket, address = serversoket.accept() #受動的な接続が到着するまで待機、
    msg = clientsocket.recv(1024)
    msg = msg.decode('ascii') #ここで変数の更新を行っている

    print(msg)

    #msg2.upper()

    enmsg = msg#.upper() ここで変数の更新を行っている.upper()は大文字変換

    clientsocket.send(enmsg.encode('ascii'))
    clientsocket.close()

#(1)クライアントでエンコードしてサーバーで出コードして戻す
#(2)bはバイナリー
#(3)変数の中身を変えるために変数を更新することを忘れないように
#(4)bと出てるときはバイナリのままなので↑のことに注意すること

