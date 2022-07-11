import os,ana
code='#include<iostream>\n'


#Current Version
frog_current_version='0.1'





#Manage library
def import_lib(inp,line_index=0):
    output=inp
    if 'import ' in inp:
        libname=inp[7:].replace('.','/')+'.frog'
        output="namespace "+inp[7:]+'{\n'
        try:
            with open('/usr/local/lib/frog'+frog_current_version+'/cpp-libary/'+libname[:-4]+'.cpp','r') as f:
                for line in f:
                    if output[0]=='#':
                        output=line+'\n'+output
                    else:
                        output+='\t'+line+'\n'
        except IOError:
            try:
                with open(libname,'r') as f:
                    while True:
                        line=f.readline()
                        if line==None:
                            break
                        output+='\t'+ana.single_ana(line,line_index)+'\n'
            except IOError:
                print(f"In line {line_index}: No libary named: "+inp[7:])
                return '//'+inp
    else:
        return inp
    return output +'}'


