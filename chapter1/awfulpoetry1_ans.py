#/usr/bin/env python3

'''
  这是书中1.5节的练习3

  创建一些词汇列表，比如，冠词（"the", "a"等）、主题（"cat", "dog", "man", "woman"）、动词（“sang”, "ran", "jumped"）与状语（"loudly", "quietly", "well"）等，
  之后循环5次，每次迭代中，使用random.choice()函数选取冠词、主题、动词、状语等内容。
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

art = ["another", "a", "no", "any"]
theme = ["dog", "man", "book", "game", "Lanister", "cat", "taylor"]
verb = ["paid", "got", "played", "laughed", "hoped", "ran", "fucked", "knew"]
adv = ["sadly", "well", "rudely", "only", "quietly", "badly", "widely", "quickly", "slowly"]

struct1 = [art, theme, verb, adv]
struct2 = [art, theme, verb]
Struct = [struct1, struct2]

time = 0
while time<5:
	line = ""
	struct = Struct[random.randint(0,1)]
	for word in struct:
		line += random.choice(word)
		line += " "
	print(line)
	time += 1