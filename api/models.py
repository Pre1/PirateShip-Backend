from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver


class Profile(models.Model):

    # TODO: exp for user progress
    # TODO: tracking levels through courses
    # TODO: ranking

    pirate = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self):
        return "username: {} || first_name: {} || email: {}".format(
            self.pirate.username,
            self.pirate.first_name,
            self.pirate.email,
        )


## ======================================================= ##


class Course(models.Model):

    # TODO:

    name = models.CharField(max_length=50)
    title_color = models.CharField(max_length=50)
    image_url = models.ImageField(null=True, blank=True)
    is_available = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return "name: {} || available: {}".format(self.name, self.is_available)


## ======================================================= ##


class Level(models.Model):

    # TODO: goals as a TextField?
    # TODO: rel with Tag

    name = models.CharField(max_length=50)
    image_url = models.ImageField(null=True, blank=True)
    content = models.TextField()
    is_available = models.BooleanField(default=False)
    is_pass = models.BooleanField(default=False)
    course = models.ForeignKey(
        Course,
        null=True,
        on_delete=models.CASCADE,
        related_name="course_levels"
    )

    body_class_name = models.CharField(max_length=50)
    body_css = models.TextField()

    levels_tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return "name: {} || available: {}  || passed: {}".format(
            self.name,
            self.is_available,
            self.is_pass
        )


## ======================================================= ##


class Tag(models.Model):

    # TODO: rel with Level

    name = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    # level_tags = models.ForeignKey(
    #     Level, on_delete=models.CASCADE, related_name='level_tags')

    class Meta:
        pass

    def __str__(self):
        return "name: {} || content: {}".format(
            self.name,
            self.content,
        )


## ======================================================= ##


class Instruction(models.Model):

    # TODO: content field to fk? with Sentence Model
    expected = models.CharField(max_length=50)
    level = models.ForeignKey(
        Level, null=True, on_delete=models.CASCADE, related_name="level_instructions")

    class Meta:
        pass

    def __str__(self):
        return "expected: {}".format(
            self.expected,
        )


## ======================================================= ##

class Sentence(models.Model):

    # TODO: content field to fk? with Sentence Model

    content = models.CharField(max_length=50)
    instruction = models.ForeignKey(
        Instruction, null=True, on_delete=models.CASCADE, related_name="instruction_sentences")

    class Meta:
        pass

    def __str__(self):
        return "content: {}".format(
            self.content,
        )


## ======================================================= ##

class Style(models.Model):

    # TODO: rel with Tag
    # TODO: rel with Level

    class_name = models.CharField(max_length=50)
    tag_css = models.TextField()

    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, related_name="level_styles")
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, related_name="tag_styles")

    class Meta:
        pass

    def __str__(self):
        return "Class Name: {}".format(
            self.class_name,
        )
