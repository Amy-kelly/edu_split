import xadmin

from courseapp.models import Course, CourseCategory, CourseLesson, CourseChapter, Teacher
from courseapp.models import Activity,CourseDiscount,CourseDiscountType,CourseExpire,CoursePriceDiscount
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


#课程优惠类型表
class CourseDiscountTypeModelAdmin(object):
    pass
xadmin.site.register(CourseDiscountType,CourseDiscountTypeModelAdmin)

#课程优惠折扣表
class CourseDiscountModelAdmin(object):
    pass
xadmin.site.register(CourseDiscount,CourseDiscountModelAdmin)

#优惠活动表
class ActivityModelAdmin(object):
    pass
xadmin.site.register(Activity,ActivityModelAdmin)

#课程优惠策略优惠活动关系表
class CoursePriceDiscountModelAdmin(object):
    pass
xadmin.site.register(CoursePriceDiscount,CoursePriceDiscountModelAdmin)

#课程有效期表
class CourseExpireModelAdmin(object):
    pass
xadmin.site.register(CourseExpire,CourseExpireModelAdmin)
