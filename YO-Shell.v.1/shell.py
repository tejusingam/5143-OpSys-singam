#Program Name: Yo-Shell.v.1

import os
import sys
import shutil
import time
import stat

from os.path import expanduser

"""
@Name: historyManager
@Description:
    Maintains a history of shell commands to be used within a shell environment.
@Methods:
    push_command - add command to history
    get_commands - get all commands from history
    number_commands - get number of commands in history
"""
class historyManager(object):
    def __init__(self):
        self.command_history = []

    """
    @Name: push_command
    @Description:
        Add command to history
    @Params:
        cmd (string) - Command added to history
    @Returns: None
    """
    def push_command(self,cmd):
        self.command_history.append(cmd)
        
    """
    @Name: get_commands
    @Description:
        get all commands from history
    @Params: None
    @Returns: None
    """
    def get_commands(self):
        return self.command_history
        
    """
    @Name: number_commands
    @Description:
        get number of commands in history
    @Params: None
    @Returns: 
        (int) - number of commands
    """
    def number_commands(self):
        return len(self.command_history)

"""
@Name: parserManager
@Description:
    Handles parsing of commands into command , arguments, flags.
@Methods:
    parse - does actual parsing of command
"""
class parserManager(object):
    def __init__(self):
        self.parts = []
    """
    @Name: parse
    @Description:
        Parses command into a list (right now). 
    @Params: 
        cmd (string) - The command to be parsed
    @Returns: 
        (int) - number of commands
    """
    def parse(self,cmd):
        self.parts = cmd.split(" ")
        return self.parts
        
"""
@Name: commandManager
@Description:
    Maintains a history of shell commands to be used within a shell environment.
@Methods:
    run_command - Runs a parsed command
    ls - Directory_listing
    cat - File dump
"""
class commandManager(parserManager):
    def __init__(self):
        self.command = None

    """
    @Name: run_command
    @Description:
        Runs a parsed command
    @Params: 
        cmd (string) - The command
    @Returns: 
        (list) - With the command parts (It shouldn't return the list, it should RUN the appropriate command from this method.
    """
    def run_command(self,cmd):
        self.command = cmd
        self.command = self.parse(self.command)
        return self.command

    """
    @Name: ls
    @Description:
        Does a directory listing
    @Params: 
        dir (string) - The directory to be listed
    @Returns: None
    """
    def ls(self):
        for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))
    
        # print path to all filenames.
        for filename in filenames:
            print(os.path.join(dirname, filename))

    def lsf(self,flag):
        files_info=[]
        for file_name in os.listdir('.'):
            file_stats=os.stat(file_name)
            file_info = [
            file_name,
            file_stats [stat.ST_SIZE],
            oct(stat.S_IMODE(file_stats.st_mode))[2:],
            time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
            time.strftime("%m/%d/%Y %I:%M:%S %P",time.localtime(file_stats[stat.ST_ATIME])),
            time.strftime("%m/%d/%Y &I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME]))
            ]
            files_info.append(file_info)
        #files_info.sort()        
        #for i in range(len(files_info)): 
        if(flag=='-m'):        
            files_info.sort(key=lambda x:time.strftime((x[3])))
        elif(flag=='-s'):
            files_info.sort(key=lambda x:time.strftime((x[2])))
        elif(flag=='-a'):
            files_info.sort(key=lambda x:time.strftime((x[4])))
        elif(flag=='-c'):
            files_info.sort(key=lambda x:time.strftime((x[5])))
            
        for file in files_info:
            #file.sort(key=lambda x: file_stats[stat.ST_MTIME])
            print(file)               
    




            """
    @Name: cat
    @Description:
        Dumps a file
    @Params: 
        file (string) - The file to be dumped
    @Returns: None
    """    
    def cat(self,file):
        if(os.path.isfile(file)):
            f = open(file,'r')
            print(f.read())
        else:
            print("file does not exist")
            
    def mv(self,src,dest):
        if os.path.isfile(src):
            shutil.move(src,dest)
            print("moved succesfully")
        else:
            print("source file doesnot exist")	

    def cp(self,src1,dest1):
        try:
            shutil.copy(src1,dest1)
            print("copyied succesfully")
        except shutil.Error as e:
            print("file not found")
        except IOError as e:
            print('Error: %s' % e.strerror)
            
    def wc(self,filename):
        try:
            f=open(filename,'r')
            wordcount=0 
            for lines in f:
                count=lines.split()
                wordcount=wordcount+len(count)
            f.close()
            print("word count:",str(wordcount))
        except IOError as e:
            print("no such file")

    def wcf(self,flag,file):
        f=open(file,'r')
        count=0
        with open(file,'r')as f:
            for line in f:
                count+=1
        print (count)                
               
            
    def cd(self,flag):
        if(flag=='~'):
            hie=os.getcwd()
            print(hie)
            home = expanduser("~")
            print(home)
        elif(flag=='..'):
            os.chdir('..')
            new=os.getcwd()
            print(new)
            

    def chmod(self,file):
        os.chmod(file,0o777 )
        print(" mode succesfully updated")

    def rm(self,file):
        if os.path.exists(file):
            try:
                os.remove(file)
                print("removed successfully")
            except IOError as e:
                print("file doesnot exist")
    
    def history(self):
        his=historyManager.get_commands(self)
        return his
    
    """
@Name: driver
@Description:
    Drives the entire shell environment
@Methods:
    run_shell - Loop that drives the shel environment
"""
class driver(object):
    def __init__(self):
        self.history = historyManager()
        self.commands = commandManager()
        self.number_commands = 0
        
    """
    @Name: runShell
    @Description:
        Loop that drives the shel environment
    @Params: None
    @Returns: None
    """ 
    def runShell(self):
        number_commands = 0
        while True:
            self.input = input("parser-$ ")         # get command
            self.history.push_command(self.input)   # put in history
            parts = self.commands.run_command(self.input)
            print(parts)
            print(parts[0])
            if parts[0]=='cat':
                self.commands.cat(parts[1])
            elif parts[0]=='ls':
                if(len(parts)==1):
                    self.commands.ls()
                elif(len(parts)==2):
                    self.commands.lsf(parts[1])
            elif parts[0]=='mv':
                if(len(parts)==3):
                    self.commands.mv(parts[1],parts[2])
                else:
                    print("given more or les files")
            elif parts[0]=='cp':
                self.commands.cp(parts[1],parts[2])
            elif parts[0]=='wc':
                if(len(parts)==2):
                    self.commands.wc(parts[1])
                elif(len(parts)==3):
                    self.commands.wcf(parts[1],parts[2]) 
                else:
                    print(" given more or less files")
            elif parts[0]=='cd':
                self.commands.cd(parts[1])
            elif parts[0]=='chmod':
                self.commands.chmod(parts[1])
            elif parts[0]=='rm':
                if(len(parts)==2):
                    self.commands.rm(parts[1]) 
                else:
                    print("given more or less files")
            elif parts[0]=='history':
                his=self.history.get_commands()
                if(len(parts)==1):
                    for item in his:
                        print(item)
                else:
                    print("more arguments in history command")
            else:
                print("command dismatched")
                
if __name__=="__main__":
    d = driver()    
    d.runShell()
