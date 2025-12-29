errors = {}
FILE = "../docs/app.log"
with open(FILE, "r") as f:
    for lines in f:
        line = lines.strip().split("]")
        message = (line[1]) # remove the date and time from the log line

        if "ERROR" in message:
            message = message.split()
            message.pop(0)
            result = " ".join(message)
            if result in errors:
                errors[result] += 1
            else:
                errors[result] = 1

print(errors)
print("Total Errors:" , sum(errors.values()))











