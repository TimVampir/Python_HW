text_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in text_list:
    name_list = i.split()[-1]
    print('Привет, ', name_list.capitalize() + '!')