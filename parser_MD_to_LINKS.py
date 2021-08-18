import re
with open('list.MD', 'r', encoding='utf8') as f:
    lines = f.readlines()

print(len(lines))
t_urls = []
for l in lines:
    # m = re.match('\(.+\)', l)
    # m = re.match(l, '\(.+\)')
    valid = re.compile('^.+\[.+\]\((.+?)\)')
    m = valid.match(l)
    if m is not None:
        # print(m.group())
        # print(m.groups()[0])
        t_urls.append(m.groups()[0])


import json
t = json.dumps(t_urls)

with open('links.json', 'w', encoding='utf8') as f:
    f.write(t)

print()