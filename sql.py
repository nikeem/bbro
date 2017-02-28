import sys
import sqlite3

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    #cur.execute("CREATE TABLE Projs(ProjId INT, ProjName TEXT, ProjOwner INT, objsType INT, whatLookAt INT, adAccId INT, adClientId INT, targetGroupId INT, Token TEXT, Objs BLOB, LastState BLOB  )")
    cur.execute("INSERT INTO Projs VALUES(1,'Nik',1,1,1,1900002663,1603181057,8447268,'9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2','[72892095,45650931]','[123]')")
    cur.execute("INSERT INTO Projs VALUES(2,'Nik',1,1,2,1900002663,1603181057,8447268,'9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2','[72892095,45650931]','[123]')")
    cur.execute("INSERT INTO Projs VALUES(3,'Nik',1,1,3,1900002663,1603181057,8447268,'9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2','[72892095,45650931]','[123]')")
    
    
    
with con:
SELECT * FROM Orders WHERE Id=6