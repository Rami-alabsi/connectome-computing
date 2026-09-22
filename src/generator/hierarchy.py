import random
from collections import defaultdict
from typing import Iterable

def hierarchical_labels(n: int, *, levels: tuple[int, ...] = (4, 4)) -> list[tuple[int, ...]]:
    if n < 1 or not levels or any(x < 1 for x in levels):
        raise ValueError("n and hierarchy levels must be positive")
    labels=[]
    for i in range(n):
        value=i
        path=[]
        for size in reversed(levels):
            path.append(value % size)
            value//=size
        labels.append(tuple(reversed(path)))
    return labels

def hierarchical_directed_graph(n: int, target_edges: int, *, levels=(4,4),
                                 p_same_leaf=1.0, p_same_parent=0.35,
                                 p_cross_parent=0.08, seed=0) -> set[tuple[int,int]]:
    if target_edges < 0 or target_edges > n*(n-1):
        raise ValueError("target_edges outside simple directed graph capacity")
    rng=random.Random(seed)
    labels=hierarchical_labels(n, levels=levels)
    candidates=[]
    for u in range(n):
        for v in range(n):
            if u==v: continue
            common=0
            for a,b in zip(labels[u],labels[v]):
                if a!=b: break
                common+=1
            p=p_same_leaf if common==len(levels) else (p_same_parent if common>=max(1,len(levels)-1) else p_cross_parent)
            candidates.append((u,v,p))
    rng.shuffle(candidates)
    chosen=[]
    for u,v,p in candidates:
        if rng.random() <= min(1.0,max(0.0,p)):
            chosen.append((u,v))
            if len(chosen)==target_edges:
                return set(chosen)
    result=set(chosen)
    remaining=[(u,v) for u,v,_ in candidates if (u,v) not in result]
    rng.shuffle(remaining)
    result.update(remaining[:target_edges-len(result)])
    return result

def hierarchy_counts(labels: Iterable[tuple[int,...]]) -> dict[int,int]:
    counts=defaultdict(int)
    for label in labels: counts[len(label)]+=1
    return dict(counts)
