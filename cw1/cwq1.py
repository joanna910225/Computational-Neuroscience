#cousework1 question 1
import matplotlib.pyplot as plt
#from numpy import *
import math


## time parameters
T 		= 1000 						# total time (msec)
dt 		= 1          				# time step
time 	= range(0, T+dt, dt) 		# time array

## model properties
Vt      = zeros(len(time))			# potential over each time step
EL 		= -70 						# leak potential (mV)
Vr 		= -70 						# rest voltage (mV)
Vt 		= -40 						# threshold voltage of spike (mV)
Rm 		= 10 						# resistance (mohm)
tau_m 	= 10 						# time constant (msec)
Ie 		= 3.1 						# input current (nA)
V_inf 	= EL + Rm * Ie
Vt0 	= EL
## model function
for i, t in enumerate(time):
	Vt[i+1] = V_inf + [Vt0 - V_inf] * exp(time/tau_m)
	if Vt[i+1] >= Vt:
		Vt[i+1] = Vr

## plot
plot(time,Vt)
title('Integrate and Fire Model')
Ylabel('Membrane Potential (V)')
Xlabel('Time (msec)')
#ylim([0,2])
show()