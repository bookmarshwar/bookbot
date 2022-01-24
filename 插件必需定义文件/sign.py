
import sqlite3,datetime,random,requests
dbfile='/home/pi/NoneBot (复制 1)/ssd/test.db'#db绝对路径
class account():
    '''
        name:用户QQ\n
        time:最后使用时间\n
        db:返回list\n
        db[0]:用户qq\n
        db[1]:好感\n
        db[2]:金币\n
        db[3]:用户初始化时间\n
        db[4]:最后使用时间\n
    '''
    def __init__(self, name):
        self.name=name
        self.db=self.select()
        self.haogan=self.db[1]
        self.conts=self.db[2]
        self.starttime=self.db[3]
        self.time=self.db[4]
        self.name2=self.db[7]
    def select(self):
        '''
        返回dblist
        '''
        select=sqlite3.connect(dbfile)
        cursor=select.cursor()
        db=cursor.execute(f"SELECT *from 'ADS' where name={self.name};").fetchone()#向数据库查询用户表数据
        select.commit()
        select.close()
        if db==None:
            time=datetime.datetime.now().strftime('%Y-%m-%d')#获取当前时间
            
            sign=sqlite3.connect(dbfile)
            cursor=sign.cursor()
            cursor.execute(f"INSERT INTO 'ADS' (name,好感,金币,时间,time,events,state,name2) \
                  VALUES ({self.name},  0, 0, '{time}',0, 0, 0,0)")#创建记录
            sign.commit()
            sign.close()
            return self.name,0,0,time,0,0,0,0

        else:
            return db

    def update_haogan(self,haogan):
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE 'ADS' set 好感={haogan}  where name={self.name}")#更新表单数据
        update.commit()
        update.close()
    def update_conts(self,conts):
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE 'ADS' set 金币={conts}  where name={self.name}")#更新表单数据
        update.commit()
        update.close()
    def update_time(self,time):
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE 'ADS' set time='{time}'  where name={self.name}")#更新表单数据
        update.commit()
        update.close()
    def update_name(self,name2):
        update=sqlite3.connect(dbfile)
        cursor=update.cursor()
        cursor.execute(f"UPDATE 'ADS' set name2='{name2}'  where name={self.name}")#更新表单数据
        update.commit()
        update.close()
    def id_conts(self):
        return self.conts
    def id_time(self):
        return self.time
    def id_startime(self):
        return self.starttime
    def id_haogan(self):
        return self.haogan
    def id_name(self):
        return self.name2
    def accounts(self):
        return self.db

#c=account(5)
#c.update_haogan(666)
class paihang():
    def haogan(self,number):
        '''
        number:返回的数据个数
        '''

        select=sqlite3.connect(dbfile)
        cursor=select.cursor()
        db=cursor.execute(f"select * from 'ADS'  order by 好感 desc limit 0,{number};").fetchall()  #向数据库查询用户表数据
        select.commit()
        select.close()

        return db
    def conts(self,number):
        '''
        number:返回的数据个数
        '''
        select=sqlite3.connect(dbfile)
        cursor=select.cursor()
        db=cursor.execute(f"select * from 'ADS'  order by 金币 desc limit 0,{number};").fetchall()  #向数据库查询用户表数据
        select.commit()
        select.close()
        return db
class event_open():


    def __init__(self,accounts):
        self.conts=accounts[2]
        self.haogan=accounts[1]
        self.event=accounts[5]
        self.state=accounts[6]
        self.name=accounts[0]
    def event_info(self,info):

        pass
demo={3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:4,11:4,12:5,13:4,1:4,2:4}
def point():
    x=random.randint(1,13)
    while demo[x] <=0:
        x=random.randint(1,13)
        print(x)
    demo[x] =demo[x]-1
    return x#返回点数