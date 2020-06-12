import numpy as np
import os
import time
import matplotlib.pyplot as plt
#from pynput.keyboard import Key, Controller
  
def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=","")
    temp = int(temp.replace(".0'C",""))
    return (temp)

def measure_cpu():
    cpu0 = os.popen("awk '{print $1}' /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").readline()
    return (int(int(cpu0)/1000))

tik = 0
TimeArray = np.array([])
TempArray = np.array([])
CpuArray = np.array([])

#os.system('stress-ng --cpu 0 --cpu-method fft')
#os.system('glxgears -fullscreen')
#os.system('glxgears')
#time.sleep(3)
'''
keyboard = Controller()
keyboard.press(Key.alt)
keyboard.press(Key.f4)
keyboard.release(Key.alt)
keyboard.release(Key.f4)
'''
start = time.time()

while time.time() - start < 800:  
#while tik < 180:
  
    TimeArray = np.append(TimeArray, round(time.time() - start))
    TempArray = np.append(TempArray, measure_temp())
    CpuArray = np.append(CpuArray, measure_cpu())
  
    time.sleep(1)
    #tik = tik + 1
      

  
print(TimeArray)
print(TempArray)
print(CpuArray)

# Create some mock data
#t = np.arange(0.01, 10.0, 0.01)
#data1 = np.exp(t)
#data2 = np.sin(2 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('CPU performance (kHz)', color=color)
ax1.plot(TimeArray, CpuArray, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('CPU temperature', color=color)  # we already handled the x-label with ax1
ax2.plot(TimeArray, TempArray, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
ax1.grid()
plt.show()

