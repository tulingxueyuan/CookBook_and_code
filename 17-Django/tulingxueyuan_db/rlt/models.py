from django.db import models

# Create your models here.

class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)

    def __str__(self):
        return self.school_name




class Manager(models.Model):
    '''
    School:Manager=1:1
    add:
        Manager.objects.create(m_id, m_name, my_school)
        或者：
        s = School()
        m = Manager(x,x,x)
        m.save()
    query:
        query school:
        m1.my_schoo.school_name
        s = School.objects.get(manager__m_id=10).school_name
        query manager:
    change:
        单个修改： save
        批量修改： update
    delete：
        简单删除
    '''
    m_id = models.IntegerField()
    m_name = models.CharField(max_length=20)

    my_school = models.OneToOneField(School)

    def __str__(self):
        return self.m_name


class Teacher(models.Model):
    '''
    外键放在多的一边：
    add:
        同 1:1,两种方法，create和new
    query：
        t1.schools
        从school反向查找
        s1.teacher_set.all()
        Teacher.objects.filter(schools=s1)
        Teacher.objects.filter(schools__school_id=0)
    change:
        update
    delete:
        对象和queryset都可以用delete

    '''

    teacher_name = models.CharField(max_length=20)
    # 注意写法
    schools = models.ForeignKey("School")

class Student(models.Model):
    '''
    add:
        1: 如果是已有用户，用get
        st1 = Student.objects.create(student_name="stu1")
        stu.teachers.add(*ts)
        2:
        stu = ....
        t = Teacher.objects.create(xxxxx)
        t.student_set.add(stu)
    query:
        查询使用set查询即可，也可以使用双下划线
    delete：
        delete删除内容
        remove,clear删除关系

    '''

    student_name = models.CharField(max_length=20)
    teachers = models.ManyToManyField("Teacher")