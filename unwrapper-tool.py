

import os

#get the current working directory 

currentdir = os.getcwd();

#Created a folder unwrapped in C:\current working directory\

#NameError: name 'currdir' is not defined ---> [you're getting this error because you didn't change currentdir to currdie on line 3]

#changed currdir to currentdir





fulloutputpath = currentdir + '\\unwrapped\\';

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
def unwrap(lines):

    filterlist = ['@D'] # Use / change this list to specify the characters you need to strip out

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
        
            # >> Why are you looking for the character in filterlist ? 
            # >> Remember that you're looking to see if you can find any element contained in
            # >> filterlist on the line itself. 
            # >> So you have to check the left and right side of each line to see if it matches any element in filterlist
            # >> and if you find it, you have to strip it off the line.
            # >> Below you're saying if I find @D in filterlist then do something to line, which doesnt make sense
            # >> because of course @D is in filterlist .... it's been declared in line 60.            
            if '@D' in filterlist:
                cleaned.append(line.rstrip()) # >> You're getting close. rstrip and lstrip can have arguements
                                              # >> All you have to do is rstrip and lstrip the character you need stripped
                    
            # >> You could do this:
            #
            #    linesize = len(line) - 1
            #    leftside = line[0:2]   # This performs a substring from line start to element number 2 of the line
            #    rightside = line[linesize - 2 :  linesize]  # This performs a substring from the second to the last element
                                                             # to the last element
            #    if leftsdie in filterlist:
            #       do something here ...
            #    if rightside in filterlist:
            #       do something here ....
            
            
        #    for all characters that you find in the filterlist
        #    strip it off line
        #    and store the newly stripped line into a list called cleaned

    

    return cleaned;


#writing to unwrapped.txt

    unwrapped = unwrap(all_lines);

    with open(fulloutputpath + 'unwrapped.txt','w') as clean:

        for line in unwrapped:

            clean.write(line);

            clean.write('\n');
