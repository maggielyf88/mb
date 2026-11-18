import json, sys

json_file = sys.argv[1] if len(sys.argv) > 1 else 'replacements_1.json'

with open('index.html', 'r', encoding='utf-8') as f:
    t = f.read()

with open(json_file, 'r', encoding='utf-8') as f:
    repls = json.load(f)

count = 0
miss = 0
for old, new in repls:
    n = t.count(old)
    if n == 0:
        miss += 1
        print('MISS: ' + old[:90])
    else:
        t = t.replace(old, new)
        count += n

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(t)

print('{}: {} replacements, {} missed'.format(json_file, count, miss))
