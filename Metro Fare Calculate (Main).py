def separate(station):
    if station == 'CEN':
        return 'CEN',0
    else:
        station_letter = station[0]
        station_num = int(station[1:len(station)])
        return station_letter,station_num

def calculate(letter_one,num_one,letter_two,num_two):
    extra = 0
    n_extra = 0
    st_extra = 0
    se_extre = 0
    super_extra = 0

    if (letter_one == 'N' and letter_two == 'N' and num_one == 8 and num_two == 8):
        super_extra = 16
    elif (letter_one == 'E' and letter_two == 'E' and num_one == 9 and num_two == 9):
        super_extra = 16
    elif (letter_one == 'E' and letter_two == 'E' and num_one == 14 and num_two == 14):
        super_extra = 1
    elif (letter_one == 'S' and letter_two == 'S' and num_one == 8 and num_two == 8):
        super_extra = 16
    elif (letter_one == 'E' and letter_two == 'E' and num_one >= 14 and num_two >= 14):
        super_extra = 999
    elif (letter_one == 'E' and letter_two == 'E' and num_one >= 9 and num_two >= 9):
        super_extra = 1
    elif (letter_one == 'N' and letter_two == 'N' and num_one >= 8 and num_two >= 8):
        super_extra = 999
    elif (letter_one == 'S' and letter_two == 'S' and num_one >= 8 and num_two >= 8):
        super_extra = 1

    if (letter_one == 'N' and num_one >= 9):
        num_one = 8
    if (letter_two == 'N' and num_two >= 9):
        num_two = 8
    if (letter_one == 'E' and num_one >= 10):
        num_one = 9
        extra = extra + 1
    if (letter_two == 'E' and num_two >= 10):
        num_two = 9
        extra = extra + 1
    if (letter_one == 'S' and num_one >= 9):
        num_one = 8
        extra = extra + 1
    if (letter_two == 'S' and num_two >= 9):
        num_two = 8
        extra = extra + 1

    if (letter_one == 'N' and letter_two == 'N'):
        if (num_one > num_two):
            count = num_one - num_two
        elif (num_one < num_two):
            count = num_two - num_one
        elif (num_one == num_two):
            count = 0
    elif (letter_one == 'E' and letter_two == 'E'):
        if (num_one > num_two):
            count = num_one - num_two
        elif (num_one < num_two):
            count = num_two - num_one
        elif (num_one == num_two):
            count = 0
    elif (letter_one == 'S' and letter_two == 'S'):
        if (num_one > num_two):
            count = num_one - num_two
        elif (num_one < num_two):
            count = num_two - num_one
        elif (num_one == num_two):
            count = 0
    elif (letter_one == 'W' and letter_two == 'W'):
        count = 0
    elif (letter_one == 'CEN'):
        count = num_two
    elif (letter_two == 'CEN'):
        count = num_one
    else:
        count = num_one + num_two

    if (count <= 1):
        price = 16
    elif (count == 2):
        price = 23
    elif (count == 3):
        price = 26
    elif (count == 4):
        price = 30
    elif (count == 5):
        price = 33
    elif (count == 6):
        price = 37
    elif (count == 7):
        price = 40
    elif (count >= 8):
        price = 44

    if (extra != 0):
        n_extra = 15
        st_extra = 10
        se_extre = 7

    if (super_extra == 999):
        n_price = 0
        st_price = 0
        se_price = 0
    elif (super_extra == 1):
        n_price = 15
        st_price = 10
        se_price = 7
    elif (super_extra == 16):
        n_price = 16
        st_price = 16
        se_price = 8
    else:
        n_price = price + n_extra
        st_price = price + st_extra
        se_price = (price / 2) + se_extre

    if ((se_price % 1) != 0):
        se_price = se_price + 0.5

    return n_price,st_price,se_price

th_station_name = {'CEN': 'สยาม', 'N1': 'สถานีราชเทวี', 'N2': 'สถานีพญาไท', 'N3': 'สถานีอนุสาวรีย์ชัยสมรภูมิ',
                   'N4': 'สถานีสนามเป้า', 'N5': 'สถานีอารีย์', 'N6': '*สถานีในอนาคต*',
                   'N7': 'สถานีสะพานควาย', 'N8': 'สถานีหมอซิต', 'N9': 'สถานีห้าแยกลาดพร้าว', 'N10': 'สถานีพหลโยธิน 24',
                   'N11': 'สถานีรัชโยธิน', 'N12': 'สถานีเสนานิคม', 'N13': 'สถานีมหาวิทยาลัยเกษตรศาสตร์',
                   'N14': 'สถานีกรมป่าไม้', 'N15': 'สถานีบางบัว', 'N16': 'สถานีกรมทหารราบที่ 11',
                   'N17': 'สถานีวัตพระศรีมหาธาตุ', 'N18': 'สถานีพหลโยธิน 59', 'N19': 'สถานีสายหยุด',
                   'N20': 'สถานีสะพานใหม่', 'N21': 'สถานีโรงพยาบาลภูมิพลอดุลยเดช', 'N22': 'สถานีพิพิธภัณฑ์กองทัพอากาศ',
                   'N23': 'สถานีแยก คปอ.', 'N24': 'สถานีคูคต', 'E1': 'สถานีชิดลม', 'E2': 'สถานีเพลินจิต',
                   'E3': 'สถานีนานา', 'E4': 'สถานีอโศก', 'E5': 'สถานีพร้อมพงษ์', 'E6': 'สถานีทองหล่อ',
                   'E7': 'สถานีเอกมัย', 'E8': 'สถานีพระโขนง', 'E9': 'สถานีอ่อนนุช', 'E10': 'สถานีบางจาก',
                   'E11': 'สถานีปุณณวิถี', 'E12': 'สถานีอุดมสุข', 'E13': 'สถานีบางนา', 'E14': 'สถานีแบริ่ง',
                   'E15': 'สถานีสำโรง', 'E16': 'สถานีปู่เจ้า', 'E17': 'สถานีช้างเอราวัณ', 'E18': 'สถานีโรงเรียนนายเรือ',
                   'E19': 'สถานีปากน้ำ', 'E20': 'สถานีศรีนครินทร์', 'E21': 'สถานีแพรกษา', 'E22': 'สถานีสายลวด',
                   'E23': 'สถานีเคหะฯ', 'W1': 'สถานีสนามกีฬาแห่งชาติ', 'S1': 'สถานีราชดำริ', 'S2': 'สถานีศาลาแดง',
                   'S3': 'สถานีช่องนนทรี', 'S4': 'สถานีเซนต์หลุยส์', 'S5': 'สถานีสุรศักดิ์', 'S6': 'สถานีสะพานตากสิน',
                   'S7': 'สถานีกรุงธนบุรี', 'S8': 'สถานีวงเวียนใหญ่', 'S9': 'สถานีโพธิ์นิมิตร', 'S10': 'สถานีตลาดพลู',
                   'S11': 'สถานีวุฒากาศ', 'S12': 'สถานีบางหว้า'}

eng_station_name = {'CEN': 'Siam Station', 'N1': 'Ratchathewi Station', 'N2': 'Phaya Thai Station',
                    'N3': 'Victory Monument Station', 'N4': 'Sanam Pao Station', 'N5': 'Ari Station',
                    'N6': '*Future BTS SkyTrain Station*', 'N7': 'Saphan Khwai Station', 'N8': 'Mo Chit Station',
                    'N9': 'Ha Yaek Lat Phrao Station', 'N10': 'Phahon Yothin 24 Station', 'N11': 'Ratchayothin Station',
                    'N12': 'Sena Nikhom Station', 'N13': 'Kasetsart University Station',
                    'N14': 'Royal Forest Department Station', 'N15': 'Bang Bua Station',
                    'N16': '11th Infantry Regiment Station', 'N17': 'Wat Phra Si Mahathat Station',
                    'N18': 'Phahon Yothin 59 Station', 'N19': 'Sai Yud Station', 'N20': 'Saphan Mai Station',
                    'N21': 'Bhumibol Adulyadej Hospital Station', 'N22': 'Royal Thai Air Force Museum Station',
                    'N23': 'Yaek Kor Por Aor Station', 'N24': 'Khu Khot Station', 'E1': 'Chit Lom Station',
                    'E2': 'Phloen Chit Station', 'E3': 'Nana Station', 'E4': 'Asok Station',
                    'E5': 'Phrom Phong Station', 'E6': 'Thong Lo Station', 'E7': 'Ekkamai Station',
                    'E8': 'Phra Khanong Station',
                    'E9': 'On Nut Station', 'E10': 'Bang Chak Station',
                    'E11': 'Punnawithi Station', 'E12': 'Udom Suk Station', 'E13': 'Bang Na Station',
                    'E14': 'Bearing Station', 'E15': 'Samrong Station', 'E16': 'Pu Chao Station',
                    'E17': 'Chang Erawan Station',
                    'E18': 'Royal Thai Naval Academy Station', 'E19': 'Pak Nam Station', 'E20': 'Srinagarindra Station',
                    'E21': 'Phraek Sa Station',
                    'E22': 'Sai Luat Station', 'E23': 'Kheha Station', 'W1': 'National Stadium Station',
                    'S1': 'Ratchadamri Station',
                    'S2': 'Sala Daeng Station', 'S3': 'Chong Nonsi Station', 'S4': 'Saint Louis Station',
                    'S5': 'Surasak Station',
                    'S6': 'Saphan Taksin Station', 'S7': 'Krung Thon Buri Station', 'S8': 'Wongwian Yai Station',
                    'S9': 'Pho Nimit Station',
                    'S10': 'Talat Phlu Station', 'S11': 'Wutthakat Station', 'S12': 'Bang Wa Station'}

print('เลือกหนึ่งอัน (CEN/N1-N5,N7-N24/S1-S12/E1-E23/W1/IDK เพื่อแสดงรายซื่อสถานี)')
print('Choose one (CEN/N1-N5,N7-N24/S1-S12/E1-E23/W1/IDK to show stations name.)')

first_station_code = str(input('กรุณาเลือกสถานีต้นทาง - Enter origin station : '))
first_station_code = first_station_code.upper()

if first_station_code == 'IDK':
    print('@ CEN')
    x = 'CEN'
    print('[CEN]', th_station_name.get(x), '-', eng_station_name.get(x))
    print('@ NORTH')
    i = 1
    while i <= 24:
        z = str(i)
        x = 'N' + z
        print('[' + x + ']', th_station_name.get(x), '-', eng_station_name.get(x))
        i = i + 1
    print('@ EAST')
    i = 1
    while i <= 23:
        z = str(i)
        x = 'E' + z
        print('[' + x + ']', th_station_name.get(x), '-', eng_station_name.get(x))
        i = i + 1
    print('@ WEST')
    x = 'W1'
    print('[W1]', th_station_name.get(x), '-', eng_station_name.get(x))
    i = 1
    print('@ SOUTH')
    while i <= 12:
        z = str(i)
        x = 'S' + z
        print('[' + x + ']', th_station_name.get(x), '-', eng_station_name.get(x))
        i = i + 1
    first_station_code = str(input('กรุณาเลือกสถานีต้นทาง Enter origin station : '))
    first_station_code = first_station_code.upper()

second_station_code = str(input('กรุณาเลือกสถานีปลายทาง Enter destination station : '))
second_station_code = second_station_code.upper()

#setupข้อมูล
th_name_one ,eng_name_one= th_station_name.get(first_station_code),eng_station_name.get(first_station_code)
th_name_two, eng_name_two= th_station_name.get(second_station_code),eng_station_name.get(second_station_code)
letter_one,num_one = separate(first_station_code)
letter_two,num_two = separate(second_station_code)

print()  # เว้นบรรทัด

#แสดงเส้นทางที่เลือก
print('จาก', th_name_one + '[' + first_station_code + '] ไป',
      th_name_two + '[' + second_station_code + ']')
print('From', eng_name_one + '[' + first_station_code + '] To',
      eng_name_two + '[' + second_station_code + ']')
print()


#คำนวน
n_price,st_price,se_price = calculate(letter_one,num_one,letter_two,num_two)


#เลือกประเภทบัตร
print('ใส่ประเภทบัตร (1:ผู้ใหญ่/บุคคลธรรมดา 2:นักเรัยน-นักศึกษา 3:ผู้สูงอายุ 4:แสดงทั้งหมด)')
print('Enter card type (1:Adult/Normal 2:Student 3:Senior 4:Show All)')
people_type = int(input('Choose one : '))
print()  # เว้นบรรทัด

#showประเภทบัตร,ราคา
if people_type == 1:
    print('ราคาผู้ใหญ่/บุคคลธรรมดา - Normal/Adult Price =', int(n_price), 'Baht')
elif people_type == 2:
    print('ราคานักเรัยนนักศึกษา - Student Price =', int(st_price), 'Baht')
elif people_type == 3:
    print('ราคาผู้สูงอายุ - Senior Price =', int(se_price), 'Baht')
elif people_type == 4:
    print('ราคาผู้ใหญ่/บุคคลธรรมดา - Normal/Adult Price =', int(n_price), 'Baht')
    print('ราคานักเรัยน นักศึกษา - Student Price =', int(st_price), 'Baht')
    print('ราคาผู้สูงอายุ - Senior Price =', int(se_price), 'Baht')
else:
    print('!Please Enter 1/2/3/4 Only!')

print()

#เปลี่ยนรถ(หากมี)
if (letter_two == 'N' and letter_one != 'N' and letter_one != 'E' and letter_one != 'CEN'):
    print('กรุณาเปลี่ยนรถที่สถานีสยาม(CEN) ชานชาลาที่ 2')
    print('Please change the car at Siam Station(CEN), Platform 2.')
    print()
elif (letter_two == 'E' and letter_one != 'E' and letter_one != 'N' and letter_one != 'CEN'):
    print('กรุณาเปลี่ยนรถที่สถานีสยาม(CEN) ชานชาลาที่ 1')
    print('Please change the car at Siam Station(CEN), Platform 1.')
    print()
elif (letter_two == 'W' and letter_one != 'W' and letter_one != 'S' and letter_one != 'CEN'):
    print('กรุณาเปลี่ยนรถที่สถานีสยาม(CEN) ชานชาลาที่ 4')
    print('Please change the car at Siam Station(CEN), Platform 4.')
    print()
elif (letter_two == 'S' and letter_one != 'S' and letter_one != 'W' and letter_one != 'CEN'):
    print('กรุณาเปลี่ยนรถที่สถานีสยาม(CEN) ชานชาลาที่ 3')
    print('Please change the car at Siam Station(CEN), Platform 3.')
    print()

print('_/|\_ ขอบคุณที่ใช้บริการ _/|\_')
print('Thank you for using the service, Have a nice day.')