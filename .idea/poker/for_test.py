suits = 'c,h,s,d'.split(',')
cards = '2,3,4,5,6,7,8,9,T,J,Q,K,A'.split(',')
cards_suits = []
cards_temp = []

for i in range(0,len(cards)):
    for j in range(0,len(suits)):
        cards_temp.append(cards[i] + suits[j])
    cards_suits.append(tuple(cards_temp))
    cards_temp = []

print(cards_suits)
print(suits)
print(cards)

lines = []
with open('C:\\Users\\niik\\AppData\\Local\\PokerStars\\PokerStars.log.0', 'r') as lorem_ipsum_text:
    for line in lorem_ipsum_text:
        if 'CocosTableState' in line:
            lines.append(line)

print(lines[len(lines)-1])
hand_list = lines[len(lines)-1].replace('[','').replace(']','').replace('\'','').replace(',','').split(' ')
print(hand_list)
print(len(hand_list))
my_cards = []
my_cards_tpl = ()

for i in range(0,len(hand_list)-1):
    if 'Lo' in hand_list[i]:
        my_cards.append(tuple(hand_list[i+1][:2]))
        my_cards.append(tuple(hand_list[i+2][:2]))
        my_cards.append(tuple(hand_list[4][:2]))
        my_cards.append(tuple(hand_list[5][:2]))
        my_cards.append(tuple(hand_list[6][:2]))
        my_cards.append(tuple(hand_list[7][:2]))
        my_cards.append(tuple(hand_list[8][:2]))

print(my_cards)
# my_cards_tpl = tuple(my_cards)
# print(my_cards_tpl)

for t1, t2, t3, t4 in cards_suits:
    print(t1, t2, t3, t4)
    # print(cards_suits.index(t1))

def fix_tuple(my_cards):
    try:
        for t1, t2 in my_cards:
            return(t1, t2)
    except ValueError:
        return None

t1, t2 = par(my_cards)
print(t1, t2)

# import poker




#print(len(lines))


# C:\Users\niik2\AppData\Local\Programs\Python\Python37\python.exe -m pip install poker
# import poker
# import pandas as pd
# from poker.room.pokerstars import Notes
# from poker.room.pokerstars import PokerStarsHandHistory


# files = GetFiles('C:\\Users\\niik2\\AppData\\Local\\PokerStars\\HandHistory\\niik2999\\HH20210417 Potomac II - $0,01-$0,02 - USD Без лимита Холдем.txt')


# notes = Notes.from_file('C:\\Users\\niik2\AppData\\Local\\PokerStars\\notes.niik2999.xml')
# print(notes.players)
# print(notes.labels)

# status = get_status()
# print(status.players)

#hh = PokerStarsHandHistory('C:\\Users\\niik2\\AppData\\Local\\PokerStars\\HandHistory\\niik2999\\HH20210417 Potomac II - $0,01-$0,02 - USD Без лимита Холдем.txt')
#print(hh.parse())

#print(list(poker.Suit))
#print(list(poker.Rank))
#print(list(poker.Hand))



