from django.db import models, transaction
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.db.models import Q, Count, Max
import glob
import json



class Lesson(models.Model):
    # MEDIA CHOICES
    QUESTION = 'question'
    LECTURE = 'lecture'
    KIND_CHOICES = (
        (LECTURE, 'lecture'),
        (QUESTION, 'question')
    )

    title = models.CharField(max_length=100)
    text = models.TextField(null=True)

    kind_choice = models.CharField(max_length=10, choices=KIND_CHOICES,
                            default=LECTURE)

    choice1 = models.TextField(null=True)
    choice2 = models.TextField(null=True)
    choice3 = models.TextField(null=True)
    choice4 = models.TextField(null=True)

    answer = models.IntegerField(null=True)

    time = models.DateTimeField('time submitted', default=timezone.now)

class Treatment(models.Model):
    lesson1 = models.ForeignKey('Lesson', related_name="treatment_lesson1", null=False)
    lesson2 = models.ForeignKey('Lesson', related_name="treatment_lesson2", null=False)
    lesson3 = models.ForeignKey('Lesson', related_name="treatment_lesson3", null=False)


class Test(models.Model):
    PRE = 'pre'
    POST = 'post'
    KIND_CHOICES = (
        (PRE, 'lecture'),
        (POST, 'question')
    )

    kind = models.CharField(max_length=10, choices=KIND_CHOICES,
                            default=PRE)
    lesson1 = models.ForeignKey('Lesson', related_name="lesson1", null=False)
    lesson2 = models.ForeignKey('Lesson', related_name="lesson2", null=False)
    lesson3 = models.ForeignKey('Lesson', related_name="lesson3", null=False)

class Student(models.Model):
    name = models.CharField(max_length=100)
    label = models.ForeignKey('Label', related_name="student_label", null=True)

class Context(models.Model):
    user = models.ForeignKey('Student', related_name="user", null=False)
    age = models.IntegerField(null=False)
    english_level = models.IntegerField(null=False)
    native_language = models.CharField(max_length=100)

class Label(models.Model):
    label = models.IntegerField(null=False)

class TreatmentLabel(models.Model):
    number_of_occurance = models.IntegerField(null=False)
    pre_test_total = models.IntegerField(null=False)
    post_test_total = models.IntegerField(null=False)

class TreatmentStudent(models.Model):
    treatment = models.ForeignKey('Treatment', related_name="treatment_id", null=False)
    student = models.ForeignKey('Student', related_name="student_id", null=False)
    pre_test_score = models.IntegerField(null=False)
    post_test_score = models.IntegerField(null=False)

class LessonStudent(models.Model):
    student = models.ForeignKey('Student', related_name="lesson_student", null=True)
    lesson = models.ForeignKey('Lesson', related_name="lesson", null=True)
    treatment_id = models.IntegerField(null=False)
    given_answer = models.IntegerField(null=False)