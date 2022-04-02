import os

txt_files = [ x for x in os.listdir(os.getcwd()) if x[-3:] == 'txt' ]
file_names = txt_files[:2]

print(f'{file_names[0]}와/과 {file_names[1]} 파일 대조를 시작합니다.\n================')

file_datas = [

]

for name in file_names:

    temple_name = open(f'{name}', 'r', encoding='utf-8')
    file_datas.append(temple_name.read())
    temple_name.close()



best_longer = max(map(len, file_datas))

same = 0


for a, b in zip(file_datas[0], file_datas[1]):
    if a == b:
        same += 1

print(f'대조를 완료했습니다.\n일치하는 갯수: {same}\n일치률: {same / best_longer * 100}')