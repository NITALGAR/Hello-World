items = ['key','mouse','keybord']
prices = {'key':2,'mouse':5,'keybord':10}
ordre =input('Hi sir ! what you want to buy? : ')


if ordre in items:
    quan =  int(input(f'How many {ordre} you need? : '))
    price = prices[ordre]*quan
    print(f'That costs {price}$')
    print("Do you want to pay cash or card?")
else :
    print("Sorry we don't sell ",ordre)




















