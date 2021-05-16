bytesArr = bytearray(b'\x00\x0F')

# Bytearray allows modification
bytesArr[0] = 255
bytesArr.append(255)
print(bytesArr)