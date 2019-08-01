import os
#get the current working directory 
currentdir = os.getcwd();
#Created a folder unwrapped in C:\current working directory\
#NameError: name 'currdir' is not defined
#changed currdir to currentdir
fulloutputpath = currdir + '\\unwrapped\\';
#fulloutputpath = currentdir + '\\unwrapped\\';

#it will return true becuase C:\current working directory\unwrapped already exist
if(os.path.exists(fulloutputpath) is False):
    os.mkdir(fulloutputpath);

    
#C:\Users\Senai\Desktop\expin\sample#1
filetounwrap = input('Enter the full path to the file you want to unwrap:');

#a null value
all_lines = None

#read all lines in the file(C:\Users\Senai\Desktop\expin\sample#1)
if(os.path.exists(filetounwrap)):
    with open(filetounwrap,'r') as lines:
        all_lines = lines.readlines();
 
#writing to unwrapped.txt
    unwrapped = unwrap(all_lines);
    with open(fulloutputpath + 'unwrapped.txt','w') as clean:
        for line in unwrapped:
            clean.write(line);
            clean.write('\n');

#Implement
#function named unwrap
#I dont understand what the function is creating to do
def unwrap(lines):
    cleaned = []
    for line in lines:
        
        #implement here
    
    return cleaned;
