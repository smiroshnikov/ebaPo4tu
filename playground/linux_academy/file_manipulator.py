FILE_OLD = 'xmen_base'
FILE_NEW = 'new_xmen_base'

xb = open(FILE_OLD, 'r')
print(xb.read())
print("file is read 1 time!")
xb.seek(0)
print("file is read 2nd time!")
xb.read()
if len(xb.read()) is 0:
    print("Condition procs  !")

xb.seek(0)
for line in xb:
    print(line, end="")

nxb = open('new_xmen_base', 'w')  # if opening a file that already exists will truncate it .
xb.seek(0)  # omitting this line will result in reading EOF during for loop

# nxb.write(xb.read())  # is exactly the same
print("\nCreating a new file ! -> \n")
for line in xb:
    nxb.write(line)

nxb.close()
xb.close()

nxb = open(FILE_NEW)
print("\n" + nxb.read())
nxb.close()

tf = open('test_file', 'w')
tf.write("Test1")
tf.write("Test2")
tf.write("dont forget newline 1 \n")
tf.write("dont forget newline 2 \n")
tf.write("dont forget newline 3 \n")
tf.write("dont forget newline 4 \n")
tf.write("dont forget newline 5 \n")
tf.write("dont forget newline and close file \n")
tf.close()
if tf.closed:
    print("File closed!")

# reading and writing
# r+

print("\nNEW FILE STARTED -----------------READ AND WRITE MODE !---------------->\n")
tf = open('test_file', 'r+')
print(tf.read())
tf.seek(0)
tf.write("another Line at the beginning due to seek(0) as argument\n")
tf.write("and another Line right after(below)  first written\n")
tf.seek(0)
print(tf.read())
print("File is horrible overwritten , add new lines to the end next time ")
tf.close()

# a better way with auto close as well

with open(FILE_OLD, 'a') as f:
    f.write("Sergey Miroshnkov\n")
# file is closed here
#print(f.read())  # this is causing an exception , pay attention "f" exists in thi scope
# a better way

mega_F = open(FILE_OLD, 'a')
with mega_F:
    mega_F.write("Troy Miroshnikov\n")
print(mega_F.read()) # exception  , file is closed!
