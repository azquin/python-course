otazka = input('Ahoj, ake je tvoje priezvisko?: ')
otazka = otazka.lstrip()
otazka = otazka.rstrip()
dlzka = len(otazka)


if str(otazka[dlzka - 3]) + str(otazka[dlzka - 2]) + str(otazka[dlzka - 1]) == 'ova':
    print('hehe ty budes samica')
elif str(otazka[dlzka - 3]) + str(otazka[dlzka - 2]) + str(otazka[dlzka - 1]) == 'ová':
    print('si samicka picka')
elif str(otazka[dlzka - 2]) + str(otazka[dlzka - 1]) == 'ka':
    print('si samicka nejaka osemetna')
elif  str(otazka[dlzka - 2]) + str(otazka[dlzka - 1]) == 'ká':
    print('si samicka ')
else:
    print('si muz tak pal do pice')           
