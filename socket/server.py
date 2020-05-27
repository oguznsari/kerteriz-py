import socket

host = "127.0.0.1"
port = 12345

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket oluşturuldu.")

    s.bind((host, port))
    print("Socket {} nolu porta bağlandı".format(port))

    s.listen(5)                         # max 5 connection
    print("socket dinleniyor.")

except socket.error as msg:
    print("Hata:", msg)


while True:
    # Client ile bağlantı kurulursa
    c, addr = s.accept()
    print("Gelen bağlantı:", addr)

    # Bağlanan client tarafına hoşgeldin mesajı gönderelim.
    mesaj = 'Bağlantı için teşekkürler.'
    c.send(mesaj.encode('utf-8'))

    # bağlantıyı sonlandıralım
    c.close()


"""
socket(family, type)

family:
    AF_UNIX: UNIX domain protocols
    AF_INET: TCP ve UDP IPv4 protocols
    AF_INET6: TCP ve UDP IPv6 protocols

type:
    SOCK_STREAM: TCP connection
    SOCK_DGRAM: UDP connection
    SOCK_RAW: Henüz olgunlaşmamış soketler
    SOCK_RDM: Güvenilir datagramlar için
    SOCK_SEQPACKET: Bağlantı üzerinden kayıtlar için bir dizi transfer.

Biz bu örneğimizde en çok kullanılan TCP bağlantı tipini ve IPv4 adresleme seçeneğini kullanacağız. 
Bir önceki kodumuz ile bağlantıyıda hazır ettiğimize göre artık server kanalı dinlemeye hazır demektir. """
