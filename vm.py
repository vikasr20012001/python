import os
print("""HELLO USER  I CAN HELP YOU TO RUN THE OS BASE PROGRAM""")
print("1.check how many hard disk connected ")

print("2.create logical volume")

x=int(input("enter your choice : "))


if x==1:
            os.system("fdisk -l")
elif x==2:
           print("enter the disk name 1 : ",end='')
           a=input()
           os.system("pvcreate {}".format(a))
           print("enter the disk name 2 : ",end='')
           b=input()
           os.system("pvcreate {}".format(b))
           print("enter volume group name : ")
           c=input()
           os.system("vgcreate {}".format(c))
           print("enter logical volume size  : ")
           d=input()
           print("enter logical volume name  : ")
           e=input()
           print("enter vg name name  : ")
           f=input()
           os.system("lvcreate --size {}G --name {} {}".format(d,e,f))
           print("create the directory",end='')
           g=input()
           os.system("mkdir {}".format(g))
           print("check the logical volume")
           os.system("lvdisplay")
           print("mount the disk",end='')
           h=input("enter the path")
           os.system("mount {} {}".format(h,g))
           print("how many you need increase the size of the logical volume : ",end='')
           i=input()
           os.system("lvextend --size {}G {}".format(i,h)
           os.system("resize2fs {}".format(h))
           print('how many decrease the size : ",end='')
           j=input()
           os.system("lvreduce -r -L {}G {}".format(j,h)

