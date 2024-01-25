def getURLs ():
    urls = dict()
    urls.setdefault('NoKey', 'NoValue')
    with open('.config', 'r') as f:
        for line in f.readlines():
            key = line.split(" ; ")[0]
            value = line.split(" ; ")[1]
            urls[key] = value
    return urls