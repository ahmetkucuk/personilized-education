from models import *
from scipy.cluster.vq import vq, kmeans, whiten
import numpy as np

def getLabel(context):
    if context.native_language == "English" or context.native_language == "english":
        if context.age > 15:
            return 7
        else:
            return 8
    else:
        if context.english_level == 1 or context.english_level == 2:
            if context.age > 15:
                return 1
            else:
                return 2
        if context.english_level == 3:
            if context.age > 15:
                return 3
            else:
                return 4
        if context.english_level == 4 or context.english_level == 5:
            if context.age > 15:
                return 5
            else:
                return 6


def makeclustering():
    contexts = Context.objects.all()
    data = np.zeros((contexts.count(), 3))
    for i in xrange(contexts.count()):
        data[i][0] = contexts[i].age
        data[i][1] = (contexts[i].english_level - 1) * 25
        if str(contexts[i].native_language).lower() == "english":
            data[i][2] = 0
        else:
            data[i][2] = 100

    whitened = whiten(data)
    centroids, disortion = kmeans(whitened, 8)

    idx, distortion = vq(whitened, centroids)

    print idx

    for i in xrange(len(idx)):
        contexts[i].user.label = Label.objects.get(pk=idx[i]+1)
        contexts[i].user.save()

def getTreatment(context):
    treatments = Treatment.objects.all()

    allTreatmentStudent = TreatmentStudent.objects.all()
    labelUsageCount = 0
    for i in xrange(allTreatmentStudent.count()):
        if allTreatmentStudent[i].student.label.label == context.user.label.label:
            labelUsageCount = labelUsageCount + 1


    treatmentInLabelCount = 0
    maxValue = 0
    treatment = Treatment()
    for i in xrange(treatments.count()):
        treatmentStudents = TreatmentStudent.objects.get(treatments=treatments[i])
        diffTotalValue = 0
        for k in xrange(treatmentStudents.count()):
            if treatmentStudents[k].student.label.label == context.user.label.label:
                treatmentInLabelCount = treatmentInLabelCount + 1
                diffTotalValue = treatmentStudents[k].pre_test_score - treatmentStudents[k].post_test_score
        avg = diffTotalValue / treatmentInLabelCount
        weightedProbabilityForIthTreatment = (treatmentInLabelCount / labelUsageCount) * avg
        if maxValue < weightedProbabilityForIthTreatment:
            maxValue = weightedProbabilityForIthTreatment
            treatment = treatments[i]
    return treatment

