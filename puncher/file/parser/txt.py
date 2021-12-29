import yaml

fp = open('../../data/stun_servers.txt')
lines = fp.readline()
yml = {'section': 'stun-servers', 'content': list()}
stun_list = list()
while lines:
    parse = lines.split()
    host = parse[1]
    port = int(parse[2])
    item = {host: port}
    stun_list.append(item)
    lines = fp.readline()
yml['content'] = stun_list
print(yaml.dump(yml, sort_keys=False))
