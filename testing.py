#!/usr/bin/env pyton3

def Add(a, b):
  return a + b

def Sub(a, b):
  retun a - b

def main():
  A = 10
  B = 5
  addition = add(A, B)
  subtraction = sub(A,B)
  print(f"a:{A}\nb:{B}\naddition:{addition}\nsubtraction:{subtraction}\n")
  
if __name__ == '__main__':
  main()
