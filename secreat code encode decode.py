def encode(msg):
    return ''.join(chr(ord(c) + 3) for c in msg)

def decode(msg):
    return ''.join(chr(ord(c) - 3) for c in msg)

choice = input("Encode or Decode? ").lower()
text = input("Enter your message: ")

if choice == "encode":
    print("Encoded:", encode(text))
else:
    print("Decoded:", decode(text))
