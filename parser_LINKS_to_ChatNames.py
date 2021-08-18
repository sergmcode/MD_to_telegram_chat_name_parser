import json
data = None
with open('links.json', 'r', encoding='utf8') as f:
    data = json.load(f)

import re
g_list = []
re_ojb = re.compile('^https:\/\/t.me\/(.+)$')
for url in data:
    m = re_ojb.match(url)
    if m is not None:
        g_name = m.groups()[0]
        g_list.append(f'@{g_name}')

with open('chat_names.json', 'w', encoding='utf8') as f:
    json.dump(g_list, f)

pass