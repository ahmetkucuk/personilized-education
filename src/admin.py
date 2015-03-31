from django.contrib import admin
import src.models

admin.site.register(src.models.Context)
admin.site.register(src.models.Lesson)
admin.site.register(src.models.LessonStudent)
admin.site.register(src.models.Student)
admin.site.register(src.models.Test)
admin.site.register(src.models.TreatmentStudent)
admin.site.register(src.models.Treatment)
admin.site.register(src.models.TreatmentLabel)
admin.site.register(src.models.Label)
