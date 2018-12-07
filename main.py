
#from km81.myfile import smth
#print(smth())

#from km81.myfile as mf
#print(mf.smth())

#from km81.myfile
#print(km81.myfile.proga())
import os.path as p
answer1 = p.exists("C:\\Users\\User\\PycharmProjects\\SupaProject\\filelesson\\data\\kol.txt")
answer2 = p.isfile("C:\\Users\\User\\PycharmProjects\\SupaProject\\filelesson\\data\\kol.txt")
answer3 = p.isdir("C:\\Users\\User\\PycharmProjects\\SupaProject\\filelesson\\data\\kol.txt")
print(answer1,answer2,answer3)