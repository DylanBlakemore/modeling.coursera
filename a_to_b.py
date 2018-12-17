randomNumberList = [0.800, 0.801, 0.752, 0.661, 0.169, 0.956, 0.949, 0.003, 0.201, 0.291, 0.615, 0.131, 0.241, 0.685, 0.116, 0.241, 0.849]

dt = 2

k = [0.2, 0.2]

nA = 4
nB = 3

def choose_particle(_nA, _nB, i):
	rand_num = randomNumberList[i]
	if rand_num < float(_nA)/float(_nA + _nB):
		return 0
	else:
		return 1  

def do_transform(choice, i):
	return randomNumberList[i*2 + 1] < k[choice] * dt

for i in range(0, 7):
	particle = choose_particle(nA, nB, i)
	transform = do_transform(particle, i)
	if particle == 0 and transform == True:
		nB = nB + 1
		nA = nA - 1
	elif particle == 1 and transform == True:
		nA = nA + 1
		nB = nB - 1

print(nA)
print(nB)