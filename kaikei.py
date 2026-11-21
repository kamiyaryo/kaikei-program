menu = {
    1: ('上位プラン' , 1200000),
    2: ('中位プラン' , 900000),
    3: ('下位プラン' , 600000)
}

for number, (name,price) in menu.items():
    print(f'{number}: {name} {price:,}円')

total = 0
sale_list = []
print(f'0: 入力終了')

while True:
    try:
        number = int(input('プラン番号を入力してください: '))
    except ValueError:
        print('数字を入力してください')
        continue
    if number == 0:
        break
    if number not in menu:
        print('そのプランはありません')
        continue
    name,price = menu[number]
    print(f'選択: {name} ({price:,}円)')

    while True:
        try:
            count = int(input('契約件数を入力してください: '))
            if count <= 0:
                print('契約件数は1以上で入力してください')
                continue
            break
        except ValueError:
            print('数字を入力してください')
    subtotal = price * count
    lines = f'{name} {price:,}円　x　{count}件 = {subtotal:,}円 '
    print(lines)
    total += subtotal
    sale_list.append(lines)

print('-- 営業売上集計 --')
for lines in sale_list:
     print(lines)
print(f'合計売上: {total:,}円')
if total >= 3000000:
     incentive = total * 10 // 100
     print(f'インセンティブ: {incentive:,}円')