text_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# text_list[1] = '"05"'     # можно так
# text_list[-2] = '"+05"'
# text_list[3] = '"17"'
text_list[1] = '05'
text_list[-2] = '+05'
# text_list.insert(1, '"')       # можно так
# text_list.insert(3, '"')
# text_list.insert(5, '"')
# text_list.insert(7, '"')
# text_list.insert(-1, '"')
# text_list.insert(-3, '"')
for idx in (1, 3, 5, 7, -2, -1):    # можно так
    text_list.insert(idx, '"')
cut_text_list = ' '.join(text_list)
print(cut_text_list)
