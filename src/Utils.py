from models import Context


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