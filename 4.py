
{"response":"66702,172469,617276,675453,699359,920334,1016601,1090653,1397146,1428247,1673887,1719780,1822054,2061109,2074547,2224577,2267143,2523283,2532916,2610202,2640406,2767419,2872997,2891974,2966841,3185104,3201061,3348842,3433751,34
59129,3700284,4013066,4066973,4447987,4741287,4821435,4831298,4911049,5088576,5088950,5227245,5228037,5253653,5328251,53
85404,5385792,5470073,5512197,5582683,5647705,5648990,5705933,5786011,6251072,6259672,6309952,6352809,6661221,6805766,68
28550,8365223,9009561,9463795,9628344,10259160,10658914,11485037,11678181,12613645,13742865,13942342,14163956,15253374,1
6122929,18044364,18128285,19536494,19608964,19906143,20894220,21284218,21613004,21840224,23164083,23325957,24642441,2477
7930,24804897,25290927,25741762,25765014,25867924,27143629,28281416,29110472,29365455,30111348,30573386,31101289,3138520
7634,268186231,270596294,273075558,279428321,279910152,286225343,286918806,296164087,297039534,332014661,351425432,35202
9394,353098671,354049078,354099461,361304346,389397415,397102968","execute_errors":[{"method":"friends.get","error_code"
:18,"error_msg":"User was deleted or banned"},{"method":"friends.get","error_code":18,"error_msg":"User was deleted or b
anned"},{"method":"friends.get","error_code":18,"error_msg":"User was deleted or banned"}]}
Traceback (most recent call last):
  File "3.py", line 222, in <module>
    newUsersToAdd, newState = getNewFriends(Objs,LastState,Token)
  File "3.py", line 141, in getNewFriends
    time.sleep(3)
                                               
                                               
                                               
                                               
                                               


def screen_name_resolve(screen_name_list_string25):
	fullreq = 'https://api.vk.com/method/execute.screen_name_resolve?screen_name_list='+screen_name_list_string25+'&access_token=9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2&v=5.53'
	apiresponse = requests.post(fullreq)
	beginwith = apiresponse.text.index("[")
	return apiresponse.text[beginwith+1:-2].split(",")





def get_group_ids_list(groupurls):
	allgroupids = []
	screen_names_list = get_screen_names_from_urls(groupurls)
	while len(screen_names_list) > 0:
		if len(screen_names_list) > 25:
			groupurlsstring = ','.join(screen_names_list[0:25])
			del screen_names_list[0:25]
		
		else:
			groupurlsstring = ','.join(screen_names_list)
			del screen_names_list [:]
				
		allgroupids = allgroupids + screen_name_resolve(groupurlsstring)
		time.sleep(.19)	
	
	return allgroupids




def getFriends25(Objs):
    
    
    
    
    
    
    r = requests.post('https://api.vk.com/method/ads.importTargetContacts', data = {'account_id':str(adAccId), 'client_id':str(adClientId), 'contacts': userIdsString, 'access_token':Token,'v': '5.62', 'target_group_id': targetGroupId })
    