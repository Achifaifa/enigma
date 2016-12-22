#! /usr/bin/env python

import string

rotor_values=[[16, 14, 21, -2, 10, 17, 7, 1, -2, 16, -5, 7, 9, 11, -12, -8, -6, 0, 1, -8, -8, -17, -22, -14, -4, -22],
              [20, 2, 2, 9, 13, 14, -4, 0, 14, 16, -4, 7, 12, 10, 7, 1, -8, -12, -3, -5, -10, -20, -9, -23, -13, -16],
              [15, 23, 4, 20, 0, 7, 19, 7, 3, 0, 9, 7, 8, -8, -7, -15, -14, -1, -15, -18, -3, -11, -14, -2, -11, -3],
              [1, -1, 18, 21, 17, 6, -1, 9, -1, 9, 3, -7, -10, 4, -5, 4, -1, 5, -6, 4, -17, -15, -8, 2, -16, -15]]

class rotor:

  def __init__(self, rotor_number, initial_position):
    """
    Rotor constructor. 

    rotor_number:     id of the rotor (Used to take change values from the rotors list)
    initial_position: first position that will be used
    """

    self.values=rotor_values[rotor_number]
    self.position=initial_position

  def __getitem__(self, index):

    return self.values[index]

  def rotate(self):
    """
    if the rotor has reached the final position, sends a signal to move the next one
    """

    self.position=(self.position+1)%26
    return self.position

class enigma:

  def __init__(self, rotor_positions):
    """
    rotor_positions:  iterable with the initial positions of the 4 cylinders [0,25]
    """

    self.rotors=[rotor(i, rotor_positions[i]) for i in range(4)]

  def encode_key(self, char):

    char=char.lower()
    for i in self.rotors: 
      char=chr((ord(char)+i[i.position]))
      if ord(char)<97: char=chr(ord(char)+26)
      if ord(char)>122:char=chr(ord(char)-26)
    self.iterate()
    return char

  def decode_key(self, char):

    char=char.lower()
    for i in self.rotors: 
      char=chr((ord(char)-i[i.position]))
      if ord(char)<97: char=chr(ord(char)+26)
      if ord(char)>122:char=chr(ord(char)-26)
    self.iterate()
    return char

  def iterate(self):

    if self.rotors[0].rotate():
      if self.rotors[1].rotate():
        if self.rotors[2].rotate():
          self.rotors[3].rotate()

rotorpos=(1,2,5,2)
test=enigma(rotorpos)
testout=""
totest="thisisatest"

print totest

for i in totest:
  i=test.encode_key(i)
  testout+=i 

print testout
test=enigma(rotorpos)

testf=""
for i in testout:
  i=test.decode_key(i)
  testf+=i

print testf


