#!/usr/bin/python
#encoding:utf-8
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
import MySQLdb

#create a cursor

def insertFoodClassify(classify_name):
    conn = MySQLdb.connect('localhost','root','RaoLiang','test')
    print 'insertFoodClassify:' + classify_name
    classify_name = re.sub(ur'\'|\"','',classify_name)
    cursor = conn.cursor()
    cursor.execute("select id from food_classify where classify_name='"+classify_name+"'")
    result = cursor.fetchall()
    if(result):
        return result[0][0]
    cursor.execute("INSERT INTO food_classify(classify_name) VALUES('"+classify_name+"')")
    food_classify_id = int(cursor.lastrowid)
    conn.commit()
    conn.close()
    return food_classify_id

def insertFood(name,alias,heat,carbohydrate,fat,protein,classify_id,img):
    conn = MySQLdb.connect('localhost','root','RaoLiang','test')
    name = re.sub(ur'\'|\"','',name)
    alias = re.sub(ur'\'|\"','',alias)
    print 'insertFood:' + name+","+str(alias)+","+str(heat)+","+str(carbohydrate)+","+str(fat)+","+str(protein)+","+str(classify_id)+",'"+img
    cursor = conn.cursor()
    sql = "INSERT INTO food(name,alias,heat,carbohydrate,fat,protein,classify_id,img) VALUES('"+name+"','"+str(alias)+"',"+str(heat)+","+str(carbohydrate)+","+str(fat)+","+str(protein)+","+str(classify_id)+",'"+img+"')"
    cursor.execute(sql)
    food_id = int(cursor.lastrowid)
    conn.commit()
    conn.close()
    return food_id

def insertFoodEnergyRuler(food_id,food_classify_name,heat):
    conn = MySQLdb.connect('localhost','root','RaoLiang','test')
    food_classify_name = re.sub(ur'\'|\"','',food_classify_name)
    print 'insertFoodEnergyRuler:' + str(food_id)+",'"+food_classify_name+"',"+str(heat)
    cursor = conn.cursor()
    sql = "INSERT INTO food_energy_ruler(food_id,food_classify_name,heat) VALUES("+str(food_id)+",'"+food_classify_name+"',"+str(heat)+")"
    cursor.execute(sql)
    food_energy_id = int(cursor.lastrowid)
    conn.commit()
    conn.close()
    return food_energy_id

allNames = []
allAliases = []
def exportData(startId):
    conn = MySQLdb.connect('localhost','root','RaoLiang','test')
    cursor = conn.cursor()
    sql = "select * from food where id>" + str(startId) + " order by id asc limit 500 "
    cursor.execute(sql)
    results = cursor.fetchall()
    i = 0
    if(len(results) == 0):
        print "no more data"
        exit(0)
    exportFileHandl = open(exportFile,'w')
    for row in results:
        i = row[0]
        name = filter(row[1], False)
        alias = []
        if(row[2]):
            alias = filter(row[2], True)
        if(name):
            if name not in allNames:
                print name
                exportFileHandl.writelines(name)
                allNames.append(name)
                if(alias):
                    for a in alias:
                        if a not in allAliases:
                            print "#" + a
                            exportFileHandl.writelines("#" + a)
                            allAliases.append(a)
    exportData(i)


def filter(strIn,isArr):
    if(strIn):
        strIn = re.sub(ur'[，|，]','、',strIn.decode("utf8"))
        strIn = re.sub(ur'(\(.*?\))','',strIn)
        strIn = re.sub(ur'(（.*?\）)','',strIn)
        if(not isArr):
            return strIn
        if(strIn):
            strArr = strIn.split('、')
            strArr = set(strArr)
            return strArr
        else:
            return []
    else:
        return []

exportFile = './foodData.txt'
exportData(0)
#a = filter("a，(a)b(b)c(c)    a（a）b（b）c（c）",False)
#print insertFoodClassify('te\'a\"st4')
#print insertFood('玉米','别名',1.1,2.2,3.3,4.4,1,'http://www.baidu.com')
#print insertFoodEnergyRuler(1,'玉米',1.22)
