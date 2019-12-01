from collections import Counter
def wcount(fname):
    with open(fname) as f:
        return Counter(f.read().split())

print("Numbers of words in the file : ",wcount("lyric.txt"))
