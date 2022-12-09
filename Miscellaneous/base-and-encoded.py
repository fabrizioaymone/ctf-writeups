from pwn import *
import base64
import binascii

HOST = "based.challs.olicyber.it"
PORT = 10600

conn = remote(HOST, PORT)

conn.recvline()
conn.recvline()
conn.recvline()
response=b"Ottimo"
while b"Ottimo" in response:
    conn.recvline()
    format = str(conn.recvline())
    data = conn.recvline()
    data = data[13:-3]
    if " da base64" in format:
        decoded = base64.b64decode(data)
    elif " a base64" in format:
        decoded = base64.b64encode(data)
    elif " da binario" in format:
        binary_int = int(data.decode(), 2)
        print(binary_int)
        byte_number = (binary_int.bit_length() + 7) // 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        decoded = binary_array
        print(f"binary array: {binary_array}")
    elif " a binario" in format:
        decoded = bin(int(binascii.hexlify(data),16))
        decoded = decoded[2:].encode()
    elif " a esadecimale" in format:
        decoded = data.hex().encode()
    elif " da esadecimale" in format:
        decoded = bytes.fromhex(data.decode()).decode().encode("ASCII")
    else:
        print(format)
        print(data)
    conn.recvuntil('risposta!\n')
    print(format)
    print(data)
    print(b'{"answer": "%b"}\n' % decoded)
    conn.send(b'{"answer": "%b"}\n' % decoded)
    print(conn.recvline())
    response=conn.recvline()
    print(response)

