def tokens(p):
    lookup = dict([(word, n) for n,word in enumerate(set(re.findall(r"[\w']+", p)))])
    parts = re.split(r"[,.']+", p)
    int_array = [[d[w] for w in re.findall(r'[\w]+', s) ] for s in parts]
