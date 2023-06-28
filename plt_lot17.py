from numpy import genfromtxt
import numpy as np
import sys
sys.path.append('/home/harry/Documents/test_plot/wpts_mpc')
import matplotlib.pyplot as plt

show_sim_res = False
#ref_states = genfromtxt('/home/harry/Documents/test_plot/wpts_mpc/data/Circle_Traj.csv', delimiter=',')
ref_states = genfromtxt('/home/harry/Documents/test_plot/wpts_mpc/data/lot17.csv', delimiter=',')
ref_x = ref_states[:,0]
ref_y = ref_states[:,1]

if show_sim_res:
    sim_res = genfromtxt('/home/harry/Documents/test_plot/wpts_mpc/data/lot17_sim.csv', delimiter=',')
    x = sim_res[:,0]
    y = sim_res[:,1]
    plt.figure(figsize=(5,10))
    plt.plot(ref_x,ref_y,'--',label='reference trajectory')
    plt.plot(x,y,label='trajectory using previliged information')

def data_read(filename):
    data = genfromtxt(filename, delimiter=',')
    return data

filename_1 = './Lot17/l17_r1.csv'
filename_2 = './Lot17/l17_r2.csv'
filename_3 = './Lot17/l17_r3.csv'
filename_4 = './Circle/circle_r1.csv'
filename_5 = './Circle/circle_r2.csv'
filename_6 = './Circle/single_circle.csv'
filename_7 = './Circle/three_circles.csv'

data = data_read(filename_7)
rx = data[:,0]
ry = data[:,1]
gtx = data[:,2]
gty = data[:,3]

plt.figure(figsize=(5,5))
#plt.plot(ref_x,ref_y,'--',label='reference trajectory')
plt.plot(rx,ry,label='gps')
plt.plot(gtx,gty,label='rtk gps')
plt.legend()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
# plt.title('lot 17')
plt.show()