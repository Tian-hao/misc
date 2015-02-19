#!/usr/bin/python
import sys
import math
from string import atof

alignfilename = sys.argv[1]
alignfile = open (alignfilename, 'r')
seq = []
for line in alignfile:
  if not '>' in line:
    line = line.rstrip()
    seq.append(line)
alignfile.close()

#used a special way to due with deletion. gives it a score 0 no matter what. e.g. p*log2(p) = 0 for deletion '-'
for n in range(0,len(seq[0])):
  A=0; C=0; D=0; E=0; F=0; G=0; H=0; I=0; K=0; L=0; M=0; N=0; P=0; Q=0; R=0; S=0; T=0; V=0; W=0; Y=0; X=0; Z=0
  for i in range(0, len(seq)):
    if seq[i][n] == 'A': A=A+1
    elif seq[i][n] == 'C': C=C+1
    elif seq[i][n] == 'D': D=D+1
    elif seq[i][n] == 'E': E=E+1
    elif seq[i][n] == 'F': F=F+1
    elif seq[i][n] == 'G': G=G+1
    elif seq[i][n] == 'H': H=H+1
    elif seq[i][n] == 'I': I=I+1
    elif seq[i][n] == 'K': K=K+1
    elif seq[i][n] == 'L': L=L+1
    elif seq[i][n] == 'M': M=M+1
    elif seq[i][n] == 'N': N=N+1
    elif seq[i][n] == 'P': P=P+1
    elif seq[i][n] == 'Q': Q=Q+1
    elif seq[i][n] == 'R': R=R+1
    elif seq[i][n] == 'S': S=S+1
    elif seq[i][n] == 'T': T=T+1
    elif seq[i][n] == 'V': V=V+1
    elif seq[i][n] == 'W': W=W+1
    elif seq[i][n] == 'Y': Y=Y+1
    elif seq[i][n] == 'X': X=X+1
    elif seq[i][n] == '-': Z=Z+1
  total = sum([A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,Z])
  Ea=0;Ec=0;Ed=0;Ee=0;Ef=0;Eg=0;Eh=0;Ei=0;Ek=0;El=0;Em=0;En=0;Ep=0;Eq=0;Er=0;Es=0;Et=0;Ev=0;Ew=0;Ey=0;Ez=0;
  if not A == 0: Ea=atof(A)/total*math.log(atof(A)/atof(total),2)
  if not C == 0: Ec=atof(C)/total*math.log(atof(C)/atof(total),2)
  if not D == 0: Ed=atof(D)/total*math.log(atof(D)/atof(total),2)
  if not E == 0: Ee=atof(E)/total*math.log(atof(E)/atof(total),2)
  if not F == 0: Ef=atof(F)/total*math.log(atof(F)/atof(total),2) 
  if not G == 0: Eg=atof(G)/total*math.log(atof(G)/atof(total),2) 
  if not H == 0: Eh=atof(H)/total*math.log(atof(H)/atof(total),2) 
  if not I == 0: Ei=atof(I)/total*math.log(atof(I)/atof(total),2)
  if not K == 0: Ek=atof(K)/total*math.log(atof(K)/atof(total),2) 
  if not L == 0: El=atof(L)/total*math.log(atof(L)/atof(total),2) 
  if not M == 0: Em=atof(M)/total*math.log(atof(M)/atof(total),2) 
  if not N == 0: En=atof(N)/total*math.log(atof(N)/atof(total),2)
  if not P == 0: Ep=atof(P)/total*math.log(atof(P)/atof(total),2) 
  if not Q == 0: Eq=atof(Q)/total*math.log(atof(Q)/atof(total),2) 
  if not R == 0: Er=atof(R)/total*math.log(atof(R)/atof(total),2) 
  if not S == 0: Es=atof(S)/total*math.log(atof(S)/atof(total),2)
  if not T == 0: Et=atof(T)/total*math.log(atof(T)/atof(total),2) 
  if not V == 0: Ev=atof(V)/total*math.log(atof(V)/atof(total),2) 
  if not W == 0: Ew=atof(W)/total*math.log(atof(W)/atof(total),2) 
  if not Y == 0: Ey=atof(Y)/total*math.log(atof(Y)/atof(total),2)
  ShannonEntropy = -sum([Ea,Ec,Ed,Ee,Ef,Eg,Eh,Ei,Ek,El,Em,En,Ep,Eq,Er,Es,Et,Ev,Ew,Ey,Ez])
  print (str(n+1)+"\t"+str(ShannonEntropy))
  #print atof(K)/atof(total)
