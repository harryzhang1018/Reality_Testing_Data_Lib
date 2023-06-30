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



def data_read(filename):
    data = genfromtxt(filename, delimiter=',')
    return data

foldername = './test_0630/'
filename = 'l17_0630_r3.csv'
file = foldername + filename

data = data_read(file)
rx = data[:,0]
ry = data[:,1]
gtx = data[:,2]
gty = data[:,3]
EKFx = data[:,4]
EKFy = data[:,5]

plt.figure(figsize=(5,10))
plt.plot(ref_x,ref_y,'--',label='reference trajectory')
# plt.plot(rx,ry,label='gps')
plt.plot(gtx,gty,label='rtk gps')
# plt.plot(EKFx,EKFy,label='state estimation')
plt.legend()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.tight_layout()
plt.title('lot 17')
#plt.show()

if show_sim_res:
    sim_res = genfromtxt('/home/harry/Documents/test_plot/wpts_mpc/data/lot17_sim.csv', delimiter=',')
    x = sim_res[:,0]
    y = sim_res[:,1]
    #plt.plot(ref_x,ref_y,'--',label='reference trajectory')
    plt.plot(x,y,label='trajectory using previliged information')

plot_profile = True
if plot_profile:
    plt.figure()
    plt.subplot(3,1,1)
    plt.plot(range(data[:,10].shape[0]),data[:,6],label='heading from imu')
    plt.legend()
    plt.subplot(3,1,2)
    plt.plot(range(data[:,8].shape[0]),data[:,8],label='throttle')
    plt.legend()
    plt.subplot(3,1,3)
    plt.plot(range(data[:,9].shape[0]),data[:,9],label='steering')
    plt.legend()
plt.tight_layout()
plt.show()