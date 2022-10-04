import os
import sys

def getPwd():
    if len(sys.argv) == 2:
        var = os.getcwd()
        print(var)
        return 0
    print("Invalid error")
    sys.exit(255)

def getEcho():
    if len(sys.argv) > 2:
        if sys.argv[2] == '-n':
            var = sys.argv[3]
            for i in range(4, len(sys.argv)):
                var = var + ' ' + sys.argv[i]
            print(var, end="")
            return 0
        else:
            var = sys.argv[2]
            for i in range(3, len(sys.argv)):
                var = var + ' ' + sys.argv[i]
            print(var)
            return 0
    print("Invalid command")
    sys.exit(246)

def getCat():                                                                                      
    if len(sys.argv) > 2:
        for i in range(2, len(sys.argv)):
            if os.path.exists(sys.argv[i]) == False:
                print("Invalid command")                                                                       
                sys.exit(236)
        for i in range(2, len(sys.argv)):
            with open(sys.argv[i], "r") as file:
                for j in iter(file.readline, ""):
                    print(j, end = "")
    else:
        print("Invalid command")
        sys.exit(236)

def getMkdir():
    if len(sys.argv) > 2:                                                                              
        for i in range(2, len(sys.argv)):                                                                  
            if os.path.exists(sys.argv[i]) == True:                                                            
                print("Invalid command")                                                                       
                sys.exit(226)                                                                          
        for i in range(2, len(sys.argv)):                                                                  
            try:                                                                                               
                os.makedirs(sys.argv[i])
            except Exception as e:                                                                             
                sys.exit(226)

def getMv():                                                                                       
    if len(sys.argv) == 4:
        if os.path.exists(sys.argv[2]):
            if os.path.isfile(sys.argv[3]) == False:
                os.rename(sys.argv[2], sys.argv[3])
            else:
                sys.exit(216)
        else:
            sys.exit(216)
    else:
        sys.exit(216)

def getLn():                                                                                       
    try:                                                                                               
        if len(sys.argv) == 4:                                                                             
            os.link(sys.argv[2], sys.argv[3])                                                              
            sys.exit(0)                                                                                
        elif len(sys.argv) == 5:                                                                           
            if sys.argv[2] == '-s' or sys.argv[2] == "--symbolic":                                             
                os.symlink(sys.argv[3], sys.argv[4])
                sys.exit(0)     
            else:
                print("Invalid command")
                sys.exit(255)                                                                   
    except Exception as e:                                                                             
        sys.exit(206) 

def getRmdir():
    if len(sys.argv) > 2:
        try:                                                                                               
            for i in range(2, len(sys.argv)):
                os.rmdir(sys.argv[i])
        except Exception as e:
            sys.exit(196)
    else:
        sys.exit(196)

def getRm():
    tab = ['-r', '-R', "--recursive", '-d', "--dir"]
    var = True
    if len(sys.argv) > 2:
        for i in range(2, len(sys.argv)):
            if (sys.argv[i])[0] == '-' and sys.argv[i] not in tab:
                var = False
            if (sys.argv[2])[0] == '-' and sys.argv[i] in tab:
                if len(sys.argv) == 3:
                    print("Invalid command")
                    sys.exit(255)
            if (sys.argv[i])[0] != '-' and os.path.exists(sys.argv[i]) == False:
                var = False
        if var == True:
            list = ["rm"]
            if (sys.argv[2])[0] != '-':
                for i in range(2, len(sys.argv)):
                    if os.path.isdir(sys.argv[i]) == False:
                        list.append(sys.argv[i])
                os.execvp(list[0], list[0:])                                                               
            else:
                os.execvp(sys.argv[1], sys.argv[1:])
        else:
            sys.exit(186)
    else:
        sys.exit(186)

def getLs():
    tab = ['-a', "--all", '-R', "--recursive"]
    var = True
    if len(sys.argv) > 1:
        if len(sys.argv) > 2:
            if (sys.argv[2])[0] == '-' and sys.argv[2] not in tab:
                var = False
            if (sys.argv[2])[0] != '-' and os.path.exists(sys.argv[2]) == False:
                var = False
            if var == True:                                                                                    
                os.execvp(sys.argv[1], sys.argv[1:])                                                       
            else:                                                                                              
                sys.exit(176)                                                                          
        os.execvp(sys.argv[1], sys.argv[1:])
    else:
        sys.exit(176)

def getCp():
    tab = ['-R', '-r', "--recursive"]
    var = True
    if len(sys.argv) > 3:
        if (sys.argv[2])[0] == '-' and sys.argv[2] not in tab:
            var = False
        if (sys.argv[2])[0] != '-' and (os.path.exists(sys.argv[2]) == False or os.path.exists(sys.argv[3]) == False):            
            var = False
        if (sys.argv[2])[0] != '-' and os.path.isdir(sys.argv[2]) == True:
            var = False
        if var == True:
            os.execvp(sys.argv[1], sys.argv[1:])                                                       
        else:
            sys.exit(166)
    else:
        sys.exit(166)

def getTouch():
    tab = ['-a', '-c', "--no-create", '-m']
    var = True
    if len(sys.argv) > 2:
        if (sys.argv[2])[0] == '-' and sys.argv[2] not in tab:
            sys.exit(156)
        os.execvp(sys.argv[1], sys.argv[1:])
    else:
        sys.exit(156)

def getChmod():
    tabn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]                                                          
    tabl = ['u', 'g', 'o', 'a']                                                                    
    if len(sys.argv) == 4:                                                                             
        if (sys.argv[2])[0] not in tabl:
            if (sys.argv[2])[0] < "0" or (sys.argv[2])[0] > "9":
                print("Invalid command")
                sys.exit(255)
        os.execvp(sys.argv[1], sys.argv[1:])
    else:
        sys.exit(231)

if len(sys.argv) == 1:                                                                             
    print("Invalid command")                                                                   
else:                                                                                              
    x = sys.argv[1]                                                                                
    if x == "pwd":                                                                                     
        getPwd()                                                                                   
    elif x == "echo":                                                                                    
        getEcho()                                                                                  
    elif x == "cat":                                                                                     
        getCat()
    elif x == "mkdir":                                                                                   
        getMkdir()                                                                                 
    elif x == "mv":                                                                                      
        getMv()                                                                                    
    elif x == "ln":                                                                                      
        getLn()
    elif x == "rmdir":
        getRmdir()
    elif x == "rm":
        getRm()
    elif x == "ls":
        getLs()
    elif x == "cp":
        getCp()   
    elif x == "touch":
        getTouch()
    elif x == "chmod":
        getChmod()
    else:
        print("Invalid command")
        sys.exit(255)