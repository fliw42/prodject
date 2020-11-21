file = open('i', 'w')
file.write('HA')


string = 'name' + '.txt'
file = open(string, 'w')

i=0
while i<10000000001:			
	file = open(str(i)+'.txt', 'w')
	file.write('random text \n')
	i=i+1