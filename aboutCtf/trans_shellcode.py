raw=input()
out=""
for i in range(0,len(raw),3):
    out+=("\\"+"x"+raw[i:i+2])
print(out)
