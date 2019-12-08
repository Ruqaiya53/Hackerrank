def merge_the_tools(S, N):
    # your code goes here
     
    for part in zip(*[iter(S)] * N):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
    
