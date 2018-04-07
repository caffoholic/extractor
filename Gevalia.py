import os, sys, time
import tasks

os.system('clear')

class clr:
    R = "\033[0;31m"
    W = "\033[0m"
    G = "\033[0;32m"
    B = "\033[0;34m"
    Y = "\033[0;93m"

class alerts:
    true =      "[" + clr.G + "!" + clr.W + "]\t"
    false =     "[" + clr.R + "!" + clr.W + "]\t"
    pending =   "[" + clr.Y + "!" + clr.W + "]\t"

def Welcome():
    print("\t"+clr.Y+"G3V4L14 S0FTW4R3!"+clr.W)
    print("\t"+clr.G+"Github: "+clr.B+"Gevalia"+clr.W)
    print("\t"+clr.Y+"Other socials: "+clr.R+"Coming soon.."+clr.W)
    print
    time.sleep(0.5)


def wip():
    print(alerts.pending+clr.R+"This task hasnt been added yet"+clr.W)

"""
Checking to see if the OS is acceptable.
"""

def Helper():
    print(clr.B+"\t-i\tShow this information")
    print("\t-h\tHide files.")
    print("\t-u\tUnhide files.")
    print("\t-x\tDelete files")
    print("\tExample: "+clr.W+sys.argv[0]+" -h Path/To/Directory")
    print(tasks.Testing())

def CheckOs():
    print(alerts.pending + clr.B + 'Checking OperatingSystem...' + clr.W)

    currentOs = os.uname()[0]
    osTrue = ['Linux','Android']

    if currentOs in osTrue:
        print(alerts.true + "Welcome " + os.uname()[1])
        print(alerts.true + "Your system is acceptable!")
        print(clr.G+"\t"+os.uname()[2]+clr.W)
        print
        time.sleep(0.5)
        CheckArgs()
    else:
        print(alerts.false + "This script only works on Linux Operating system!")

"""
Starting the process of the job chosen.
"""

def StartProcess():
    time.sleep(0.5)
    print
    print(alerts.pending+clr.B+"Task to complete: "+clr.W+sys.argv[1])
    
    acceptedArgs = ['-h','-u','-x','-i']
    
    if sys.argv[1] in acceptedArgs:
        job = sys.argv[1]
        if(job == "-h"):
            tasks.HideFiles(sys.argv[2])
        elif(job == "-u"):
            tasks.UnhideFiles(sys.argv[2])
        elif(job == "-x"):
            #deleteFiles()
            wip()
        else:
            Helper()
    else:
        print(alerts.false+clr.R+"Illegal argument!"+clr.W)
        Helper()


"""
Checking to see if the arguments are passed correctly.
"""

def Arguments():
    job = sys.argv[1]
    path = sys.argv[2]

    if(os.path.exists(path)):
        fileCount = len(os.listdir(path))
        
        print(alerts.true + "Path exists: " + clr.Y + path + clr.W)
        if(fileCount < 1):
            print(alerts.false + clr.R + "No files in directory" + clr.W)
        else:
            print(alerts.true + clr.G + "Contains: " + str(fileCount) + " files." + clr.W)
            StartProcess()
    else:
        print(alerts.false+clr.R+"Path does not exist!"+clr.W)

#Are there any arguments?
def CheckArgs():
    print(alerts.pending + clr.B + 'Checking arguments...' + clr.W)

    try:
        sys.argv[2]
        Arguments()
    except IndexError:
        print(alerts.false + "No arguments passed.")
        print("\t" + clr.R + "You need precisely 1 argument\n\tand a Location!" + clr.W)

"""
Putting everything together.
"""
    
print
print
Welcome()
CheckOs()
print
print
