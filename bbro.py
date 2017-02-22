import requests
from os import path
import re


#тип добавляемого объекта. сейчас задаем руками, а потом - radiobutton
objsType = "group"




#получаем ссылки на объекты, создаем лист objsUrls
inputObjs = open('input.txt')
objsUrls = inputObjs.read().split("\n")

# преобразуем урлы в id объектов, чтобы добавить их в базу и начать отслеживать.
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
            if re.match(regextpl, eachObjUrl) is not None:
                topicFullId = eachObjUrl[eachObjUrl.find("vk.com/")+9:]
            else:
                topicFullId = eachObjUrl[eachObjUrl.find("vk.com/")+7:]
            objsList.append(topicFullId)
    else pass
    
    return objsList
            









#проверяем и сортируем объекты, Реализуем позже. Сейчас пользователь будет сам выбирать тип объектов
#for eachObjUrl in objsUrls:
#    urlPartToCheck = eachObjUrl[eachObjUrl.find("vk.com/")+7:]
    
    
    
    
    
    
    
    
	alluserids =[]
    
    


# def get_screen_names_from_urls(groupurls):
#	screen_names_list = []
#	for fullurl in groupurls:
#			rrr = fullurl[fullurl.find("vk.com/")+7:]
#			screen_names_list.append(rrr)
#	return screen_names_list







#if fullurl[fullurl.find("vk.com/"):] == 



#def inputObjs():
    fileWithObjs =
    
    
#def getStartSubs()


#def getCurrentSubs()