Hadeel = print ("Now I lestining to abu noura")
ask= input ("Do you know who is Abu noura ?")

#If- Else statemnt 
if ask == "Yes":
    print ("Well Done!")

else:
    print ("I hope You Know him <3")
    print ("\n\n")

    
secondQ= input ("I think you have yout favourite singer, tell me ?")

if secondQ == "Khalid abdulrahman" or secondQ == "Abu Naif":
    print ("I love him !!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print (" محد مهتم")

#while loop and for loop

thirdQ= int(input("How many time that you join workShop? "))

while thirdQ ==1:
    print ("U must join more")
    break

for i in range (8):
    print (i)

#Files write and read

Readfile= open(r"C:\Users\ASUS\Desktop\textfile.txt", 'r')
print (Readfile.read()) #to read the file
Readfile. close ()

WriteOnFile= open ("textfile.txt","w")
WriteOnFile.write= ("Best wishes babe <3 <3")
WriteOnFile.close()

print ("***"*25)
#Functions
def myName (name):
    print (name+"Engineer")
myName("Hadeel")
myName("ALDhafeeri")

def myMajor (major):
    x= input("My Major:\t")
    print (major+x)

myMajor("Computer")

    



















































    

