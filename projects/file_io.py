
#first argument is the path then the mode
#remember to close the files (file_handle.close)
#open and write or open and read, don't try to do both.
file_handle = open('hello.txt', 'w')
file_handle.write('hello\n')
file_handle.write('goodbye\n')
file_handle.close()
