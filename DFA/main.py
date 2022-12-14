def Prefix(state , string):
    errState = 'q4'
    finishState = 'q3'

    if len(string) >= 3:
        if state == 'q0':
            if string[0] == '1':
                print(state + " -> " + string[0] + ' -> ' + 'q1')
                return Prefix('q1' , string[0:])
            else:
                print(state + " -> " + string[0] + ' -> ' + errState)
                return Prefix(errState , string[0:])
        
        elif state == 'q1':
            if string[1] == '0':
                print(state + " -> " + string[0:2]  + ' -> ' + 'q2')
                return Prefix('q2' , string[0:])
            else:
                print(state + " -> " + string[0:2] + ' -> ' + errState)
                return Prefix(errState , string[0:])
        
        elif state == 'q2':
            if string[2] == '1':
                print(state + " -> " + string[0:3]  + ' -> ' + finishState)
                return Prefix(finishState , string[0:])
            else:
                print(state + " -> " + string[0:3] + ' -> ' + errState)
                return Prefix(errState , string[0:])
        
        elif state == finishState : 
            print(string[0:3] + " -> " + finishState) 
            print(string + " -> " + finishState)
            return(finishState + '(Final State)')

        elif state == errState : 
            print(string + " -> " + errState)
            return(errState + "(Dead State)")

        else : 
            return(string + " -> " + state)
    
    else : 
        print(string + " -> " + errState)
        return(errState + "(Dead State)")

def Suffix(state , string):
    finishState= 'q3'

    if len(string) >= 1:
        suffixString = string[-3:]
        if state == "q0":
            if suffixString[0] == "1":
                return Suffix("q1", suffixString[1:])
            else:
                return Suffix("q0", suffixString[1:])

        elif state == "q1":
            if suffixString[0] == "0":
                return Suffix("q2", suffixString[1:])
            else:
                return Suffix("q1", suffixString[1:])

        elif state == "q2":
            if suffixString[0] == "1":
                return Suffix("q3", suffixString[1:])
            else:
                return Suffix("q0", suffixString[1:])

        elif state == finishState : 
            return(finishState + "(Finish State)")
    
    return state


def SubString(state , string):
    finishState = 'q3'
    
    if len(string) >= 1:
        if state == "q0":
            if string[0] == "1":
                print(state + " -> " + string[0] + ' -> ' + 'q1')
                return SubString("q1", string[1:])
            else:
                print(state + " -> " + string[0] + ' -> ' + 'q0')
                return SubString("q0", string[1:])

        elif state == "q1":
            if string[0] == "0":
                print(state + " -> " + string[0] + ' -> ' + 'q2')
                return SubString("q2", string[1:])
            else:
                print(state + " -> " + string[0] + ' -> ' + 'q1')
                return SubString("q1", string[1:])
                
        elif state == "q2":
            if string[0] == "1":
                print(state + " -> " + string[0] + ' -> ' + 'q3')
                return SubString("q3", string[1:])
            else:
                print(state + " -> " + string[0] + ' -> ' + 'q0')
                return SubString("q0", string[1:])

        elif state == finishState : 
            return(finishState + "Final State")
    
    return state

def MainMenu():
    print("Tugas Programming DFA")
    print("================================")
    print("Menu: ")
    print("1. Prefix 101 \t\t 2. Suffix 101 \n3. Substring 101 \t 4. Exit")
    print("Masukkan Pilihan: " , end='')
    choice = int(input())

    if choice == 1:
        print("\nMasukkan String: " , end='')
        string = str(input())
        
        print(Prefix('q0' , string))

    elif choice == 2:
        print("\nMasukkan String: " , end='')
        string = str(input())
        
        print("Hasil: " , Suffix('q0' , string))

    elif choice == 3:
        print("\nMasukkan String: " , end='')
        string = str(input())

        print(SubString('q0' , string))
            
    exit()

MainMenu()
