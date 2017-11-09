#!/usr/bin/env python3
'''
  这是书中练习1.5的的练习2

  该程序提示用户在while循环中输入数值，并根据数值逐步构建一个列表，然后对列表进行排序（不可以用list.sort()）
  用户输入（按Enter键）时，打印出输入的数值本身、输入的数值个数、输入的数值的和、输入的最小值和最大值、中值以及平均值。

  运行实例
  average1_ans.py
  enter a number or Enter to finishu: 5
  enter a number or Enter to finishu: 4
  enter a number or Enter to finishu: 1
  enter a number or Enter to finishu: 8
  enter a number or Enter to finishu: 5
  enter a number or Enter to finishu: 2
  enter a number or Enter to finishu: 
  
  输出：
  numbers: [1, 2, 4, 5, 5, 8]
  count = 6 sum = 25 lowest = 1 highest = 8 middle = 4.5 mean = 4.1666667
  
'''

Numbers = []
Count   = 0
Sum     = 0

while True:
	line = input("enter a number or Enter to finish:")
	if line:
		try:
			number = int(line)
		except ValueError as err:
			print(err)
			continue
		Sum += number
		Count +=1
		Numbers.append(number)
	else:
		break

if Count:
	# 列表插入排序
	for x in range(0, Count):
		for y in range(x,Count):
			if Numbers[x] > Numbers[y]:
				temp = Numbers[x]
				Numbers[x] = Numbers[y]
				Numbers[y] = temp

	if (Count % 2):
		middle = Numbers[int((Count-1)/2)]
	else:
		middle = (Numbers[int(Count/2)] + Numbers[int(Count/2)-1]) / 2
	print("numbers: ", Numbers)
	print("count = ", Count, " sum = ", Sum, " lowest = ", Numbers[0], " highest = ", Numbers[Count-1], " middle = ", middle, " mean = ", Sum/Count)