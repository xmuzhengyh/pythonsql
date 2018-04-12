#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb


db = MySQLdb.connect(host="localhost",user="root",passwd="",db="zyhtest",port=3306,charset="utf8")
cursor = db.cursor()

def stu_in():

   sno=raw_input('sno:\n')
   name=raw_input('name:\n')
   sex=raw_input('sex:\n')
   age=raw_input('age:\n')
   classno=raw_input('classno:\n')
   dno=raw_input('dno:\n')
   try:
      cursor.execute("insert into student values('%s' , '%s' , '%s' , '%s','%s','%s')"%(sno,name, sex, age, classno, dno))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM student"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         sno = row[0]
         name = row[1]
         sex = row[2]
         age = row[3]
         classno=row[4]
         dno=row[5]
         print "sno:%s name:%s sex:%s age:%s classno:%s dno:%s" % (sno, name, sex, age,classno,dno)
   except:
      print "Error: unable to fecth data"

def stu_out():
   sno=raw_input('sno:\n')
   try:
      cursor.execute("delete from student where sno=%s"%(sno))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM student"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         sno = row[0]
         name = row[1]
         sex = row[2]
         age = row[3]
         classno=row[4]
         dno=row[5]
         print "sno:%s name:%s sex:%s age:%s classno:%s dno:%s" % (sno, name, sex, age,classno,dno)
   except:
      print "Error: unable to fecth data"

def course_in():
   cno = raw_input('cno:\n')
   subject = raw_input('subject:\n')
   time = input('time:\n')
   credit = input('credit:\n')
   try:
      cursor.execute("insert into course values('%s','%s','%d' ,'%d')" % (cno, subject, time, credit))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM course"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         cno = row[0]
         subject = row[1]
         time = row[2]
         credit = row[3]
         print "cno:%s subject:%s time:%d credit:%d" % (cno, subject, time, credit)
   except:
      print "Error: unable to fecth data"
def course_out():
   cno=raw_input('cno:\n')
   try:
      cursor.execute("delete from course where cno=%s"%(cno))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM course"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         cno = row[0]
         subject = row[1]
         time = row[2]
         credit = row[3]
         print "cno:%s subject:%s time:%d credit:%d" % (cno,subject,time,credit)
   except:
      print "Error: unable to fecth data"
def dept_in():
   dno = raw_input('dno:\n')
   dname = raw_input('dname:\n')
   try:
      cursor.execute("insert into dept values('%s','%s')" % (dno,dname))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM dept"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         dno = row[0]
         dname = row[1]
         print "dno:%s dname:%s" % (dno, dname)
   except:
      print "Error: unable to fecth data"

def dept_out():
   dno=raw_input('dno:\n')
   try:
      cursor.execute("delete from dept where dno=%s"%(dno))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM dept"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         dno = row[0]
         dname = row[1]
         print "dno:%s dname:%s" % (dno,dname)
   except:
      print "Error: unable to fecth data"
def class_in():
   classno = raw_input('classno:\n')
   num = input('num:\n')
   try:
      cursor.execute("insert into class(classno, num) values('%s','%d')" % (classno, num))
      db.commit()
   except:
      db.rollback()
      print "error"

   print "请输入%d名学生:"%num
   for i in range(0,num):
      stu_in()

   monitor=raw_input('请设置班长输入sno:\n')
   try:
      cursor.execute("update class set monitor='%s' where classno='%s'" % (monitor,classno))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM class"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         classno = row[0]
         num = row[1]
         monitor=row[2]
         print "classno:%s num:%d monitor:%s" % (classno, num,monitor)
   except:
      print "Error: unable to fecth data"


def class_out():
   classno = raw_input('classno:\n')
   print  classno
   try:
      cursor.execute("delete from class where classno=%s"%(classno))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM class"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         classno = row[0]
         num=row[1]
         monitor=row[2]
         print "classno:%s num:%d monitor:%s" % (classno,num,monitor)
   except:
      print "Error: unable to fecth data"

def study_in():
   sno = raw_input('sno:\n')
   cno = raw_input('cno:\n')
   score=input('score:\n')
   try:
      cursor.execute("insert into study values('%s','%s','%d')" % (sno, cno,score))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM study"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         sno = row[0]
         cno = row[1]
         score=row[2]
         print "sno:%s cno:%s score:%d" % (sno, cno,score)
   except:
      print "Error: unable to fecth data"

def study_out():
   sno = raw_input('sno:\n')
   cno = raw_input('cno:\n')
   try:
      cursor.execute("delete from study where sno=%s and cno=%s" % (sno,cno))
      db.commit()
   except:
      db.rollback()
      print "error"
   sql = "SELECT * FROM study"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         sno = row[0]
         cno =row[1]
         score=row[3]
         print "sno:%s cno:%s score:%d" % (sno, cno,score)
   except:
      print "Error: unable to fecth data"

def show_view():
   sql = "SELECT * FROM stuscore2"
   try:
      cursor.execute(sql)
      results = cursor.fetchall()
      for row in results:
         sno = row[0]
         name=row[1]
         dname=row[2]
         cno = row[3]
         subject=row[4]
         score = row[5]
         print "sno:%s name=%s dname=%s cno:%s subject=%s score:%d" % (sno,name,dname,cno,subject,score)
   except:
      print "Error: unable to fecth data"




while 1:
   print ('                          欢迎进入学生成绩管理系统！')
   t=raw_input("请输入有关表格操作 1、student 表 2、course 表 3、dept 表 4、class 表 5、study 表 6、成绩表\n请输入：")
   if t=='1':
      s=input("输入1.插入 2.删除\n")
      if s=='1':
         stu_in()
      elif s=='2':
         stu_out()
   elif t=='2':
      s = input("输入1.插入 2.删除\n")
      if s == '1':
         course_in()
      elif s == '2':
         course_out()
   elif t=='3':
      s = input("输入1.插入 2.删除\n")
      if s == '1':
         dept_in()
      elif s == '2':
         dept_out()
   elif t=='4':
      s = input("输入1.插入 2.删除\n")
      if s == '1':
         class_in()
      elif s == '2':
         class_out()
   elif t=='5':
      s = input("输入1.插入 2.删除\n")
      if s == '1':
         study_in()
      elif s == '2':
         study_out()
   elif t=='6':
      show_view()
   input()

