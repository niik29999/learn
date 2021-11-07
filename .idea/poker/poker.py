import pandas as pd
import time

df_cards = pd.read_excel('C:\\Users\\niik\\Documents\\poker\\poker.xlsx',sheet_name='cards',index_col=0)
df_outs = pd.read_excel('C:\\Users\\niik\\Documents\\poker\\poker.xlsx',sheet_name='outs',index_col=0)
df_chance = pd.read_excel('C:\\Users\\niik\\Documents\\poker\\poker.xlsx',sheet_name='start_chance',index_col=0)
#print(df_cards.loc[['num'],['6']])

while True:
    #variables
    players_max = 9
    bet = 0.02
    bank = 0.05
    outs = 3
    logPath = 'C:\\Users\\niik\\AppData\\Local\\PokerStars\\PokerStars.log.0'

    # вероятность собрать сет
    def set(cards, all_cards_tpl, cards_count):
        card_count = 0
        for card in cards:
            if card not in '-':
                card_count = max(card_count,all_cards_tpl.count(card))

        cards_need = 3 - card_count
        j = 1
        for i in range(0,cards_need):
            j = j * ((4 - cards_need - i) / (cards_count - i))
            #print(j)

        return('Вероятность сет:  {0:10.3f}%'.format(j * 100))

    # вероятность флеша
    def flesh(suits, all_suits_tpl,cards_count):
        suit_count = 0
        for suit in suits:
            suit_count = max(suit_count,all_suits_tpl.count(suit))

        suits_need = 5 - suit_count

        if 7 - len(all_suits_tpl) - suits_need < 0:
            return('Вероятность флеша: 0%')
        else:
            j = 1
            for i in range(0,suits_need):
                j = j * ((13 - suit_count - i) / (cards_count - i))

            return('Вероятность флеша:  {0:10.3f}%'.format(j * 100))


    cards = '2,3,4,5,6,7,8,9,T,J,Q,K,A'.split(',')
    suits = 'c,h,s,d'.split(',')

    lines = []
    with open(logPath, 'r') as lorem_ipsum_text:
        for line in lorem_ipsum_text:
            if 'CocosTableState' in line:
                lines.append(line)

    hand_list = lines[len(lines)-1].replace('[','').replace(']','').replace('\'','').replace(',','').split(' ')
    my_cards = []
    my_suits = []
    my_cards_tpl = ()
    my_suits_tpl = ()

    for i in range(0,len(hand_list)-1):
        if 'Lo' in hand_list[i]:
            my_cards_tpl = tuple((hand_list[i+1][:1] + hand_list[i+2][:1] + hand_list[4][:1] \
                                  + hand_list[5][:1] + hand_list[6][:1] + hand_list[7][:1] + hand_list[8][:1]))

            my_suits_tpl = tuple(hand_list[i+1][1:2] + hand_list[i+2][1:2] + hand_list[4][1:2] \
                                 +  hand_list[5][1:2] +  hand_list[6][1:2]+  hand_list[7][1:2]+  hand_list[8][1:2])

            all_cards_tpl = tuple((hand_list[i+1][:1] + hand_list[i+2][:1] + hand_list[4][:1] \
                + hand_list[5][:1] + hand_list[6][:1] + hand_list[7][:1] + hand_list[8][:1]))

            all_suits_tpl = tuple(hand_list[i+1][1:2] + hand_list[i+2][1:2] + hand_list[4][1:2] \
                +  hand_list[5][1:2] +  hand_list[6][1:2]+  hand_list[7][1:2]+  hand_list[8][1:2])

    print(all_cards_tpl)
    #print(int(df_cards.loc[['num'],[all_cards_tpl[0]]].to_string(header=False, index=False)))
    print(all_suits_tpl)
    cards_count = 52 - len(all_suits_tpl)

    if int(df_cards.loc[['num'],[all_cards_tpl[0]]].to_string(header=False, index=False)) > int(df_cards.loc[['num'],[all_cards_tpl[1]]].to_string(header=False, index=False)):
        hand = str(all_cards_tpl[0]) + str(all_cards_tpl[1])
    else:
        hand = str(all_cards_tpl[1]) + str(all_cards_tpl[0])

    if all_suits_tpl[0] == all_suits_tpl[1]:
        hand = hand + 's'

    #print(hand)

    # start hand chance
    try:
        print('start hand chance to win ' + hand + ': ' + df_chance.loc[[hand],[players_max]].to_string(header=False, index=False))
    except:
        print('no_chance')

    # вероятность собрать сет
    x = set(my_cards_tpl, all_cards_tpl,cards_count)
    print(x)

    # вероятность собрать флеш
    x = flesh(my_suits_tpl, all_suits_tpl,cards_count)
    print(x)

    # chance
    df_outs['bank_chance'] = str(bank/bet) + ':1'
    print(df_outs.loc[[outs],['tern_1','river_1','tern_1_vr','river_1_vr','bank_chance']])

    time.sleep(7)


