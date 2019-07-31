import os

currentdir = os.getcwd();
fulloutputpath = currdir + '\\unwrapped\\';

if(os.path.exists(fulloutputpath) is False):
    os.mkdir(fulloutputpath);

filetounwrap = input('Enter the full path to the file you want to unwrap:');
all_lines = None

if(os.path.exists(filetounwrap)):
    with open(filetounwrap,'r') as lines:
        all_lines = lines.readlines();
    
    unwrapped = unwrap(all_lines);
    with open(fulloutputpath + 'unwrapped.txt','w') as clean:
        for line in unwrapped:
            clean.write(line);
            clean.write('\n');

#Implement
def unwrap(lines):
    cleaned = []
    for line in lines:
        #implement here
    
    return cleaned;
