

-72892095_9495



#для основного цикла скрипта, который выполняется с сервера и обновлят данные в базе.
# 1. Обновляем количество проектов. Нужно будет их выстроить в очередь и начать проверять. Как только заканчиваем проход, обновляем количество проектов.
# 1.1. Получаем из базы число проектов. Это будет счетчик.
# 1.2. Получаем из базы id проектов, сортровка по дате добавления, и делаем список.
# 
# Потом - добавить приоритеты. В первую очередь ставятся проекты платных пользователей.
# 2. Начинаем проходить по списку.
# 2.1. Получаем из базы параметры проекта (словарь с вложенными списками и кортэжами?), парсим его в переменные (или исползем так)
# 2.2. В зависимости от настроек проекта начинаем делать запрося к api:
#   if objs=group
#       смотрим в настройках, что отслеживаем:
            if newSubs
            elif newUnsubs
            elif activity
                сначала получаем массов записей [id,owner_id,date,comments,likes,reposts] записей wall.get
                    likes.getList
                    wall.getReposts - profiles
                    comments: id, from_id
                
            
            
            
#   elif objs=user
#   elif objs=boardtopic
#
#

try: 
    
# тут будет выполянться 
  function()
except Error:
  # Если не сработал try и объявлена ошибка Error
else:
  # Если сработал try и не сработал except
finally:
  # Выполняется в любом случае