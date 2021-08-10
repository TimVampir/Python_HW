# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором
# ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.


def thesaurus(*args):
    my_dict = {}
    for i in args:
        key = i[0].capitalize()
        if key not in my_dict:
            my_dict[key] = []
        my_dict[key].append(i)
    return my_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
