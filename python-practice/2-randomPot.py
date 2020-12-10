#make a randomPot
import random
print("Recommend me three times")

PlayList=[]
Dict1={}
a = input("Artist: ")
b = input("Title of song: ")
Dict1.setdefault("artist", a)
Dict1.setdefault("song", b)
PlayList.append(Dict1)
Dict2={}
a = input("Artist: ")
b = input("Title of song: ")
Dict2.setdefault("artist", a)
Dict2.setdefault("song", b)
PlayList.append(Dict2)
Dict3={}
a = input("Artist: ")
b = input("Title of song: ")
Dict3.setdefault("artist", a)
Dict3.setdefault("song", b)
PlayList.append(Dict3)

ranNum=random.randint(0,2)
print("Artist: ",PlayList[ranNum]["artist"],", Tite of song: ",PlayList[ranNum]["song"])