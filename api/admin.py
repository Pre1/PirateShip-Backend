from django.contrib import admin
from .models import (
    Profile,
    Course,
    Level,
    Tag,
    Instruction,
    Style,
    Sentence
)

admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Tag)
admin.site.register(Sentence)
admin.site.register(Instruction)
admin.site.register(Style)
