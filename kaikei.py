menu = {
    1: ('下位プラン' , 600000),
    2: ('中位プラン' , 900000),
    3: ('上位プラン' , 1200000)
}

for number, (name,price) in menu.items():
    print(f'{number}: {name} {price:,}円')