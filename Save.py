from LeituraDados import clean

def save_open():
    with open('saved_preferences.txt', encoding='iso-8859-1') as f:
        lines = f.readlines()
    list_lines = list(lines)

    ini = clean(list_lines[1])
    fim = clean(list_lines[3])
    point = clean(list_lines[5])
    stp = clean(list_lines[7])
    dts = (list_lines[9])
    lab = (list_lines[11])
    vaz = (list_lines[13])
    fiber_lenght = clean(list_lines[15])
    p_status = clean(list_lines[17])


    return ini,fim,point,stp,dts,lab,vaz,fiber_lenght,p_status

print(save_open())

def save_write(line_num, text):
    lines = open('saved_preferences.txt', 'r').readlines()
    lines[line_num] = str(text) + '\n'
    out = open('saved_preferences.txt', 'w')
    out.writelines(lines)
    out.close()


