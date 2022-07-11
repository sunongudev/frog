import lib,ios,var

#isContinuedToLoad=True
def split_line(inp):
    return inp.split('\n')

def single_ana(inp,line_index=0):
    output=inp
    if inp!=None:
        output=lib.import_lib(inp,line_index) if output==inp else output
        output=ios.i(output,line_index) if output==inp else output
        output=ios.o(output,line_index) if output==inp else output
        output=var.var(output,line_index) if output==inp else output
        output=var.constant(output,line_index) if output==inp else output
        output=var.array(output,line_index) if output==inp else output
        output=output+';' if 'return' in output else output
        k=0
        while True:
            k=output.find('#',k)
            if k==-1:
                break
            elif output.count('"',0,k)%2==0:
                output=output[:k]+'//'+output[(k+1):]
    return output

def ana(inp,include=lib.code):
    demo=split_line(inp)
    for i in range(0,len(demo)):
        demo[i]=single_ana(demo[i].strip(),i)
    return include+'\n'.join([i for i in demo if i!=None]) if demo!=None else None 
