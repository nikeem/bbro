import sys
import sqlite3

con = sqlite3.connect('test.db')

with con:
    
    cur = con.cursor()    
    #cur.execute("CREATE TABLE Projs(ProjId INT, ProjName TEXT, ProjOwner INT, objsType INT, whatLookAt INT, adAccId INT, adClientId INT, targetGroupId INT, Token TEXT, Objs BLOB, LastState BLOB  )")
    #cur.execute("INSERT INTO Projs VALUES(7,'Nik',1,1,1,1900002663,1603181057,8447268,'9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2','[72892095,45650931]','[123]')")
#    cur.execute("INSERT INTO Projs VALUES(2,'Nik',1,1,2,1900002663,1603181057,8447268,'9db2a2fed1095f2a477f08d467eed637d32d853f66e525671cac881a1a71fcb8ad6fca4968993072face2','[72892095,45650931]','[123]')")
    cur.execute("INSERT INTO Projs VALUES(7,'Nik',1,2,4,1900002663,1603181057,8447268,'9a03bc09de702b1bc8df9d00a576bc62cb4e6525ac62be696b779e3c00b93190a0d68859ca695edc89499','[5276994,163495609,12613645,12739958,40896309,1981304,225021324,189670472,13394386,2412123,212650644,4331659,109873610,257514883,45338456,397260742,6607401,80388432,202885980,48025865,28390614,6830548,345047164,194745576,82354574,23824178,73261516,1945523,16631653,2576586,152708028,7045235,5227245,60365297,322444724,6188064,308425099,1197563,32259262,8093941,4522102,193629598,28518036,176393064,257737041,55559271,29446705,163401907,240173710,16373845,219398452,5942850,49632845,182507782,80536012,2486955,164289532,190342971,8165924,29230317,209387171,2808733,406479433,190392320,329067528,6657637,23816806,101156135,263132649,270736037,301077140,165815803,268186231,156103682,145549080,40227562,11225206,17807345,344241940,131779883,85115667,224611445,366997024,7320149,244547658,179693195,30451960,267676766,7327116,305991534,6144447,13284897,34676054,20322911,329420492,72600806,194716599,137694037,582723,209287230,67462749,3027174,155563774,360845822,114223035,9511113,6196280,13167931,88604682,191576280,11634547,19354834,85528056,288637162,268190068,270154365,132734832,30146801,207571233,228213857,97868825,143953556,53788193,63875992,101225671,492448,3528632,3312043,88857194,154736215,243923351,93556746,203898660,112578717,29096993,252790397,22203592,4948346,152700708,46584504,155810758,38769139,296552842,5425587,1418216,114547970,16719899,153130158,242705025,52079513,60241080,53160982,5215791,83623961,37347785,329660850,360674963,54544310,261796839,71733782,955245,80986510,22483896,1031106,302357420,265778043,50403,119024044,45338456]','[1,2]')")
    
    
    
#with con:
#SELECT * FROM Projs WHERE ProjId=6


#1663923