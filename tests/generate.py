#!/usr/bin/env python3
import os, random; random.seed(50)
def neighbors(A,n,m,i,j):
    s=0
    for di in (-1,0,1):
        for dj in (-1,0,1):
            if di==0 and dj==0: continue
            ii=i+di; jj=j+dj
            if 0<=ii<n and 0<=jj<m: s+=A[ii*m+jj]
    return s
def step(A,n,m):
    B=[0]*(n*m)
    for i in range(n):
        for j in range(m):
            s=neighbors(A,n,m,i,j); idx=i*m+j
            B[idx] = 1 if (A[idx]==1 and (s==2 or s==3)) or (A[idx]==0 and s==3) else 0
    return B
def w(name, n, m, A):
    os.makedirs("tests", exist_ok=True)
    with open(f"tests/input_{name}.txt","w") as f:
        f.write(f"{n} {m}\\n")
        for i in range(n):
            f.write(" ".join(str(x) for x in A[i*m:(i+1)*m])+"\\n")
    B=step(A,n,m)
    with open(f"tests/output_{name}.txt","w") as f:
        for i in range(n):
            f.write(" ".join(str(x) for x in B[i*m:(i+1)*m])+"\\n")
def main():
    w("min",1,1,[0])
    n,m=2000,2000; A=[0]*(n*m); c=(n//2)*m + m//2; A[c-1]=A[c]=A[c+1]=1; w("max",n,m,A)
    n,m=7,7; A=[random.randint(0,1) for _ in range(n*m)]; w("rnd", n, m, A)
if __name__=="__main__": main()
