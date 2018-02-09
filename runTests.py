import os
import io
import filecmp

#from subprocess import call
#Authors: Jordan Ho, Patrick San Juan

# project is constructed using https://github.com/jehiah/json2csv
#command: json2csv 

#global variables
inputFilePath = 'TestData/TestFiles/TestInput/Files/'
outputFilePath = 'TestData/TestFiles/TestOutput/Files/'
outputMessagePath = 'TestData/TestFiles/TestOutput/Messages/'
expectedOutputPath = 'TestData/ExpectedOutput/'
testNum = 1

print '\njson2csv program Testing'
print '-----------------------------------------'

def getfileName(fileName):
	global testNum
	return ('test' + str(testNum) + '_' + fileName);


def runJSONToCSV(csvFields, inputFile):
	outputFile = outputFilePath + getfileName('output.csv')
	cmd = 'json2csv -k ' + csvFields + ' -i ' + inputFilePath + inputFile + ' -o ' + outputFile
	print 'running cmd' + cmd + '\n'
	os.system(cmd)
	return; 


def compareFilesOutput_pythonCMP():
	outputFile = outputFilePath + getfileName('output.csv')
	expectedOutputFile = expectedOutputPath + getfileName('ExpectedOutput.csv')
	outputMessageFile = outputMessagePath + getfileName('message.txt')

	cmd = 'diff -q ' + outputFile + ' ' + expectedOutputFile
	print 'running cmd' + cmd + '\n'
	os.system(cmd + ' > ' + outputMessageFile)

	print 'test message is output to ' + outputMessageFile + '\n'

	fileIsSame = filecmp.cmp(outputFile, expectedOutputFile)
	if fileIsSame:
		message = 'Both Files are identical, TEST PASSED'
		print message
		addMessageOutput(message)
	else:
		message = 'Files are different, TEST FAILED'
		print message
		addMessageOutput(message)
	return; 


def addMessageOutput(message):
	global testNum
	with io.FileIO(outputMessagePath + getfileName('message.txt'), 'a') as file:
			file.write(message)


def testFrame(testName, csvFields, inputFile):
	global testNum
	print '\n 	[Test: ' + str(testNum) + ' - ' + testName + ']'
	print '-----------------------------------------'
	runJSONToCSV(csvFields, inputFile)
	compareFilesOutput_pythonCMP()
	testNum += 1
	return;


#do testing here
#testFrame('Test name', 'field1,field2', 'input.json')

#test 1
testFrame('Testing something', 'user.name,remote_ip', 'test1_input.json')

#test 2
#TODO
#.....







