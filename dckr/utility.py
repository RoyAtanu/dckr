import json

def ParseName(name):
    return name[1:]

def ParsePort(portJson):
    ports = ''
    p = json.loads(str(portJson).replace("\'", "\""))
    for key, value in p.items():
        t = ('0.0.0.0' if value[0]['HostIp'] == '' else value[0]['HostIp']) + ':' + value[0]['HostPort'] + '->' + key
        if ports == '':
            ports += t
        else:
            ports += ', ' + t
    return ports

def ParseRepository(repoDigest, repoTag):
    repo = ''
    if repoDigest is not None:
        for r in repoDigest:
            if repo == '':
                repo = r.split('@sha256:')[0]
            else:
                repo += ', ' + r.split('@sha256:')[0]
        return repo
    if repoTag is not None:
        for r in repoTag:
            if repo == '':
                repo = r.split(':')[0]
            else:
                repo += ', ' + r.split(':')[0]
        return repo
    return repo

def ParseTag(repoTag):
    tag = ''
    if not repoTag :
        return '<none>'
    for t in repoTag:
        if tag == '':
            tag = t.split(':')[1]
        else:
            tag += ', ' + t.split(':')[1]
    return tag

def ParseSize(size):
    return str('%.1f'%(size/1000000)) + ' MB'