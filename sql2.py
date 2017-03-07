import sys
import sqlite3

con = sqlite3.connect('test.db')

with con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Projs WHERE ProjId=8")
    
    #получили строку в форме tuple
    #print(cur.fetchone()[1])
    
    #распоковали tuple, полученный из базы в переменные.
    (ProjId,ProjName,ProjOwner,objsType,whatLookAt,adAccId,adClientId,targetGroupId,Token,Objs,LastState) = cur.fetchone()
    
    print(ProjId,ProjName,ProjOwner,objsType,whatLookAt,adAccId,adClientId,targetGroupId,Token,Objs,LastState)