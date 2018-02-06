import os
#from subprocess import call

#global variables
inputFilePath = 'input/'
outputFilePath = 'output/'
correctValueFilePath = 'correctValues/'
testNum = 0

print '\nStarting json to csv Testing'
print '-----------------------------------------'

def callTest(csvFields, inputFile, outputFile):
	cmd = 'json2csv -k ' + csvFields + ' -i ' + inputFilePath + inputFile + ' -o ' + outputFilePath + outputFile
	print 'running cmd: ' + cmd
	os.system(cmd)
	return; 

def compareValues(correctValueFile, outputFile):
	cmd = 'diff ' + correctValueFilePath + correctValueFile + ' ' + outputFilePath + outputFile
	print 'running cmd: ' + cmd
	os.system(cmd)
	return; 


def testSuite(testName, csvFields, inputFile, outputFile, correctValueFile):
	global testNum
	print '\n [Test: ' + str(testNum) + ' ' + testName + ']'
	print '-----------------------------------------'
	callTest(csvFields, inputFile, outputFile)
	compareValues(correctValueFile, outputFile)
	testNum += 1
	return;


#do testing here
testSuite('default Test', 'user.name,remote_ip', 'input.json', 'output.csv', 'outputCorrect.csv')









