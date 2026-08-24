from parser import parse_log_line

total = 0
parsed = 0
failed = 0
examples = []

with open("access.log", "r", encoding="utf-8") as file:

    for line in file:

        total += 1

        record = parse_log_line(line)

        if record:
            parsed += 1

        else:
            failed += 1

            if len(examples) < 10:
                examples.append(line.strip())

print()
print("Total Lines   :", total)
print("Parsed Lines  :", parsed)
print("Failed Lines  :", failed)

print()
print("Examples of failed lines:")

for line in examples:
    print(line)