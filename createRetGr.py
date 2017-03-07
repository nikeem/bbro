def CreateGroup(adAccId,adClientId,targetGroupId,Token,userIds):
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