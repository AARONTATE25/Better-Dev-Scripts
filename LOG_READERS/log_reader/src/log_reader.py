FILE = "../docs/app.log"

with open(FILE, "r") as f:
    count = 0
    for lines in f:
        line = lines.strip().split()
        for word in line:
            if word == "ERROR":
                count +=1
            else: continue

    print(count)