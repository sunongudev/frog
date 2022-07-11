

var_types=['string','char','int','float']

def var(inp,line_index=0):
    if inp!=None and '{' in inp:
        return inp
    var_type=''
    output=inp
    for i in var_types:
        if inp!=None and i in inp and inp.index(i)==0:
            var_type=i
            break
    before_assign_index=len(inp)-1
    try:
        before_assign_index=inp.index('=')-1
    except ValueError:
        pass
    var_name=inp[(len(var_type)+1):(before_assign_index+1)]
    if var_type:
        if var_type=='string':
            output='char '+var_name+'[256]'
            try:
                output+=inp[(before_assign_index+1):]
            except IndexError:
                pass
    else:
       return inp
    return output+';'


def constant(inp,line_index=0):
    try:
        k=inp.index('const ')
        if k==0:
            return 'const '+var(inp[6:],line_index=line_index)
    except ValueError:
        return inp


def array(inp,line_index=0):
    try:
        k=inp.index('array[')
        number_of_elements=0
        try:
            i=inp.index(']',k)
            str_number_of_elements=inp[(k+6):i]
            try:
                number_of_elements=int(str_number_of_elements)
            except ValueError:
                if str_number_of_elements:
                    print(f'In line {line_index}: Array Length is only assigned to int value.')
                    return '//'+inp
            if k==0:
                temp=var(inp[(i+1):],line_index=line_index)
                temp=temp[:-1] if temp[-1]==';' else temp
                return temp+f'[{number_of_elements}]'+';' if number_of_elements>0 else temp+'[];'
        except ValueError:
            print(f'In line {line_index}: \'[\' was never closed.')
            return '//'+inp
    except ValueError:
        return inp

