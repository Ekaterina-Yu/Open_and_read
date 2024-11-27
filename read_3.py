import os

with open('1.txt', 'r', encoding='utf-8') as f_1, open('2.txt', 'r', encoding='utf-8') as f_2, open('3.txt', 'r', encoding='utf-8') as f_3:
    
    txt_dict = {}

    xx = f_1.read()
    ss = f_2.read()
    ww = f_3.read()

    file_path_1 = '/1.txt'
    nof_1 = os.path.basename(file_path_1)
    
    file_path_2 = '/2.txt'
    nof_2 = os.path.basename(file_path_2)
    
    file_path_3 = '/3.txt'
    nof_3 = os.path.basename(file_path_3)
    
with open('1.txt', 'r', encoding='utf-8') as f_1, open('2.txt', 'r', encoding='utf-8') as f_2, open('3.txt', 'r', encoding='utf-8') as f_3:

    x = str(len(f_1.readlines()))
    s = str(len(f_2.readlines()))
    w = str(len(f_3.readlines()))
    

    txt_dict[x] = nof_1, xx
    txt_dict[s] = nof_2, ss
    txt_dict[w] = nof_3, ww

    txt_list = sorted(txt_dict.items())
    
    with open('main.txt', 'wt', encoding='utf-8') as main_txt:
        for element in txt_list:
            for el in element:
                for l in el:
                    main_txt.writelines(l)
                    main_txt.write('\n')


    







        