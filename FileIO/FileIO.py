import sys
import os

file_name = "test.txt"
test_file = open(file_name, "wb")
print(test_file.mode)
print(test_file.closed)
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()

test_file = open(file_name, "r+")
print(test_file.mode)
print(test_file.closed)

text_in_file = test_file.read()
print(text_in_file)
test_file.close()

print(test_file.closed)

# PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'test.txt' -> 'discard.txt'
# os.rename(file_name, "discard.txt")

# PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'test.txt'
# os.remove(file_name)
