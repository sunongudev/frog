

def i(inp,line_index=0):
    try:
        k=inp.index('input(')
        varname='varinput1911h03m44d10july'
        if k==1:
            print(f"In line {line_index}: No variable assigned to input.")
            return '//'+inp
        elif k>1:
            varname=inp[:(k-1)]
            return 'char '+varname+'[256];\nstd::cout<<'+inp[(k+6):-1]+';\nstd::cin>>'+varname+';'
    except ValueError:
        return inp

def o(inp,line_index=0):
    try:
        k=inp.index('print(')
        if k==0:
            return 'std::cout<<'+inp[6:-1].replace(',"\\n"','<<std::endl')+';'
        elif k>=1 and inp[k-1]=='=':
            print(f'In line {line_index}: Print function no return any value.')
            return '//'+inp
    except ValueError:
        return inp
