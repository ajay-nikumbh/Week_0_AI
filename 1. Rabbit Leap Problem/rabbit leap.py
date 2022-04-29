
START = 'abcdef-uvwxyz'
GOAL  = 'uvwxyz-abcdef'
RFROGS = 'abcdefghi'
LFROGS = 'rstuvwxyz'

def swap_positions(s,i,j):
    assert i < j
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

def apply_move(s,f):
    i = s.index(f)
    if f in RFROGS: # go right
        if i+1 < len(s) and s[i+1] == '-':
            return swap_positions(s,i,i+1)
        if i+2 < len(s) and s[i+1] != '-' and s[i+2] == '-':
            return swap_positions(s,i,i+2)
    if f in LFROGS: # go left
        if i-1 >= 0 and s[i-1] == '-':
            return swap_positions(s,i-1,i)
        if i-2 >= 0 and s[i-1] != '-' and s[i-2] == '-':
            return swap_positions(s,i-2,i)

def show_state(s):
    print (s)

def next_moves(s):
    i = s.index('-')
    ms = []
    # in from the left
    if i-1 >= 0 and s[i-1] in RFROGS:
        ms.append(s[i-1])
    if i-2 >= 0 and s[i-2] in RFROGS:
        ms.append(s[i-2])
    # in from the right
    if i+1 < len(s) and s[i+1] in LFROGS:
        ms.append(s[i+1])
    if i+2 < len(s) and s[i+2] in LFROGS:
        ms.append(s[i+2])
    return ms

def search(s):
    work = set([("",s)])
    states = 0
    while work:
        path, cur = work.pop()
        states += 1
        show_state(cur)
        for k in next_moves(cur):
            succ = apply_move(cur, k)
            work.add((path+k, succ))
            print ("  ", path+k, " --> ",
            show_state(succ))
            if succ == GOAL:
                print ("           !!! GOAL in", len(path)+1, " moves.")
    print ("Visited", states, "states.")

search(START)
