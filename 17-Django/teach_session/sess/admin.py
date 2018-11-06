from django.contrib import admin
from sess.models import Teacher, ClassRoom, Student
# Register your models here.

class ClassRoomInfo(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = True
    list_display = ["loc", "className", "showName"]
    list_filter = ["loc", "className"]
    search_fields = ["loc", "className"]
    fieldsets = (
        ("第一个呀：", {"fields": ("loc",)}),
        ("第二个呀：", {"fields": ("className", )})
    )



class TeacherInfo(admin.ModelAdmin):
    list_display = ["name", "cource", "classroom", "roomloc"]

@admin.register(Student)
class StudentInfo(admin.ModelAdmin):
    pass


admin.site.register(ClassRoom, ClassRoomInfo)
admin.site.register(Teacher, TeacherInfo)

# admin.site.register(ClassRoom)
# admin.site.register(Teacher)
