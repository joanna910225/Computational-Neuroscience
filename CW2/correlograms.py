# coursework 2 q2 and 3
import matplotlib.pyplot as plt
from numpy import *
import math
# for loading neuron 1 - 4 and time
f = open("neuron1.csv")
neuron1 = map( lambda x: float(x.strip()), f.readlines() )
f = open("neuron2.csv")
neuron2 = map( lambda x: float(x.strip()), f.readlines() )
f = open("neuron3.csv")
neuron3 = map( lambda x: float(x.strip()), f.readlines() )
f = open("neuron4.csv")
neuron4 = map( lambda x: float(x.strip()), f.readlines() )

limit = 10000 # 1 sec

def correlograms(neuronx,neurony):
	diffarray = []
	for i,timepoint1 in enumerate(neuronx):
		for j,timepoint2 in enumerate(neurony):
			diffarray.append(timepoint1 - timepoint2)

	diffarray.sort()

	############### calculate frequency #########################
	outputx = []
	outputy = []
	outputx.append(diffarray[0])
	count = 1
	for i,t in enumerate(diffarray):
		if i > 0:
			if t == diffarray[i-1]:
				count = count + 1
			else:
				outputx.append(t)
				outputy.append(count)
				count = 1
	outputy.append(count)


	############### apply 1sec limit to the array #################
	preparex = []
	preparey = []
	for j,k in enumerate(outputx):
		if abs(k) <= limit:
			preparex.append(k)
			preparey.append(outputy[j])

	#print preparex[0]
	#print preparex[-1]
	########## Classification  ############
	delta = 100
	levelarray = []
	freqarray = []
	count = 0 #sequence number of levelarray and freqarray
	levelarray.append( -(int(abs( preparex[0] ) / delta)+1)*delta) # add first element to level array
	freqarray.append(outputy[0])
	for i,number in enumerate(preparex):
		if number != 0:
			level = int(abs(number) / delta)+1
		else:
			level = 0
		#print level
		if level == abs(levelarray[count])/delta:
			freqarray[count] = freqarray[count] + preparey[i]
		else:
			if number < 0:
				level = -1 * level
			#print(level*delta)
			levelarray.append(level*delta)
			freqarray.append(preparey[i])
			count = count + 1
	return levelarray,freqarray

################# plot auto correlograms ##################################
names = locals()
fig1 = plt.figure(1)
for i in range (1,5):
	vals,freqs = correlograms(names['neuron'+str(i)],names['neuron'+str(i)])
	plt.subplot( 4,1,i)
	plt.bar(vals,freqs,50,color = 'black')
	plt.grid(True)
	plt.title('Neuron '+ str(i))

fig1.suptitle('Auto-Correlograms')
fig1.subplots_adjust(hspace = 0.5)
#plt.savefig('auto-correlogram.png')


################ plot cross correlograms ################################

n=1
fig2 = plt.figure(2)
#fig1,bx = plt.subplots(nrows = 4, ncols = 3, sharex = True,sharey = True)
for i in range(1,5):
	for j in range(1,5):
		if i != j:
			vals,freqs = correlograms(names['neuron'+str(i)],names['neuron'+str(j)])
			plt.subplot( 4,3,n )
			plt.bar(vals,freqs, 50,color = 'black')
			plt.grid(True)
			plt.title('Neuron ' + str(i) + ' -- ' + 'Neuron ' + str(j))
			n = n+1

fig2.suptitle('Cross-Correlograms')
fig2.subplots_adjust(hspace = 0.5)			

plt.show()		