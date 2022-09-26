from funcoes import clean

def save_open():
    path = 'saved_preferences'
    with open(f'{path}.txt', encoding='iso-8859-1') as f:
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

def save_write(line_num, text):
    path = 'saved_preferences'
    lines = open(f'{path}.txt', 'r').readlines()
    lines[line_num] = str(text) + '\n'
    out = open(f'{path}.txt', 'w')
    out.writelines(lines)
    out.close()

def save_log(name,data):
    path = "log_output"
    with open(f'{path}/log_{name}.txt', 'w') as f:
        f.write(data)


