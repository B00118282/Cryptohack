from pwn import xor

flag = xor(bytes.fromhex("ed66878c338e662d3473f0d98eedbd0d"), bytes.fromhex("7ae18c704272532658c10b5faad06d74"))
print(flag)

byte_string = b""

decoded_string = byte_string.decode("utf8")

print(decoded_string)