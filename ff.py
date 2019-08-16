# J.R ->>> This will work as a first python project.
# The only comment I have is that it's very specific to only one type of file. Meaning that 
# if the file format ever changed, for example the wrapper length changed, you may need to change the code again.
#    
#  The next step (maybe for a new project later on) is to make it flexible so that you have a list of patterns
#  that you're looking for and removing. If the pattern changes all you have to do is change or add to the list.
#  By doing this, you're script becomes adaptable to many other types of files if needed.
#

import os

#get the current working directory 

currentdir = os.getcwd();

#Created a folder unwrapped in C:\current working directory\

fulloutputpath = currentdir + '\\unwrapped\\';


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


def unwrap(lines):
    
    cleaned = []   # declare a  list to hold each line
#initialize the count variable 
    linecount=0
    
    for line in lines:
        #increment by one and keep track of lines
        linecount=linecount +1
        #
        if linecount >4 and linecount <= len(lines) - 2:
            line = line[2:len(line)]
            line = line[0:len(line)-5]
            cleaned.append(line)
    
    return cleaned
       

unwrapped = unwrap(all_lines)

with open(fulloutputpath + 'unwrapped.txt','w') as clean:

    for line in unwrapped:
        clean.write(line);
        clean.write('\n');
        
clean.close()
