from mysql.connector import MySQLConnection

class sqlExecute():
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.config = {
            'user':'root',
            'password':'775477birhan',
            'host': '127.0.0.1'
        }
        self.learnerData ={}
        self.lessonData={}
        self.classData={}

    def run_execute(self, sorgu):
        connection = MySQLConnection(**self.config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sorgu)
        connection.commit()
        connection.close()
    def fetch_execute(self,sorgu):
        connection = MySQLConnection(**self.config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sorgu)
        data=cursor.fetchall()
        connection.close()
        return data

    #users
    def getUserInfo(self):
        return self.fetch_execute("select * from users where username='{}'".format(self.username))

    #learners
    def sameNumberLearnerControl(self,learnerNumber):
        existNumber=self.fetch_execute("select ogrenci_no from students")
        if (True if [i['ogrenci_no'] for i in existNumber].count(learnerNumber)>0 else False) is True:return True
    def addLearner(self,learnerInfo):
        query="insert into `students`(`ogrenci_no`, `ad`, `soyad`, `dogum_tarihi`, `cinsiyet`, `ev_adresi`, `mail_adresi`, `telefon`) values('{}','{}','{}','{}','{}','{}','{}','{}')"
        query=query.format(learnerInfo['ogrenci_no'],learnerInfo['ad'],learnerInfo['soyad'],learnerInfo['dogum_tarihi'],learnerInfo['cinsiyet'],learnerInfo['ev_adresi'],learnerInfo['mail_adresi'],learnerInfo['telefon'])

        self.run_execute(query)
    def getLearnersInfo(self):
        # for name and surname
        self.info_name_surname = []
        learners = self.fetch_execute("select * from students")
        [self.info_name_surname.append(learner['ad'] + " " + learner['soyad'] + " " + learner['ogrenci_no']) for learner in learners]
        self.learnerData['name_and_surname'] = self.info_name_surname
        return self.learnerData
    def updateLearnerInfo(self,newLearnerInfo):
        query="UPDATE `students` SET `ad`='{}',`soyad`='{}',`dogum_tarihi`='{}',`cinsiyet`='{}',`ev_adresi`='{}',`mail_adresi`='{}',`telefon`='{}' WHERE ogrenci_no={}"
        self.run_execute(query.format(newLearnerInfo['ad'],newLearnerInfo['soyad'],newLearnerInfo['dogum_tarihi'],newLearnerInfo['cinsiyet'],newLearnerInfo['ev_adresi'],newLearnerInfo['mail_adresi'],newLearnerInfo['telefon'],newLearnerInfo['ogrenci_no']))
    def theLearnerDelete(self,theLearnerNumber):
        self.run_execute("delete from `students` where ogrenci_no={}".format(theLearnerNumber))
    def getTheLearnerInfo(self,theLearnerNumber):
        #to get_info in section ogrenci
        return self.fetch_execute("select * from students where ogrenci_no='{}'".format(theLearnerNumber))
    def getLearnersInNoClass(self):
        learnersInfo = self.fetch_execute("select ogrenci_id,ogrenci_no,ad,soyad from students")
        takeLessonsId=[i['ogrenci_id'] for i in self.fetch_execute("select ogrenci_id from take_lesson")]


        for i in learnersInfo:
            if takeLessonsId.count(i['ogrenci_id'])>0:
                learnersInfo.remove(i)
        print(learnersInfo)


        return [i['ad']+" "+i['soyad']+" "+i['ogrenci_no'] for i in learnersInfo]
    def setLearnerToEmplace(self,class_learner_info):
        ogr_id=self.fetch_execute("select ogrenci_id from students where ogrenci_no='{}'".format(class_learner_info[-1]))[0]['ogrenci_id']
        print(ogr_id,class_learner_info[0])
        self.run_execute("insert into `take_lesson` (`ogrenci_id`,`sinif_id`) values('{}','{}')".format(ogr_id,class_learner_info[0]))


    #lessons
    def addLesson(self,lessonData):
        query = "insert into `lessons`(`ders_kod`, `ders_ismi`, `ders_tanim`, `ders_kredi`, `ders_akts`, `vize_yuzde`, `final_yuzde`) values('{}','{}','{}','{}','{}','{}','{}')"
        query = query.format(lessonData['ders_kod'], lessonData['ders_ismi'], lessonData['ders_tanim'],lessonData['ders_kredi'], lessonData['ders_akts'], lessonData['vize_yuzde'],lessonData['final_yuzde'])

        self.run_execute(query)
    def getLessonsInfo(self):
        # for lesson code and lesson name
        self.info_lesson_code_name= []
        lessons= self.fetch_execute("select * from lessons")
        [self.info_lesson_code_name.append(lesson['ders_kod'] + " " + lesson['ders_ismi']) for lesson in lessons]
        self.lessonData['code_name'] = self.info_lesson_code_name
        return self.lessonData

    #classes
    def sameClassCodeControl(self,classCode):
        existClass = self.fetch_execute("select sinif_id from classes")

        if (True if str([i['sinif_id'] for i in existClass]).count(classCode) > 0 else False) is True: return True
    def addClass(self,classData):
        query = "insert into `classes`(`sinif_id`, `sinif_ismi`) values('{}','{}')".format(classData['sinif_id'],classData['sinif_ismi'])

        self.run_execute(query)
    def getClassesInfo(self):
        # for class code and class name
        self.info_class_code_name = []
        classes = self.fetch_execute("select * from classes")

        [self.info_class_code_name.append(str(claSS['sinif_id']) + " " + claSS['sinif_ismi']) for claSS in classes]
        self.classData['code_name'] = self.info_class_code_name
        return self.classData
    def register(self,dictData):
        self.db_name = self.username
        #### CREATE TABLES ####
        try:
            query0 = "create database %s character set utf8 collate utf8_general_ci;" % (self.db_name)
            query1 = "create table users(username VARCHAR(50),password VARCHAR(30),name VARCHAR(300),surname VARCHAR(20), e_mail VARCHAR(30),department_no VARCHAR(30), user_type VARCHAR(30));"
            query2 = "create table students(ogrenci_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,ogrenci_no VARCHAR(50),ad VARCHAR(50),soyad VARCHAR(50),dogum_tarihi VARCHAR(300),cinsiyet VARCHAR(20), ev_adresi VARCHAR(80),mail_adresi VARCHAR(50), telefon VARCHAR(30));"
            query3 = "create table lessons(ders_kod INT NOT NULL AUTO_INCREMENT PRIMARY KEY,ders_ismi VARCHAR(50),ders_tanim VARCHAR(900),ders_kredi INT,ders_akts INT,vize_yuzde INT,final_yuzde INT);"
            query4 = "create table classes(sinif_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,sinif_ismi VARCHAR(80))"
            query5 = "create table notes (ogr_id INT NOT NULL,ders_kodu INT NOT NULL, sinif_id INT NOT NULL, vize_not INT,final_not INT, donem_bilgisi VARCHAR(50))"
            query6 = "create table roll_call (ogr_id INT NOT NULL,ders_kodu INT NOT NULL, sinif_id INT NOT NULL,hafta1 VARCHAR(8)," \
                     "hafta2 VARCHAR(8),hafta3 VARCHAR(8),hafta4 VARCHAR(8),hafta5 VARCHAR(8),hafta6 VARCHAR(8),hafta7 VARCHAR(8), " \
                     "hafta8 VARCHAR(8),hafta9 VARCHAR(8),hafta10 VARCHAR(8),hafta11 VARCHAR(8),hafta12 VARCHAR(8),hafta13 VARCHAR(8)," \
                     "hafta14 VARCHAR(8),hafta15 VARCHAR(8),hafta16 VARCHAR(8),donem_bilgisi VARCHAR (50))"
            query7="create table take_lesson(ogrenci_id INT NOT NULL, ders_kodu INT NOT NULL,sinif_id INT NOT NULL)"

            for query in [query0,query1,query2,query3,query4,query5,query6,query7]:
                self.run_execute(query)
                self.config['database'] = '%s' % (self.db_name)


        #### INSERT USER ###
            userInsert="INSERT INTO `users`(`username`, `password`, `name`, `surname`, `e_mail`, `department_no`, `user_type`) VALUES('{}','{}','{}','{}','{}','{}','{}')"
            userInsert=userInsert.format(dictData['kullaniciAdi'],dictData['sifre'],dictData['ad'],dictData['soyad'],dictData['ePosta'],dictData['bolumAdi'],'user')
            self.run_execute(userInsert)

        except:
            print(dictData['kullaniciAdi'],"adlı bir kullanıcı var")
    def login(self):
        not_get = ["information_schema", "performance_schema", "phpmyadmin", "mysql"]
        db = [i['Database'] for i in self.fetch_execute("SHOW DATABASES;")]
        [db.remove(i) for i in not_get]
        # is the username exist?
        if db.count(self.username)>0:
            self.config['database']=self.username
            #is the password correct?
            real_password= [i['password'] for i in self.fetch_execute("select password from users where username='{}'".format(self.username))][0]

            return (True if real_password==self.password else False)
        else:
            return False