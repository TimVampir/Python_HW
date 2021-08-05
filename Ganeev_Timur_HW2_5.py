price = [68.2, 73.91, 58.12, 12.54, 73.21, 99.45, 24.17, 33.84, 54.85, 22.88]
new_price = []
for i in price:
    rub = int(i)
    kop = round((i - rub) * 100)
    new_price.append(f'{rub}руб {kop}коп')
print(new_price)