import os, sys, time
import tasks, ac

os.system('clear')

def Welcome():
    print("\t"+ac.clr.Y+"G3V4L14 S0FTW4R3!"+ac.clr.W)
    print("\t"+ac.clr.G+"Github: "+ac.clr.B+"Gevalia"+ac.clr.W)
    print("\t"+ac.clr.Y+"Other socials: "+ac.clr.R+"Coming soon.."+ac.clr.W)
    print("\n")
    time.sleep(0.5)


def wip():
    print(ac.alrt("This task hasnt been added yet", "pnd"))

"""
Checking to see if the OS is acceptable.
"""

def Helper():
    print(ac.clr.B+"\t-i\tShow this information")
    print("\t-h\tHide files.")
    print("\t-u\tUnhide files.")
    print("\t-x\tDelete files")
    print("\tExample: "+ac.clr.W+sys.argv[0]+" -h Path/To/Directory")

def CheckOs():
    print(ac.alrt('Checking OperatingSystem...', "pnd"))

    currentOs = os.uname()[0]
    osTrue = ['Linux','Android']

    if currentOs in osTrue:
        print(ac.alrt("Welcome " + os.uname()[1], "tru"))
        print(ac.alrt("Your system is acceptable!", "tru"))
        print(ac.clr.G+"\t"+os.uname()[2]+ac.clr.W)
        print("\n")
        time.sleep(0.5)
        CheckArgs()
    else:
        print(ac.alrt("This script only works on Linux Operating system!", "fls"))

"""
Starting the process of the job chosen.
"""

def StartProcess():
    time.sleep(0.5)
    print
    print(ac.alrt(ac.clr.B+"Task to complete: "+ac.clr.W+sys.argv[1], "pnd"))
    
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
        print(ac.alrt(clr.R+"Illegal argument!"+clr.W, "fls"))
        Helper()


"""
Checking to see if the arguments are passed correctly.
"""

def Arguments():
    job = sys.argv[1]
    path = sys.argv[2]

    if(os.path.exists(path)):
        fileCount = len(os.listdir(path))
        
        print(ac.alrt("Path exists: " + ac.clr.Y + path + ac.clr.W, "tru"))
        if(fileCount < 1):
            print(ac.alrt(ac.clr.R + "No files in directory" + ac.clr.W, "fls"))
        else:
            print(ac.alrt(ac.clr.G + "Contains: " + str(fileCount) + " files." + ac.clr.W, "tru"))
            StartProcess()
    else:
        print(ac.alrt(ac.clr.R+"Path does not exist!"+ac.clr.W, "fls"))

#Are there any arguments?
def CheckArgs():
    print(ac.alrt(ac.clr.B + 'Checking arguments...' + ac.clr.W, "tru"))

    try:
        sys.argv[2]
        Arguments()
    except IndexError:
        print(ac.alrt("No arguments passed.", "fls"))
        print("\t" + ac.clr.R + "You need precisely 1 argument\n\tand a Location!" + ac.clr.W)
        Helper()

"""
Putting everything together.
"""
    
print("\n\n")
Welcome()
CheckOs()
print("\n\n")
