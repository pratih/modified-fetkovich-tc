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
scale = 3
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

# # 7. extra     
# ====================
# math equation using LATEX     
plt.xlabel(r'$t_{Dsf}$', fontsize=20)
plt.ylabel(r'$\left(\frac{s_f}{x_f}\right)q_D$', fontsize=20)
print('7. extra  ')

# show plot
plt.show()