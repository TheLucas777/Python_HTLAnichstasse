'''
dreizentes Übungsfile - Themen: Funktionen
Lucas
28.03.2022
'''
text_list = []


def reverse(list):
    for x in range(0, len(list)):
        tx = list[x]
        print(tx[::-1])


while (True):
    text = input("Write something (end = stop the program): ")
    if (text == "end"):
        reverse(text_list)
        break
    text_list.append(text)
