from subprocess import call

command = 'D:\Libraries\opencv\build\x86\vc12\bin\opencv_traincascade.exe'
positive = ' -vec newfile.vec '
negative = ' -bg bg.txt '
catalog = ' -data newcascade'
stages = ' -numStages '
nPos = ' -numPos '
nNeg = ' -numNeg '
mode = ' -mode '
far = ' -maxFalseAlarmRate'
modes = ['BASIC', 'CORE', 'ALL']
positives = dict('BASIC'=300, 'CORE'=250, 'ALL'=150)
negatives = dict('BASIC'=500, 'CORE'=350, 'ALL'=250)
for st in range (1,10,5)
	for jm in modes
		for i in range(1,5)
			call([command, positive, negative, catalog + '1' + jm, mode + jm, nPos + positives[jm], nNeg + negatives[jm],stages + st])