# print('\u250c')
# print()
# print('\u252c')
# print()
# print('\u2510')
# print()
# print('\u251c')
# print()
# print('\u253c')
# print()
# print('\u2524')
# print()
# print('\u2514')
# print()
# print('\u2534')
# print()
# print('\u2518')
# print()
# print('\u2500')


from colorama import Fore, Style
def one_field(name1: str, name2: str, info1: str, info2:str):
    print('\u250c'+ "\u2500" + "\u2500" + "\u2500" + "\u252c" + "\u2500" + "\u2500" + "\u2500"+ '\u2510')
    print('| ' + Fore.RED + name1 + Style.RESET_ALL  + ' | ' + Fore.BLUE + name2 + Style.RESET_ALL  + ' |' +
          "\t\t\t" + Fore.RED + info1 + Style.RESET_ALL  + ' | ' + Fore.BLUE + info2 + Style.RESET_ALL)
    print('\u2514'+ "\u2500" + "\u2500" +"\u2500" + "\u2518" + "\u2500" + "\u2500" + "\u2500" + '\u2518')


