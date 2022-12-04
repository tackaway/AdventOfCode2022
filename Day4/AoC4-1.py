count=0
f = open("input.txt", "r")   #Open the file
for x in f:
    r1s = int(x.partition(",")[0].partition("-")[0].strip())
    r1e = int(x.partition(",")[0].partition("-")[2].strip())
    r2s = int(x.partition(",")[2].partition("-")[0].strip())
    r2e = int(x.partition(",")[2].partition("-")[2].strip())
    if((r2s >= r1s and r2e <= r1e) or (r1s >= r2s and r1e <= r2e)):
        count+=1
print(count)


