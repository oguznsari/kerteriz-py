import socket

# Socket oluşturulması
s = socket.socket()

# bağlanılacak adres ve port
host = "localhost"
port = 12345

try:
    # bağlantı yap
    s.connect((host, port))

    # serverdan yanıtı al
    yanit = s.recv(1024)
    print(yanit.decode("utf-8"))

    # bağlantıyı kapat
    s.close()

except socket.error as msg:
    print("[Server aktif değil.] Mesaj:", msg)


"""
Socket programlama ile server tarafını kodlamamızın ardından client tarafını da kodlayarak bağlantılarımızı yapmaya 
    başlayabiliriz. Bunun için yine önce kütüphanemizi dahil edip ardından bağlanacağımız IP ve portu belirleyelim. 
    Son olarak bağlantımızı kurarak karşıdan gelen mesajı ekrana yazdıralım.

Client tarafını yazarken ek olarak recv() fonksiyonu ile mesajın tampon boyutunu (buffer size) ayarlamamız gerekiyor. 
    Böylece bir sn de alınacak maksimum dosya boyutunu byte cinsinden ayarlamış oluyoruz. 
    Bu boyutu ayarlarken değerimizin 2 nin üssü şeklinde olmasına dikkat ediniz. (Örneğin 1024, 2048, 4096...)  """

