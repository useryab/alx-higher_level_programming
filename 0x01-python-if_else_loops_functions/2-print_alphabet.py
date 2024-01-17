#!/usr/bin/python3
start_codepoint = ord('a')
end_codepoint = ord('z')
for codepoint in range(start_codepoint, end_codepoint + 1):
   print(chr(codepoint), end="")