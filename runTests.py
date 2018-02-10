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

print '\njson2csv program ACTS Testing'
print '=============================================================='

def buildTestFileName(fileName):
	global testNum
	return ('test' + str(testNum) + '_' + fileName);

def createMessageOutput(cmd):
	global testNum
	with io.FileIO(outputMessagePath + buildTestFileName('message.txt'), 'w') as file:
			file.write(cmd)


def addMessageOutput(message):
	global testNum
	with io.FileIO(outputMessagePath + buildTestFileName('message.txt'), 'a') as file:
			file.write(message)


def runJSONToCSV(csvFields, inputPathFile, outputPathFile):
	outputMessageFile = outputMessagePath + buildTestFileName('message.txt')
	outputFile = outputFilePath + buildTestFileName(outputPathFile)
	inputFile = inputFilePath + buildTestFileName(inputPathFile)
	outputMessageFile = outputMessagePath + buildTestFileName('message.txt')
	expectedMessageFile = expectedMessagePath + buildTestFileName('ExpectedMessage.txt')

	cmd = 'json2csv -k ' + csvFields + ' -i ' + inputFile + ' -o ' + outputFile
	print cmd + '\n'
	createMessageOutput(cmd + '\n\n');

	if os.path.exists(inputFile) == False:
		#file path of input file is incorrect

		message = 'Path to input file is invalid'
		print "Message: " + message
		addMessageOutput(message)
		print '\nMessage is saved to: ' + outputMessageFile

	elif os.path.exists(outputFile) == False:
		#file path of output file is incorrect

		message = 'Path to output file is invalid'
		print "Message: " + message
		addMessageOutput(message)
		print '\nMessage is saved to: ' + outputMessageFile

	else:
		#run system command
		os.system(cmd)

		#compare files
		compareFilesOutput_pythonCMP(outputPathFile)

	#compares message files
	compareExpectedMessageOutput(outputMessageFile, expectedMessageFile)
	return; 


def compareFilesOutput_pythonCMP(outputPathFile):
	outputFile = outputFilePath + buildTestFileName(outputPathFile)
	expectedOutputFile = expectedOutputPath + buildTestFileName('ExpectedOutput.csv')
	outputMessageFile = outputMessagePath + buildTestFileName('message.txt')
	expectedMessageFile = expectedMessagePath + buildTestFileName('ExpectedMessage.txt')

	cmd = 'diff ' + outputFile + ' ' + expectedOutputFile
	print cmd + '\n'
	os.system(cmd)
	addMessageOutput(cmd + '\n\n');

	fileIsSame = filecmp.cmp(outputFile, expectedOutputFile)
	if fileIsSame:
		message = 'Both Expected and Output Files are identical'
		print "Message: " + message
		addMessageOutput(message)
	else:
		message = 'Both Expected and Output Files are different'
		print "Message: " + message
		addMessageOutput(message)

	print '\nMessage is saved to: ' + outputMessageFile
	return; 


def compareExpectedMessageOutput(messageFile, expectedMessageFile):

	cmd = '\ndiff ' + messageFile + ' ' + expectedMessageFile
	print cmd + '\n'
	os.system(cmd)

	messageIsSame = filecmp.cmp(messageFile, expectedMessageFile)
	if messageIsSame:
		message = 'Both Expected and Output Messages are identical, TEST PASSED!'
		print message
	else:
		message = 'Both Expected and Output Messages are different, TEST FAILED!'
		print message
	return; 


def testFrame(testName, csvFields, inputFile, outputPathFile):
	global testNum
	print '\n\n[Test: ' + str(testNum) + ' - ' + testName + ']'
	print '=============================================================='
	runJSONToCSV(csvFields, inputFile, outputPathFile)
	testNum += 1
	return;


#do testing here

# test 1 
# output file should be empty as input file is empty 
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = EMPTY, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = FALSE
testFrame('Testing Valid Input Path, Empty File', 'nonExistentField', 'input.json', 'output.csv')


# test 2 
# output file should be empty as invalid path
#VALID_JSON_PATH = FALSE, FILE_CONTENTS = EMPTY, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = FALSE
testFrame('Testing Invalid Input Path, Empty File', 'nonExistentField', 'invalidPath/nonExistentFile.json', 'output.csv')


# test 3
# outputs a generated csv file from json
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = MULTIPLE_ROWS, ALL_VALID_JSON_OBJECTS = TRUE, EACH_ROW_HAS_ONE_JSON_OBJECT = TRUE, FIELDS_EXIST_IN_JSON_OBJ = TRUE, VALID_OUTPUT_PATH = TRUE
testFrame('Testing Valid Input Path, Multiple Rows File, Valid Json Obj, Each row has one jason Obj, Fields exist in Json Obj, Valid Output Path', 'user.name,remote_ip', 'input.json', 'output.csv')


# test 4 
# output file should be empty as invalid path
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = SINGLE_ROW, ALL_VALID_JSON_OBJECTS = TRUE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = TRUE, VALID_OUTPUT_PATH = FALSE
testFrame('Testing Valid Input Path, Single Row File, Valid Json Obj, Each row does not have one jason Obj, Fields exist in Json Obj, Invalid Output Path', 'user.name,remote_ip', 'input.json', 'invalidPath/nonExistentFile.csv')


# test 5
# output file should be empty as invalid path
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = MULTIPLE_ROWS, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = TRUE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = FALSE
testFrame('Testing Valid Input Path, Multiple Rows File, Invalid Json Obj, Each row has one jason Obj, Fields do not exist in Json Obj, Invalid Output Path', 'nonExistentField,nonExistentField2', 'input.json', 'invalidPath/nonExistentFile.csv')


# test 6
# output file should be empty as invalid json
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = SINGLE_ROW, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = TRUE, FIELDS_EXIST_IN_JSON_OBJ = TRUE, VALID_OUTPUT_PATH = TRUE
testFrame('Testing Valid Input Path, Single Row File, Invalid Json Obj, Each row has one jason Obj, Fields exist in Json Obj, Valid Output Path', 'user.name,remote_ip', 'input.json', 'output.csv')



# test 7
# output file should be empty as each row has one json object is false
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = MULTIPLE_ROWS, ALL_VALID_JSON_OBJECTS = TRUE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = TRUE, VALID_OUTPUT_PATH = TRUE
testFrame('Testing Valid Input Path, Multiple Rows File, Invalid Json Obj, Each row does not have one jason Obj, Fields exist in Json Obj, Valid Output Path', 'user.name', 'test7_input.json', 'invalidPath/nonExistentFile.csv')


# test 8
# output file should be empty as all valid json object is false and each row has one is false
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = SINGLE_ROW, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = TRUE
testFrame('Testing Valid Input Path, Single Row File, Invalid Json Obj, Each row does not have one jason Obj, Fields do not exist in Json Obj, Valid Output Path', 'nonExistentField', 'test8_input.json', 'output.csv')



# test 9
# output file should be empty as all conditions are false
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = EMPTY, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = FALSE
testFrame('Testing Valid Input Path, Empty Field, Invalid Json Obj, Each row does not have one jason Obj, Fields do not exist in Json Obj, Invalid Output Path', 'nonExistentField,nonExistentField2', 'test9_input.json', 'output.csv')




