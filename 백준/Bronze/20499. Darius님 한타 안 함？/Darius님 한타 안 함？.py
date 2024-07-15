K, D, A = map(int, input().split('/'))
print(['gosu','hasu'][(K+A<D) or D==0])