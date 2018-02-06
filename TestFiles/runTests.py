import os
#from subprocess import call

#global variables
inputFilePath = 'input/'
outputFilePath = 'output/'


print 'Starting json to csv testing'
print '-----------------------------------------'

def callTest(inputFile, outputFile):
	cmd = 'json2csv -k user.name,remote_ip -i ' + inputFilePath + inputFile + ' -o ' + outputFilePath + outputFile
	print 'running command: ' + cmd
	os.system(cmd)
	return; 


print '\ntest 0'
callTest('input.json', 'output.csv')





