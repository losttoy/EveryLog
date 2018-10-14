# -*- coding: utf-8 -*- 
#!/usr/bin/python


import numpy as np
import sys


# mod
#1-等额本息
#2-等额本金
#3-到期一次性还本付息
#4-先息后本
mod = sys.argv[1]
#还款月份
month = int(sys.argv[2])
#总本金
principal = float(sys.argv[3])
#总本息
pi = float(sys.argv[4])


if mod == '1':
 #usage
 #python ma.py 模型 期数（按月） 总本金 本息和
 #蚂蚁借呗号称日利率万三 一万借六个月需要还10334.17(由于第一个月的还款额超过一个月，故偏多)
 #python ma.py 1 6 10000 10334.17
 #年化利率=11.37%

 #房贷借100w 借5年 还款112.541472w
 #python ma.py 1 60 1000000 1125414.72
 #年化利率=4.75%
  args=[1]
  for i in range(1,month):
    args.append(0)
  args.append(-1-principal/pi*month)
  args.append(principal/pi*month)
  result =  np.roots(args)

  x = 12*((np.real(result[len(result)-1])**-1)-1)*100
  print ("%.2f%%"%(x))
elif mod == '2':
 #usage
 #房贷借100w 借5年 还款112.072917w
 #python ma.py 2 60 1000000 1120729.17
 #年化利率=4.75%
  print ("%.2f%%"%(12*(pi-principal)*2/(month+1)/principal*100))
elif mod == '3' or mod == '4':
 #usage
 #蚂蚁借呗一万借6个月 还10555
 #python ma.py 4 6 10000 10555
 #年化利率=4.75%
  print ("%.2f%%"%((pi/principal-1)/month*12*100))
else:
  print "ERROR"

