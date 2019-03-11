#!/bin/python

import math
import os
import random
import re
import sys

# Complete the balancedForest function below.

def balancedForest(c, edges):

  if __name__ == '__main__':

    ##QUANTAS QUERYS?
    q = 0
    while (q < 1 or q > 5):
      print "how many querys?"
      q = int(raw_input())

    for q_itr in xrange(q):

        #QUANTAS FOLHAS/NODOS?
        n = 0
        while (n < 1 or n > 5*(10**4)):
          print "How many nodes?"
          n = int(raw_input())
       
       #INSERE OS VALORES NAS FOLHAS/NODOS
        error = True
        while(error):
          print "Instert values separated by space: "
          c = map(int, raw_input().rstrip().split())
          edges = []
          error = any(i > 10**9 for i in c)

        #INSERE AS CONEXOES/GALHOS
        for _ in xrange(n - 1):
          print "Insert edge: "
          edges.append(map(int, raw_input().rstrip().split()))
        
        #CRIA AS CONEXOES DAS DUAS FUTURAS ARVORES
        edges2 = []
        edges3 = []


        #QUEBRA A DOIS GALHOS/CONEXOES E COLOCA NAS NOVAS ARVORES
        for i in xrange(0,2):
          found = False
          while(not found):
            print "Break an edge: "
            broken = map(int, raw_input().rstrip().split())
            for sublist in edges:
              if sublist is broken:
                print "Found it"
                del edges[sublist]
                if i == 1:
                  edges2.append(broken)
                if i == 2:
                  edges3.append(broken)
                found = True
                break
            if not found:
              print "Not found... Try again"
        
        #REMOVE AS FOLHAS CONECTADAS AS PARTES SEPARADAS DA ARVORE ORIGINAL
        #E AS COLOCAM NAS NOVAS ARVORES
        for i in xrange (n-1):
          for sublist in edges:
            if sublist[0] == edges2[i][1]:
              edges2.append(edges[sublist].pop)

        for i in xrange (n-1):
          for sublist in edges:
            if sublist[0] == edges3[i][1]:
              edges3.append(edges[sublist].pop)

        #SOMA OS VALORES DE CADA ARVORE
        tree_sum[0] = c[edges[0][0]]
        tree_sum[1] = c[edges2[0][0]]
        tree_sum[2] = c[edges3[0][0]]

        for i in xrange (0, len(edges)):
          tree_sum[0] += c[edges[i][1]]
        for i in xrange (0, len(edges2)):
          tree_sum[1] += c[edges2[i][1]]
        for i in xrange (0, len(edges3)):
          tree_sum[2] += c[edges3[i][1]]

        if tree_sum[0] == tree_sum[1]:
          return tree_sum[0] - tree_sum[2]
        else:
          if tree_sum[0] == tree_sum[2]:
            return tree_sum[0] - tree_sum[1]
          else:
            if tree_sum[1] == tree_sum[2]:
              return tree_sum[1] - tree_sum[0]
            else:
              return -1

    

        

c = int()
edges = []
balancedForest(c, edges)

print edges, "\n", c

