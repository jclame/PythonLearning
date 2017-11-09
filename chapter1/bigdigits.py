#/usr/bin/env python3

'''
  这是书中的例子
  
  在命令行中提供一个数值，之后该程序会使用“大”数字向控制台输出该数值

  输入：数值
  输出：大数字

  输入例子：4107
  输出例子：
	    *   *    ***   *****
	   **  **   *   *      *
	  * *   *  *     *    *
	 *  *   *  *     *   *
	******  *  *     *  *
	    *   *   *   *  *
	    *  ***   ***   *
  提示：
  可以用 sys 库	
'''

import sys

Zero  = ["  ***  ",
		 " *   * ",
		 "*     *",
		 "*     *",
		 "*     *",
		 " *   * ",
		 "  ***  "]

One   = [" * ",
		 "** ",
		 " * ",
		 " * ",
		 " * ",
		 " * ",
		 "***"]

Two   = [" *** ",
		 "*   *",
		 "    *",
		 "   * ",
		 "  *  ",
		 " *   ",
		 "*****"]

Three = [" *** ",
		 "*   *",
		 "    *",
		 "  ** ",
		 "    *",
		 "*   *",
		 " *** "]

Four  = ["    * ",
	 	 "   ** ",
	 	 "  * * ",
		 " *  * ",
		 "******",
		 "    * ",
		 "    * "]

Five  = ["******",
		 "*     ",
		 "* *** ",
		 "*    *",
		 "     *",
		 "*    *",
		 " **** "]

Six   = [" **** ",
		 "*    *",
		 "*     ",
		 "* *** ",
		 "*    *",
		 "*    *",
		 " **** "]

Seven = ["*****",
		 "    *",
		 "   * ",
		 "  *  ",
		 " *   ",
		 "*    ",
		 "*    "]

Eight = [" *** ",
		 "*   *",
		 "*   *",
		 " *** ",
		 "*   *",
		 "*   *",
		 " *** "]

Nine  = [" **** ",
		 "*    *",
		 "*    *",
		 " *****",
		 "    * ",
		 "   *  ",
		 "  *   ",]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
	digits = sys.argv[1]
	row = 0
	while row < 7:
		line = ""
		column = 0
		while column < len(digits):
			number = int(digits[column])
			digit = Digits[number]
			line += digit[row] + " "
			column += 1
		print(line)
		row += 1
except IndexError:
	print("usage: bigdigits.py <number>")
except ValueError as err:
	print(err, "in", digits)