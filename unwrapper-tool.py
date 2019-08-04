import os
#get the current working directory 
currentdir = os.getcwd();
#Created a folder unwrapped in C:\current working directory\
#NameError: name 'currdir' is not defined ---> [you're getting this error because you didn't change currentdir to currdie on line 3]
#changed currdir to currentdir


fulloutputpath = currdir + '\\unwrapped\\';
#fulloutputpath = currentdir + '\\unwrapped\\';

#it will return true becuase C:\current working directory\unwrapped already exist
if(os.path.exists(fulloutputpath) is False):
    os.mkdir(fulloutputpath);

    
#C:\Users\Senai\Desktop\expin\sample#1.txt
filetounwrap = input('Enter the full path to the file you want to unwrap:');

#a null value
all_lines = None

#read all lines in the file(C:\Users\Senai\Desktop\expin\sample#1)
if(os.path.exists(filetounwrap)):
    with open(filetounwrap,'r') as lines:
        all_lines = lines.readlines();
  #all_lines = the expin
 #The function needs to be on this line

#writing to unwrapped.txt
    unwrapped = unwrap(all_lines);
    with open(fulloutputpath + 'unwrapped.txt','w') as clean:
        for line in unwrapped:
            clean.write(line);
            clean.write('\n');

#Implement
#function named unwrap
#I dont understand what the function is trying to do
# This is the main function that unwraps the expin
def unwrap(lines):
    filterlist = ['@1','@2','@3'] # Use / change this list to specify the characters you need to strip out
    cleaned = []   # declare a  list to hold each line
    
    # The below statement is just a loop.
    # it's the same as saying:
    # for index in range(0,len(lines)):
    #    lines[index] ... etc
    # the way the loop is written below, you dont need to keep track of the array index.
    for line in lines:
        # pseudocode:
        #  for each line variable,
        #    check if it contains any character specified in the filterlist 
        #    for all characters that you find in the filterlist
        #    strip it off line
        #    and store the newly stripped line into a list called cleaned
    
    return cleaned;
