from pwn import *

def result(data):
    data = data.decode('UTF-8').split()
    op, a, b = data
    a,b = int(a), int(b)
    match op:
        case "SOMMA":
            return a+b
        case 'DIFFERENZA':
            return a-b
        case 'PRODOTTO':
            return a*b
        case 'DIVISIONE_INTERA':
            return int(a/b)
        case 'POTENZA':
            return a**b
        case _:
            return op




HOST = "2048.challs.olicyber.it"
PORT = 10007

conn = remote(HOST, PORT)
conn.recvuntil(b'operazioni:\n')

for i in range(20148):
    data = conn.recv()
    print(data.decode('UTF-8').split())
    print(result(data))
    conn.send(str(result(data)).encode()+b'\n')

conn.interactive()

    

    


