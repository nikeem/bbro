import sys
import sqlite3
import requests
#import re
import time
import json



#конфиг, который нужно вынести в отдельный файл, а затем хранить в базе 
#upd 02.03 конфиг грузится из базы
#тип добавляемого объекта. сейчас задаем руками, а потом - radiobutton
#objsType = "group"
#group 1, user 2, topic 3
#whatLookAt = "comments"
#allactivity 1 (likes11, comments12, reposts13), 
#boardComments 5
#newSubs 2
#unSubs 3
#newFollowers 4

#account_id=1900002663
#client_id=1603181057
#target_group_id=8447268
#whereTo = [account_id,client_id,target_group_id,contacts]

projsTable = 'Projs'
dbname = 'test.db'



"""
Запись данных в базу.
1. Если джанго работает через свою ORM, мошу ли я в этом скрипте испортировать класс и использовать базу через ORM?
2. Принимаем данные с форм.
3. Страница проекта должна грузить эти данные и показывать.
"""


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
def writeToDb(newState,dbname,projId):
    newStateString = '['+','.join(newState)+']'
    #newStateString = ','.join(str(oneId) for oneId in newState)
    condb = sqlite3.connect(dbname)
    with condb:
        cur = condb.cursor()
        cur.execute("UPDATE {} SET LastState = '{}' WHERE ProjId={}".format(projsTable, newStateString, projId))
        
#отправляем данные в ретаргет
def retargetGroupUpdate(adAccId,adClientId,targetGroupId,Token,userIds):
    #пока работает в один заход - до 1000 контактов разово. нужно переписать так, чтобы эту функцию можно было использовать и для добавления всего спика первоначально при созании проекта, и при добавлении отдельных контактов.
    #userIdsString = ','.join(userIds)
    userIdsString = ','.join(str(oneId) for oneId in userIds)
    
    #print("userIdsString: ", userIdsString)
    
    newfilename = time.strftime('%y%m%d%H%M%S', time.localtime()) + 'ids.txt'
    thefile = open(newfilename, 'w')
    for item in userIds:
        thefile.write("%s\n" % item)
        thefile.close
    print('Записали пользователей в файл')
    
    r = requests.post('https://api.vk.com/method/ads.importTargetContacts', data = {'account_id':str(adAccId), 'client_id':str(adClientId), 'contacts': userIdsString, 'access_token':Token,'v': '5.62', 'target_group_id': targetGroupId })
    
    #fullreq = 'https://api.vk.com/method/ads.importTargetContacts?account_id='+str(adAccId)+'&client_id='+str(adClientId)+'&contacts='+userIdsString+'&access_token='+Token+'&v=5.62'
    #r = requests.post(fullreq)
    resultt = r.text
    print('{} users added!'.format(resultt))
    return resultt
    

    
#def getWallLikes():
    
    
#def getWallReposts():
    
    
#def getWallComments():


#def getAllWallActivity():
    # def getWallLikes():
    # def getWallReposts():    
    # def getWallComments():
        
    
def getNewSubs(Objs,LastState,access_token):
    alluserids = []
    for eachid in Objs:
        offset = 0
        print("Парсим группу", eachid)
        #получаем число членов
        memcount = requests.post('https://api.vk.com/method/execute.memcount', data = {'grid':eachid, 'access_token':access_token,'v': '5.62'}).json()['response']
        	
        if memcount == 0:
            pass
        elif memcount <= 24000:
            qwe = requests.post('https://api.vk.com/method/execute.getallmem', data = {'grid':eachid, 'offs':offset, 'access_token':access_token,'v': '5.62'}).json()['response']
            alluserids = alluserids + qwe
		
	
        else:
            while offset < memcount:
                qwe = requests.post('https://api.vk.com/method/execute.getallmem', data = {'grid':eachid, 'offs':offset, 'access_token':access_token,'v': '5.62'}).json()['response']
                alluserids = alluserids + qwe
                offset = offset + 24000
                time.sleep(.19)
        time.sleep(.33)
        
    alluserids = ','.join(str(oneId) for oneId in alluserids)    
    allUsersList = alluserids.split(",")
    
    newSubs = list(set(allUsersList) - set(LastState))
    #print(newSubs)
    return newSubs, set(allUsersList)
    
    
    
    
#должно работать, потестить    
def getUnsubs(Objs,LastState,Token):
    newSubs, allUsersList = getNewSubs(Objs,LastState,Token)
    unSubs = list(set(LastState) - set(allUsersList))
    print('unSubs', unSubs)
    return unSubs, allUsersList
    
    

def getNewFriends(Objs,LastState,access_token):
    allFriendsList = []
    
    while len(Objs) > 0:
        if len(Objs) > 25:
            userIds25Max = ','.join(Objs[0:25])
            del Objs[0:25]		
        else:
            userIds25Max = ','.join(Objs)
            del Objs [:]
            
        print("Парсим друзей пользоватлей: ", userIds25Max)
        r = requests.post('https://api.vk.com/method/execute.friendsget', data = {'usrids':userIds25Max, 'access_token':access_token,'v': '5.62'})
        resultt = r.json()['response']
                
        if isinstance(resultt, str):
            print("Получили данные от АПИ в формате строки")
            allFriendsList = allFriendsList + resultt.split(",")
                        
        elif isinstance(resultt, list):                        
            print("Получили данные от АПИ в формате массива")
            resultt = ','.join(str(oneId) for oneId in resultt)
            #print("конвертим в стринг")
            #print(resultt)            
            allFriendsList = allFriendsList + resultt.split(",")         
        time.sleep(0.1)
    
    #print(len(set(allFriendsList)))
    #print(len(set(LastState)))
    
    newFriends = list(set(allFriendsList) - set(LastState))
    #print(len(newFriends))
        #print(allFriendsList[1:9])
    #print(LastState[1:9])
    #print(newFriends[1:9])  
    
    return newFriends, set(allFriendsList)


#def getBoardTopicComms():
        
        
#основной цикл   

# получаем настройки проекта. ЗДЕСЬ ХАРДКОД ID ПРОЕКТА. ПЕРЕДАВАТЬ ПЕРЕВЕННОЙ!
(ProjId,ProjName,ProjOwner,objsType,whatLookAt,adAccId,adClientId,targetGroupId,Token,Objs,LastState) = loadSettings(projsTable,8,dbname)
#print(ProjId,ProjName,ProjOwner,objsType,whatLookAt,adAccId,adClientId,targetGroupId,Token,Objs,LastState)

#раскладываем строку объектов с список объектов
Objs = Objs[1:-1].split(',')
#print(Objs)

#раскладываем строку найденных объектов в список объектов
#print("LastState до разделения в список ", LastState)
LastState = LastState[1:-1].split(',')
#print(LastState)

print("Загрузили настройки проекта\n")

#в зависимости от типа объекта и типа отслеживания, вызываем функцию, а уже внутри нее вызывем функцию в зависимости от объекта отслеживания

if objsType == 1:
    print('group')
    if whatLookAt == 1:
        print('all wall activity')
        newUsersToAdd, newState = getAllWallActivity(Objs,LastState,Token)
        
        
    elif whatLookAt == 11:
        print('likes wall activity')
        newUsersToAdd, newState = getLikesWall(Objs,LastState,Token)
        
        
    elif whatLookAt == 12:
        print('comments wall activity')
        newUsersToAdd, newState =getCommsWall(Objs,LastState,Token)
        
        
    elif whatLookAt == 13:
        print('likes reposts activity')
        newUsersToAdd, newState = getRepostsWall(Objs,LastState,Token)
        
    #done!
    elif whatLookAt == 2:
           
        print('new subs')
        newUsersToAdd, newState = getNewSubs(Objs,LastState,Token)
        
    elif whatLookAt == 3:
        print('unsubs')
        newUsersToAdd, newState = getUnsubs(Objs,LastState,Token)
        
    
elif objsType == 2:
    print('Следим за пользователями ')
    if whatLookAt == 1:
        print('all wall activity')
        newUsersToAdd, newState = getAllWallActivity(Objs,LastState,Token)
    
        
    elif whatLookAt == 11:
        print('likes wall activity')
        newUsersToAdd, newState = newUsersToAdd, newState = getLikesWall(Objs,LastState,Token)
        
    elif whatLookAt == 12:
        print('likes wall activity')
        newUsersToAdd, newState = newUsersToAdd, newState = getCommsWall(Objs,LastState,Token)
        
    elif whatLookAt == 13:
        print('likes wall activity')
        newUsersToAdd, newState = newUsersToAdd, newState = getRepostsWall(Objs,LastState,Token)
        
#готово!        
    elif whatLookAt == 4:
        print('Получаем новых друзей пользователей ')
        newUsersToAdd, newState = getNewFriends(Objs,LastState,Token)
    
elif objsType == 3:
    print('topic')
    if whatLookAt == 5:
        print('boardComments')
        
print("В базу добивм:", newUsersToAdd)     
if len(newUsersToAdd) == 0 or newUsersToAdd[0] == "" :
    print("Ничего не добавили!")
else:
    retargetGroupUpdate(adAccId,adClientId,targetGroupId,Token,newUsersToAdd)
    writeToDb(newState,dbname,ProjId)
    
