import sys
import sqlite3
import requests
import re



#конфиг, который нужно вынести в отдельный файл, а затем хранить в базе
#тип добавляемого объекта. сейчас задаем руками, а потом - radiobutton
#objsType = "group"
#group 1, user 2, topic 3
#whatLookAt = "comments"
#allactivity 1 (likes11, comments12, reposts13), 
#boardComments 5
#newSubs 2
#unSubs 3
#newFollowers 4

#настройка ретаргета ads.importTargetContacts

#account_id=1900002663
#client_id=1603181057
#target_group_id=8447268
#whereTo = [account_id,client_id,target_group_id,contacts]

projsTable = "Projs"

#получаем данные из базы
def loadSettings(projsTable,projId,dbname):
    condb = sqlite3.connect(dbname)
    with condb:
        cur = condb.cursor()
        cur.execute("SELECT * FROM {} WHERE ProjId={}".format(projsTable, projId))
    
        #получили строку в форме tuple
        #print(cur.fetchone()[1])
    
        #распоковали tuple, полученный из базы в переменные.
        #(ProjId,ProjName,ProjOwner,objsType,whatLookAt,adAccId,adClientId,targetGroupId,Token,Objs,LastState) = cur.fetchone()
    
        #print(ProjId,ProjName,ProjOwner,objsType,whatLookAt,adAccId,adClientId,targetGroupId,Token,Objs,LastState)
        
        return cur.fetchone()

#  отправляем данные в базу, обновляем колонку LastState
def writeToDb(newState,dbname):
    newStateString = '['+','.join(newState)+']'
    condb = sqlite3.connect(dbname)
    with condb:
        cur = condb.cursor()
        cur.execute("UPDATE {} SET LastState = '{}' WHERE ProjId={}".format(projsTable, newStateString, projId))

#def getAllWallActivity():
    # def getWallLikes():
    #def getWallReposts():    
    # def getWallComments():
        
    
def getWallLikes():
    
    
def getWallReposts():
    
    
def getWallComments():
    
    
def getNewSubs():
    
    
def getUnSubs():
    
#функция получает список друзей всех пользователй в списке Objs, вычитает прошлый список LastState и возвращает id свежедобавленныъ друзей.   
def getNewFriends(Objs,LastState,access_token):
    allFriendsList = []
    for userid in Objs:
        execute.friendsget2
        fullreq = 'https://api.vk.com/method/execute.friendsget2?usrid='+str(userid)+'&access_token='+access_token+'&v=5.62'
        r = requests.post(fullreq)
        resultt = r.text
        beginwith = r.text.index("[")
        resultt = r.text[beginwith+1:-2]
        allFriendsList = allFriendsList+resultt.split(",")
	    
    newFriends = list(set(allFriendsList) - set(LastState))
    return newFriends



    
def getBoardTopicComms():
        
        
#основной цикл   

# получаем настройки проекта
(ProjId,ProjName,ProjOwner,objsType,whatLookAt,adAccId,adClientId,targetGroupId,Token,Objs,LastState) = loadSettings(projsTable,1,'test.db')
#print(ProjId,ProjName,ProjOwner,objsType,whatLookAt,adAccId,adClientId,targetGroupId,Token,Objs,LastState)

#раскладываем строку объектов с список объектов
Objs = Objs[1:-1].split(',')
#print(Objs[0])

#раскладываем строку найденных объектов в список объектов
LastState = LastState[1:-1].split(',')
#print(LastState[0])


#в зависимости от типа объекта и типа отслеживания, вызываем функцию, а уже внутри нее вызывем функцию в зависимости от объекта отслеживания

if objsType == 1:
    print('group')
    if whatLookAt == 1:
        print('all wall activity')
        
    elif whatLookAt == 11
        print('likes wall activity')
        
    elif whatLookAt == 12
        print('likes wall activity')
        
    elif whatLookAt == 13
        print('likes wall activity')
        
    elif whatLookAt == 2
        print('new subs')
        
    elif whatLookAt == 3
        print('unsubs')
        
    
elif objsType == 2:
    print('user')
    if whatLookAt == 1:
        print('all wall activity')
        
    elif whatLookAt == 11
        print('likes wall activity')
        
    elif whatLookAt == 12
        print('likes wall activity')
        
    elif whatLookAt == 13
        print('likes wall activity')
        
    elif whatLookAt == 4
        print('new friends')
        newFriends = getNewFriends(Objs,LastState,Token)
        
        

    
        


        
        
#добавляем пересозданный ряд в базу
#cur.execute("INSERT INTO Projs VALUES(3,'Nik',1,1,3,1900002663,1603181057,8447268,'9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2','[72892095,45650931]','[123]')")
        
        
        
        
        
        
        
    
    
elif objsType == 3:
    print('topic')
    if whatLookAt == 5:
        print('boardComments')




#отправляем данные в ретаргетинг
#def updateRetarget()



#обновляем row в базе sqllite
#def updateDb()
