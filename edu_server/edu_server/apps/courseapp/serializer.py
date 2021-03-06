from rest_framework.serializers import ModelSerializer

from courseapp.models import CourseCategory, Course, Teacher, CourseChapter


# 课程分类
class CourseCategorySerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ["id", "name"]


# 课程所属老师的序列化器
class CourseTeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id","image", "name", "title", "signature","brief")


#课时章节表的序列化器
class CourseChapterSerializer(ModelSerializer):
    class Meta:
        model = CourseChapter
        fields = ("id","chapter","name")

# 课程列表
class CourseModelSerializer(ModelSerializer):
    # 序列化器嵌套查询老师信息
    teacher = CourseTeacherSerializer()
    # course = CourseChapterSerializer()

    class Meta:
        model = Course
        fields = ["id", "name", "course_img","question","lesson_level","course_video","brief_show",
                  "students", "lessons", "pub_lessons", "price", "teacher","chapter_list","lesson_list",
                  "discount_name","real_price","active_time"]


#评论
class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id","comment","question"]

        extra_kwargs = {
            "question":{
                "read_only":True
            }
        }