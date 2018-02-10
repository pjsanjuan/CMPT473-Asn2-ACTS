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
expectedMessagePath = 'TestData/ExpectedMessages/'
testNum = 1

print '\njson2csv program Testing'
print '-----------------------------------------'

def getfileName(fileName):
	global testNum
	return ('test' + str(testNum) + '_' + fileName);


def runJSONToCSV(csvFields, inputFile):
	outputMessageFile = outputMessagePath + getfileName('message.txt')
	outputFile = outputFilePath + getfileName('output.csv')
	cmd = 'json2csv -k ' + csvFields + ' -i ' + inputFilePath + inputFile + ' -o ' + outputFile
	print 'running cmd ' + cmd + '\n'
	createMessageOutput(cmd + '\n\n')
	os.system(cmd  + ' >> ' + outputMessageFile)
	return; 


def compareFilesOutput_pythonCMP():
	outputFile = outputFilePath + getfileName('output.csv')
	expectedOutputFile = expectedOutputPath + getfileName('ExpectedOutput.csv')
	outputMessageFile = outputMessagePath + getfileName('message.txt')
	expectedMessageFile = expectedMessagePath + getfileName('ExpectedMessage.txt')

	cmd = 'diff ' + outputFile + ' ' + expectedOutputFile
	print 'running cmd ' + cmd + '\n'
	addMessageOutput(cmd + '\n\n')
	os.system(cmd + ' >> ' + outputMessageFile)

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

	compareExpectedMessageOutput(outputMessageFile, expectedMessageFile)
	return; 

def createMessageOutput(cmd):
	global testNum
	with io.FileIO(outputMessagePath + getfileName('message.txt'), 'w') as file:
			file.write(cmd)


def addMessageOutput(message):
	global testNum
	with io.FileIO(outputMessagePath + getfileName('message.txt'), 'a') as file:
			file.write(message)


def compareExpectedMessageOutput(messageFile, expectedMessageFile):
	messageIsSame = filecmp.cmp(messageFile, expectedMessageFile)
	if messageIsSame:
		message = 'Both messages are same'
		print message
	else:
		message = 'Messages are different'
		print message
	return; 


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
#VALID_JSON_PATH = , FILE_CONTENTS = , EACH_ROW_HAS_ONE_JSON_OBJECT = , FIELDS_EXIST_IN_JSON_OBJ = 
testFrame('Testing Empty File, Valid Json file Path', 'nonExistentFile', 'test1_input.json')

#test 2
#VALID_JSON_PATH = , FILE_CONTENTS = , EACH_ROW_HAS_ONE_JSON_OBJECT = , FIELDS_EXIST_IN_JSON_OBJ = 
testFrame('Testing Empty File, Invalid Json file Path', 'user.name,remote_ip', 'nonExistentFile.json')

# #test 3
#VALID_JSON_PATH = , FILE_CONTENTS = , EACH_ROW_HAS_ONE_JSON_OBJECT = , FIELDS_EXIST_IN_JSON_OBJ = 
testFrame('Testing something', 'user.name,remote_ip', 'test3_input.json')

# #test 4
#VALID_JSON_PATH = , FILE_CONTENTS = , EACH_ROW_HAS_ONE_JSON_OBJECT = , FIELDS_EXIST_IN_JSON_OBJ = 
# testFrame('Testing something', 'user.name,remote_ip', 'test4_input.json')

# #test 5
#VALID_JSON_PATH = , FILE_CONTENTS = , EACH_ROW_HAS_ONE_JSON_OBJECT = , FIELDS_EXIST_IN_JSON_OBJ = 
# testFrame('Testing something', 'user.name,remote_ip', 'test5_input.json')

# #test 6
#VALID_JSON_PATH = , FILE_CONTENTS = , EACH_ROW_HAS_ONE_JSON_OBJECT = , FIELDS_EXIST_IN_JSON_OBJ = 
# testFrame('Testing something', 'user.name,remote_ip', 'test6_input.json')

# #test 7
#VALID_JSON_PATH = , FILE_CONTENTS = , EACH_ROW_HAS_ONE_JSON_OBJECT = , FIELDS_EXIST_IN_JSON_OBJ = 
# testFrame('Testing something', 'user.name,remote_ip', 'test7_input.json')

# #test 8
#VALID_JSON_PATH = , FILE_CONTENTS = , EACH_ROW_HAS_ONE_JSON_OBJECT = , FIELDS_EXIST_IN_JSON_OBJ = 
# testFrame('Testing something', 'user.name,remote_ip', 'test8_input.json')









