import xadmin
from xadmin import views
from xadmin.layout import Fieldset, Main, Row, Side

from acheve_mgt.models import MyClass, Student, Course, ScoreShip


class MyClassAdmin(object):
    list_display = ['name', 'grade', 'dept']
    ordering = ['-create_time', 'name', 'grade']
    serch_fields = ['name', 'grade', 'dept']


class StudentAdmin(object):
    list_display = ['number', 'name', 'myclass']
    ordering = ['-create_time', 'number']


class CourseAdmin(object):
    list_display = ['name', 'teacher_name', 'score']
    ordering = ['-create_time', 'score', 'name']


class ScoreShipAdmin(object):
    list_display = ['course', 'student', 'daily_score',
                    'exam_score', 'get_sum_score']
    # fieldsets = (
    #     ('None', {
    #         'fields':('course', 'student', 'daily_score', 'exam_score', 'get_sum_score'),
    #     }),
    # )
    # form_layout = (
    #     Main(
    #         Fieldset('',
    #                  'daily_score'),
    #     ),
    # )

    ordering = ['-create_time', 'term']

    # def get_sum_score(self, obj):
    #     return obj.exam_score*0.7 + obj.daily_score*0.3
    # get_sum_score.short_description = '单科成绩总评分'


#后台中各个注册模型排列顺序与注册顺序有关
xadmin.site.register(MyClass, MyClassAdmin)
xadmin.site.register(Student, StudentAdmin)
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(ScoreShip, ScoreShipAdmin)