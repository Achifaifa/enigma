#! /usr/bin/env python

import random, string

def rotor_generator():

  rand=list(string.lowercase)

  while 1:
    random.shuffle(rand)
    diffs=[ord(i)-97-rand.index(i) for i in rand]
    yield diffs

a=rotor_generator()
for i in range(4): print a.next()


