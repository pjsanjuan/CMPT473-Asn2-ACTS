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

def createMessageOutput(cmd):
	global testNum
	with io.FileIO(outputMessagePath + getfileName('message.txt'), 'w') as file:
			file.write(cmd)


def addMessageOutput(message):
	global testNum
	with io.FileIO(outputMessagePath + getfileName('message.txt'), 'a') as file:
			file.write(message)


def runJSONToCSV(csvFields, inputPathFile, outputPathFile):
	outputMessageFile = outputMessagePath + getfileName('message.txt')
	expectedMessageFile = expectedMessagePath + getfileName('ExpectedMessage.txt')
	outputMessageFile = outputMessagePath + getfileName('message.txt')
	outputFile = outputFilePath + getfileName(outputPathFile)
	inputFile = inputFilePath + inputPathFile

	cmd = 'json2csv -k ' + csvFields + ' -i ' + inputFile + ' -o ' + outputFile
	print 'running cmd ' + cmd + '\n'
	createMessageOutput(cmd + '\n\n');

	if os.path.exists(inputFile) == False:
		#file path of input file is incorrect
		print 'test message is output to ' + outputMessageFile + '\n'

		message = 'Path to input file is invalid'
		print message
		addMessageOutput(message)
	elif os.path.exists(outputFile) == False:
		#file path of output file is incorrect
		print 'test message is output to ' + outputMessageFile + '\n'

		message = 'Path to output file is invalid'
		print message
		addMessageOutput(message)
	else:
		#run system command
		os.system(cmd)

		#compare files
		compareFilesOutput_pythonCMP(outputPathFile)

	compareExpectedMessageOutput(outputMessageFile, expectedMessageFile)
	return; 


def compareFilesOutput_pythonCMP(outputPathFile):
	outputFile = outputFilePath + getfileName(outputPathFile)
	expectedOutputFile = expectedOutputPath + getfileName('ExpectedOutput.csv')
	outputMessageFile = outputMessagePath + getfileName('message.txt')
	expectedMessageFile = expectedMessagePath + getfileName('ExpectedMessage.txt')

	cmd = 'diff ' + outputFile + ' ' + expectedOutputFile
	print 'running cmd ' + cmd + '\n'

	os.system(cmd)
	addMessageOutput(cmd + '\n\n');

	#os.system(cmd + ' >> ' + outputMessageFile)

	print 'test message is output to ' + outputMessageFile + '\n'

	fileIsSame = filecmp.cmp(outputFile, expectedOutputFile)
	if fileIsSame:
		message = 'Both Files are identical'
		print message
		addMessageOutput(message)
	else:
		message = 'Both Files are different'
		print message
		addMessageOutput(message)
	return; 


def compareExpectedMessageOutput(messageFile, expectedMessageFile):

	print '\ncomparing message to expected message: \n'
	print messageFile + '\n'
	print expectedMessageFile + '\n'

	messageIsSame = filecmp.cmp(messageFile, expectedMessageFile)
	if messageIsSame:
		message = 'Both messages are identical, TEST PASSED!'
		print message
	else:
		message = 'Both Messages are different, TEST FAILED!'
		print message
	return; 


def testFrame(testName, csvFields, inputFile, outputPathFile):
	global testNum
	print '\n[Test: ' + str(testNum) + ' - ' + testName + ']'
	print '-----------------------------------------'
	runJSONToCSV(csvFields, inputFile, outputPathFile)
	testNum += 1
	return;


#do testing here
#testFrame('Test name', 'field1,field2', 'input.json')

#test 1  
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = EMPTY, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = FALSE
testFrame('Testing Valid Input Path, Empty File', 'nonExistentField', 'test1_input.json', 'output.csv')


# #test 2
#VALID_JSON_PATH = FALSE, FILE_CONTENTS = EMPTY, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = FALSE
testFrame('Testing Invalid Input Path, Empty File', 'nonExistentField', 'invalidPath/nonExistentFile.json', 'output.csv')


# # #test 3
#VALID_JSON_PATH = TRUE, FILE_CONTENTS = MULTIPLE_ROWS, ALL_VALID_JSON_OBJECTS = TRUE, EACH_ROW_HAS_ONE_JSON_OBJECT = TRUE, FIELDS_EXIST_IN_JSON_OBJ = TRUE, VALID_OUTPUT_PATH = TRUE
testFrame('Testing Valid Input Path, Multiple Rows File, Valid Json Obj, Each row has one jason Obj, Fields exist in Json Obj, Valid Output Path', 'user.name,remote_ip', 'test3_input.json', 'output.csv')


# # #test 4
# #VALID_JSON_PATH = TRUE, FILE_CONTENTS = SINGLE_ROW, ALL_VALID_JSON_OBJECTS = TRUE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = TRUE, VALID_OUTPUT_PATH = FALSE
# testFrame('Testing Valid Input Path, Single Row File, Valid Json Obj, Each row does not have one jason Obj, Fields exist in Json Obj, Invalid Output Path', 'user.name,remote_ip', 'test4_input.json', 'invalidPath/nonExistentFile.csv')


# # #test 5
# #VALID_JSON_PATH = TRUE, FILE_CONTENTS = MULTIPLE_ROWS, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = TRUE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = FALSE
# testFrame('Testing Valid Input Path, Multiple Rows File, Invalid Json Obj, Each row has one jason Obj, Fields do not exist in Json Obj, Invalid Output Path', 'nonExistentField,nonExistentField2', 'test5_input.json', 'invalidPath/nonExistentFile.csv')


# # #test 6
# #VALID_JSON_PATH = TRUE, FILE_CONTENTS = SINGLE_ROW, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = TRUE, FIELDS_EXIST_IN_JSON_OBJ = TRUE, VALID_OUTPUT_PATH = TRUE
# testFrame('Testing Valid Input Path, Single Row File, Invalid Json Obj, Each row has one jason Obj, Fields exist in Json Obj, Valid Output Path', 'user.name,remote_ip', 'test6_input.json', 'output.csv')



# # #test 7
# #VALID_JSON_PATH = TRUE, FILE_CONTENTS = MULTIPLE_ROWS, ALL_VALID_JSON_OBJECTS = TRUE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = TRUE, VALID_OUTPUT_PATH = TRUE
# testFrame('Testing Valid Input Path, Multiple Rows File, Invalid Json Obj, Each row does not have one jason Obj, Fields exist in Json Obj, Valid Output Path', 'user.name,remote_ip', 'test7_input.json', 'invalidPath/nonExistentFile.csv')


# # #test 8
# #VALID_JSON_PATH = TRUE, FILE_CONTENTS = SINGLE_ROW, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = TRUE
# testFrame('Testing Valid Input Path, Single Row File, Invalid Json Obj, Each row does not have one jason Obj, Fields do not exist in Json Obj, Valid Output Path', 'nonExistentField,nonExistentField2', 'test8_input.json', 'output.csv')



# # #test 9
# #VALID_JSON_PATH = TRUE, FILE_CONTENTS = EMPTY, ALL_VALID_JSON_OBJECTS = FALSE, EACH_ROW_HAS_ONE_JSON_OBJECT = FALSE, FIELDS_EXIST_IN_JSON_OBJ = FALSE, VALID_OUTPUT_PATH = FALSE
# testFrame('Testing Valid Input Path, Empty Field, Invalid Json Obj, Each row does not have one jason Obj, Fields do not exist in Json Obj, Invalid Output Path', 'nonExistentField,nonExistentField2', 'test9_input.json', 'output.csv')




