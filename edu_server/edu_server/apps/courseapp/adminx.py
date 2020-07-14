import xadmin

from courseapp.models import Course, CourseCategory, CourseLesson, CourseChapter, Teacher

#课程分类表
class CourseCategoryModelAdmin(object):
    pass


xadmin.site.register(CourseCategory, CourseCategoryModelAdmin)

#课程信息表
class CourseModelAdmin(object):

    pass


xadmin.site.register(Course, CourseModelAdmin)

#课程章节表
class CourseChapterModelAdmin(object):

    pass


xadmin.site.register(CourseChapter, CourseChapterModelAdmin)

#课程课时表
class CourseLessonModelAdmin(object):

    pass


xadmin.site.register(CourseLesson, CourseLessonModelAdmin)

#讲师表
class TeacherModelAdmin(object):

    pass


xadmin.site.register(Teacher, TeacherModelAdmin)
