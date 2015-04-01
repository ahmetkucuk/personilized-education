#!/usr/bin/env python
# __author__ = 'aburak'

import django
from src.models import *
from random import randint


class Customloader():

    def run(self):
        self.initialLessonsAndStudents()
        self.createTreatments()
        self.createTests()
        self.createTreatmentStudent()

    def initialLessonsAndStudents(self):
        for i in range(10):
            lesson = Lesson(title='Question' + str(i), text="Question text", choice1="A", choice2="B", choice3="C", choice4="D", answer=1, kind_choice=Lesson.QUESTION)
            lesson.save()

        for i in range(10):
            student = Student(name='Alper' + str(i))
            student.save()

    def createTreatments(self):
        lessons = Lesson.objects.all()

        for i in range(50):
            treatment = Treatment(lesson1=lessons[(i%10)], lesson2=lessons[((i+1)%10)], lesson3=lessons[((i+2)%10)])
            treatment.save()

    def createTests(self):

        preLesson1 = Lesson(title='Pre Question 1', text="Question text", choice1="A", choice2="B", choice3="C", choice4="D", answer=1, kind_choice=Lesson.QUESTION)
        preLesson2 = Lesson(title='Pre Question 2', text="Question text", choice1="A", choice2="B", choice3="C", choice4="D", answer=1, kind_choice=Lesson.QUESTION)
        preLesson3 = Lesson(title='Pre Question 3', text="Question text", choice1="A", choice2="B", choice3="C", choice4="D", answer=1, kind_choice=Lesson.QUESTION)

        preLesson1.save()
        preLesson2.save()
        preLesson3.save()

        preTest = Test(kind=Test.PRE, lesson1=preLesson1, lesson2=preLesson2, lesson3=preLesson3)
        preTest.save()

        postLesson1 = Lesson(title='Post Question 1', text="Question text", choice1="A", choice2="B", choice3="C", choice4="D", answer=1, kind_choice=Lesson.QUESTION)
        postLesson2 = Lesson(title='Post Question 2', text="Question text", choice1="A", choice2="B", choice3="C", choice4="D", answer=1, kind_choice=Lesson.QUESTION)
        postLesson3 = Lesson(title='Post Question 3', text="Question text", choice1="A", choice2="B", choice3="C", choice4="D", answer=1, kind_choice=Lesson.QUESTION)

        postLesson1.save()
        postLesson2.save()
        postLesson3.save()

        postTest = Test(kind=Test.POST, lesson1=postLesson1, lesson2=postLesson2, lesson3=postLesson3)
        postTest.save()

    def createTreatmentStudent(self):
        treatments = Treatment.objects.all()
        students = Student.objects.all()
        for i in range(10):
            currentStudent = students[i]
            for j in range(50):
                currentTreatment = treatments[j]
                preScore = randint(0, 3)
                treatmentStudent = TreatmentStudent(treatment=currentTreatment, student=currentStudent, pre_test_score=preScore, post_test_score=randint(preScore, 3))
                treatmentStudent.save()



if __name__ == "__main__":
    print("Run directly")
else:
    print("Imported")
    loader = Customloader()
    loader.run()

