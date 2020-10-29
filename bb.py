import os
print("""HELLO USER  I CAN HELP YOU TO RUN THE OS BASE PROGRAM""")
print("1.RUN CAL COMMAND")

print("2.RUN DATE COMMAND")

print("3.RUN WHOAMI COMMAND")

print("4.RUN PS -AUX COMMAND")
while True:
   print("please enter your choice which type of system you use remote/local : ",end=' ')
   i=input("")
   x=int(input("enter what you want to do : "))
   if i=="local":
       if x==1:
            os.system("cal")
       elif x==2:
            os.system("date")
       elif x==3:
            os.system("whoami")
       elif x==4:
            os.system("ps -aux")
   if i=="remote":
        y=input("enter the remote system ip : ")
        if x==1:
           os.system("ssh {} cal".format(y))
        elif x==2:
           os.system("ssh {} date".format(y))
        elif x==3:
           os.system("ssh {} whoami".format(y))
        elif x==4:
           os.system("ssh {} ps -aux".format(y))
           
