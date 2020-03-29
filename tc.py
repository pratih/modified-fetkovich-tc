# Helmi Pratikno
# 3/27/2020
# Displaying Modified Fetkovich Type Curve using Python
# Repo: https://github.com/pratih/modified-fetkovich-tc

# # 0. import external modules
import math 
import pandas as pd 
import matplotlib.pyplot as plt

# # 1. set canvas size
# ====================
xrange = [1e-3,1e2]
yrange = [1e-2,1e2]
xratio = math.log(xrange[1]/xrange[0],10)
yratio = math.log(yrange[1]/yrange[0],10)
# print(xratio)
scale = 2.5
fig= plt.figure(figsize=(xratio*scale,yratio*scale))
print('1. set canvas size')

# # 2. set limit
# ====================
plt.xlim(xrange[0], xrange[1])
plt.ylim(yrange[0], yrange[1])
print('2. set limit')

# # 3. set log scales & fontsize
# ====================
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
# set fontsize on ticks
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
print('3. set log scales & fontsize')

# # 4. set title and labels
# ====================
plt.title('Modified Fetkovich Type Curve', fontsize=25)
plt.xlabel('tDsf', fontsize=20)
plt.ylabel('(sf/xf)qD', fontsize=20)
print('4. set title and labels')

# # 5. get data source
# ====================
filename = 'tc_data.csv'
# read source file
df = pd.read_csv(filename)
# read header
cols = pd.read_csv(filename, nrows=1).columns.tolist()
print('5. get data source')

# # 6. plot series using loop
# ====================
for col in cols:
    # print(col)
    if col != 'tDsf':
      plt.plot(df['tDsf'],df[col])
print('6. plot series using loop')

# # 7. extras     
# ====================
print('7. extras')
# math equation using LATEX     
plt.xlabel(r'$t_{Dsf}$', fontsize=20)
plt.ylabel(r'$\left(\frac{s_f}{x_f}\right)q_D$', fontsize=20)
# annotate bTR
bTR_txts = [r'$b_{TR}=1$', '2', '3', '4']
bTR_ys = [3.58E+01, 7.18, 4.20, 3.1]
bTR_x = 1e-2
for idx, val in enumerate(bTR_txts):
  plt.annotate(val, (bTR_x,bTR_ys[idx]), textcoords="offset points", xytext=(0,-5), ha='center', size=18) 
# annotate bBDF
bBDF_txts = [r'$b_{BDF}=0$', '.2', '.4', '.6', '.8', '1']
bBDF_y = 2e-2
bBDF_xs = [1.22, 3.34, 6, 1.17E+01, 25, 50]
for idx, val in enumerate(bBDF_txts):
  plt.annotate(val, (bBDF_xs[idx],bBDF_y), textcoords="offset points", xytext=(0,-5), ha='center', size=18) 

# show plot
plt.show()