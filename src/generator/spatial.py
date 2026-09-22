import math
import random
from typing import Mapping, Sequence

def euclidean_distance(a: Sequence[float], b: Sequence[float]) -> float:
    if len(a)!=len(b): raise ValueError("coordinates must have equal dimensionality")
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))

def wiring_cost(edges: set[tuple[int,int]], positions: Mapping[int,Sequence[float]]) -> float:
    return sum(euclidean_distance(positions[u],positions[v]) for u,v in edges)

def distance_decay_probability(distance: float, *, length_scale: float, floor: float=0.0) -> float:
    if length_scale<=0: raise ValueError("length_scale must be positive")
    if distance<0: raise ValueError("distance must be non-negative")
    return min(1.0,max(floor,math.exp(-distance/length_scale)))

def spatial_graph(positions: Mapping[int,Sequence[float]], target_edges: int, *,
                  length_scale: float=0.25, long_range_fraction: float=0.05, seed: int=0) -> set[tuple[int,int]]:
    nodes=list(positions)
    if target_edges<0 or target_edges>len(nodes)*(len(nodes)-1):
        raise ValueError("target_edges outside simple directed graph capacity")
    if not 0<=long_range_fraction<=1: raise ValueError("long_range_fraction must be in [0,1]")
    rng=random.Random(seed)
    pairs=[]
    for u in nodes:
        for v in nodes:
            if u==v: continue
            d=euclidean_distance(positions[u],positions[v])
            pairs.append((u,v,d,distance_decay_probability(d,length_scale=length_scale)))
    pairs.sort(key=lambda x:x[2])
    shortcut_n=min(target_edges,int(round(target_edges*long_range_fraction)))
    tail=pairs[-max(1,shortcut_n):] if shortcut_n else []
    chosen=set(rng.sample([(u,v) for u,v,_,_ in tail],k=min(shortcut_n,len(tail)))) if tail else set()
    weighted=[(u,v,p) for u,v,_,p in pairs if (u,v) not in chosen]
    rng.shuffle(weighted); weighted.sort(key=lambda x:x[2],reverse=True)
    for u,v,p in weighted:
        if len(chosen)>=target_edges: break
        if rng.random()<p: chosen.add((u,v))
    if len(chosen)<target_edges:
        remaining=[(u,v) for u,v,_,_ in pairs if (u,v) not in chosen]
        rng.shuffle(remaining); chosen.update(remaining[:target_edges-len(chosen)])
    return chosen

def mean_edge_length(edges: set[tuple[int,int]], positions: Mapping[int,Sequence[float]]) -> float:
    return wiring_cost(edges,positions)/len(edges) if edges else 0.0
