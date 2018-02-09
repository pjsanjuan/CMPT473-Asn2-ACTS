import os

#from subprocess import call
#Authors: Jordan Ho, Patrick San Juan

# project is constructed using https://github.com/jehiah/json2csv
#command: json2csv 

#global variables
inputFilePath = 'TestData/TestFiles/TestInput/Files/'
outputFilePath = 'TestData/TestFiles/TestOutput/Files/'
expectedOutputPath = 'TestData/ExpectedOutput/'
testNum = 0

print '\njson2csv program Testing'
print '-----------------------------------------'

def runJSONToCSV(csvFields, inputFile, outputFile):
	cmd = 'json2csv -k ' + csvFields + ' -i ' + inputFilePath + inputFile + ' -o ' + outputFilePath + outputFile
	print cmd
	os.system(cmd)
	return; 

def compareFilesOutput(outputFile, expectedOutputFile):
	cmd = 'diff ' + expectedOutputPath + expectedOutputFile + ' ' + outputFilePath + outputFile
	print cmd
	os.system(cmd)
	return; 

def testFrame(testName, csvFields, inputFile, outputFile, expectedOutputFile):
	global testNum
	print '\n 	[Test: ' + str(testNum) + ' - ' + testName + ']'
	print '-----------------------------------------'
	runJSONToCSV(csvFields, inputFile, outputFile)
	compareFilesOutput(outputFile, expectedOutputFile)
	testNum += 1
	return;


#do testing here
#testFrame('Test name', 'field1,field2', 'input.json', 'output.csv', 'outputCorrect.csv')

#test 1
testFrame('Testing something', 'user.name,remote_ip', 'test1_input.json', 'test1_output.csv', 'test1_ExpectedOutput.csv')

#test 2
#TODO
#.....







