#/usr/bin/env python3

'''
  这是书中1.5节的练习3

  创建一些词汇列表，比如，冠词（"the", "a"等）、主题（"cat", "dog", "man", "woman"）、动词（“sang”, "ran", "jumped"）与状语（"loudly", "quietly", "well"）等，
  若用户给定参数n（1<n<10），则循环n次，每次迭代中，使用random.choice()函数选取冠词、主题、动词、状语等内容。
  若用户没有给定参数，则循环5次，每次迭代中，使用random.choice()函数选取冠词、主题、动词、状语等内容。
  使用random.randint()函数在两种语句结构之间进行选择：
  冠词、主题、动词、状语；
  只包括冠词、主题与动词，之后打印语句。

  输入：awfulpoetry1_ans.py

  输出例子：
  another boy laughed badly
  the woman jumped
  a boy hoped
  a horse jumped
  another man laughed rudely

  tip: 可以使用random包
'''

import random
import sys

art = ["another", "a", "no", "any"]
theme = ["dog", "man", "book", "game", "Lanister", "cat", "taylor"]
verb = ["paid", "got", "played", "laughed", "hoped", "ran", "fucked", "knew"]
adv = ["sadly", "well", "rudely", "only", "quietly", "badly", "widely", "quickly", "slowly"]

def print_line(n):
  time = 0
  while time<n:
    line = ""
    struct = Struct[random.randint(0,1)]
    for word in struct:
      line += random.choice(word)
      line += " "
    print(line)
    time += 1

struct1 = [art, theme, verb, adv]
struct2 = [art, theme, verb]
Struct = [struct1, struct2]

if len(sys.argv)<2:
  print_line(5)
elif 1<int(sys.argv[1])<10:
  print_line(int(sys.argv[1]))
else:
  print("the arguement must more than 1 and less than 10")