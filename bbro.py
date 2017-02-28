import requests
from os import path
import re
import sqlite3

#==================================================
#заготовки для работы с базой черех алхимию
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('sqlite:///:memory:')

#Session = sessionmaker(bind=engine)
#session = Session()

#Base = declarative_base()
#==================================================


#конфиг, который нужно вынести в отдельный файл, а затем хранить в базе
#тип добавляемого объекта. сейчас задаем руками, а потом - radiobutton
objsType = "group"
#group 1, user 2, topic 3
whatLookAt = "comments"
#allactivity 1 (likes11, comments12, reposts13), 
#newSubs 2
#unSubs 3
#newFriends 4


#настройка ретаргета ads.importTargetContacts

account_id=1900002663
client_id=1603181057
target_group_id=8447268
#whereTo = [account_id,client_id,target_group_id,contacts]



#получаем ссылки на объекты, создаем лист objsUrls
inputObjs = open('input.txt')
objsUrls = inputObjs.read().split("\n")
inputObjs.close

#проверка типа объектов. ошибка, если не правильный тип

#проверяем и сортируем объекты, Реализуем позже. Сейчас пользователь будет сам выбирать тип объектов
#for eachObjUrl in objsUrls:
#    urlPartToCheck = eachObjUrl[eachObjUrl.find("vk.com/")+7:]
    

    
# преобразуем урлы в id объектов, чтобы добавить их в базу и начать отслеживать. Возвращает список объектов
def getObjsList(objsUrls):
    if objsType == "group":
        regextpl = '^.+vk\.com\/club\d+$'
        for eachObjUrl in objsUrls:
            if re.match(regextpl, eachObjUrl) is not None:
                groupId = eachObjUrl[eachObjUrl.find("vk.com/")+11:]
            else:
                groupId = eachObjUrl[eachObjUrl.find("vk.com/")+7:]
            objsList.append(groupId)
    elif objsType == "user":
        regextpl = '^.+vk\.com\/id\d+$'
        for eachObjUrl in objsUrls:
            if re.match(regextpl, eachObjUrl) is not None:
                userId = eachObjUrl[eachObjUrl.find("vk.com/")+9:]
            else:
                userId = eachObjUrl[eachObjUrl.find("vk.com/")+7:]
            objsList.append(userId)
            
    elif objsType == "topic":
        regextpl = '^.+vk\.com\/topic-\d+.\d+$'
        for eachObjUrl in objsUrls:
            topicFullId = eachObjUrl[eachObjUrl.find("vk.com/topic-")+13:]
            objsList.append(topicFullId)
    else pass
    
    return objsList


#сохраняем список объектов в базу


con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE Projs(ProjId INT, ProjName TEXT, ProjOwner INT, objsType INT, whatLookAt INT, adAccId INT, adClientId INT, targetGroupId INT, Token TEXT, Objs BLOB, LastState BLOB  )")
    cur.execute("INSERT INTO Projs VALUES(1,'Nik',1,1,1,1900002663,1603181057,8447268,'9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2',[72892095,45650931]),[]")
    cur.execute("INSERT INTO Projs VALUES(1,'Nik',1,1,2,1900002663,1603181057,8447268,'9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2',[72892095,45650931]),[]")
    cur.execute("INSERT INTO Projs VALUES(1,'Nik',1,1,3,1900002663,1603181057,8447268,'9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2',[72892095,45650931]),[]")
    
    


#основной цикл









    
    
    
    
    
    
    
#	alluserids =[]
    
    


# def get_screen_names_from_urls(groupurls):
#	screen_names_list = []
#	for fullurl in groupurls:
#			rrr = fullurl[fullurl.find("vk.com/")+7:]
#			screen_names_list.append(rrr)
#	return screen_names_list







#if fullurl[fullurl.find("vk.com/"):] == 



#def inputObjs():
#    fileWithObjs =
    
    
#def getStartSubs()


#def getCurrentSubs()