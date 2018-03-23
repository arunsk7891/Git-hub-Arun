
print ("\n\t\t\t\t\t\tFILE READ WRITE \n")
strn = input('\n\t\t Enter the text file path to read and write  : \n\n\t\t ')
path = strn
print ("\n\t\t Received input file path is : \n\n\t\t",path)
print ("\n\n\t\t")
wait = input("\n\t\tPRESS ENTER TO CONFIRM & CONTINUE -- ")


d_file = open(path,'r')
filedata = d_file.read()
print ("\n\n\t\t File Contents Are : ")
print(filedata)
new_path = path
new_rd = open(new_path,'a+')

respon = int(input("\n\t\t Enter 1 to write to file : \n\t\t Enter 0 to exit loop: "))
print ("\n\n \t\t Your Response is  :  ",respon)
b=respon
print("\n\n")

if(b==1):
    word =input ("Enter your text : \n\t\t  ")
    wait = input("\n\t\tPRESS ENTER TO CONFIRM & CONTINUE TO WRITE TO FILE.")
    new_rd.write(word)
    addent="\n\n\t"
    new_rd.write(addent)
    print(" \t\t new text entered ")
    new_rd.close()
    d_file.close()
    
else:
    print(" \n\t\t\t\t Exiting Loop ")
    new_rd.close()
    d_file.close()
    

respon1 = int(input("\n\t\t Enter 1 to display new file content : \n\t\t Enter 0 to exit loop : "))
if (respon1==1):
    d_file1 = open(path,'r')
    filedata1 = d_file1.read()
    print ("\n\n\t\t File Contents Are : ")
    print(filedata1)
    d_file1.close()
    wait = input("\n\t\tPRESS ENTER TO Exit ")
    
else:
    print(" \n\n\t\t\t\t Exiting the Loop  ")
    

clear =int(input ("\n\t\tDo you want to Clear file contents ?\n\t\t Enter 1 to CLEAR ,0 to EXIT  "))
if (clear==1):
    print("\n\n\t\t Clearing file ")
    open(new_path, 'w').close()
    print("\n\n\t\t Cleared file ")
    wait = input("\n\t\tPRESS ENTER TO Exit ")
else:
    print(" \n\n\t\t\t\t Exiting the file  ")
    exit()



exit()
    
    
