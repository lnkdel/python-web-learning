from peewee import *

db = SqliteDatabase('sampleDB.db')


class BaseModel(Model):
    class Meta:
        database = db


class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField(null=False)
    period = IntegerField()
    description = CharField()

    class Meta:
        order_by = ('title',)
        db_table = 'course'


class Teacher(BaseModel):
    id = PrimaryKeyField()
    name = CharField(null=False)
    gender = BooleanField()
    address = CharField()
    course_id = ForeignKeyField(Course, to_field='id', related_name='course')

    class Meta:
        order_by = ('name',)
        db_table = 'teacher'
        

# Course.create_table()
# Teacher.create_table()

# Course.create(id=1, title='经济学', period=320, description='文理科学生均可选修')
# Course.create(id=2, title='大学英语', period=300, description='大一学生必修课')
# Course.create(id=3, title='哲学', period=100, description='必修课')
# Course.create(id=104, title='编译原理', period=100, description='必修课')
# Teacher.create(name='白求恩', gender=True,address='...',course_id=1)
# Teacher.create(name='李申', gender=True,address='...',course_id=3)
# Teacher.create(name='张文', gender=False,address='...',course_id=2)

# record = Course.get(Course.title=='大学英语')
# print ('课程: {0}, 学时: {1}'.format(record.title, record.period))

# # 更新
# record.period = 200
# record.save()

# record = Course.get(Course.title=='大学英语')
# print ('课程: {0}, 学时: {1}'.format(record.title, record.period))

# 删除
# record.delete_instance()

# courses = Course.select()
# for course in courses:
#     print(course.title)

# courses = Course.select().where(Course.id<10).order_by(Course.period.desc())
# for course in courses:
#     print(course.title)

total = Course.select(Course, fn.Avg(Course.period).alias('avg_period'))
for t in total:
    print(t.period)

