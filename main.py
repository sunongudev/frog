import ana,glob,os,sys
from lib import frog_current_version
homedir=os.path.expanduser('~')
os.system("mkdir -p ~/.cache/frog")
try:
    version=sys.argv[1] if sys.argv[1]=='-v' else ''
    print(f'Frog version {frog_current_version}.0')
    sys.exit()
except IndexError:
    pass

if os.listdir(homedir+'/.cache/frog'):
    print("Waiting for cleaning up cache...\n")
    os.system('rm -rf ~/.cache/frog/*')
    print("Cache has been cleaned up!")

print('Waiting for compile library...')
for i in glob.glob(f'/usr/local/lib/frog{frog_current_version}/site-packages/*.frog'):
    cpp_filename=f'/usr/local/lib/frog{frog_current_version}/cpp-library/'+os.path.basename(i)[:-4]+'cpp'
    if cpp_filename:
        pass
    else:
        with open(cpp_filename,'w') as f:
            with open(i,'r') as f2:
                f.write(ana.ana(f2.read()))
            f.flush()
print("=>All library has been compiled finished!\n")
from datetime import datetime
import time
try:
    current_time=time.time()
    theFile=sys.argv[1] if sys.argv[1]!='-o' else sys.argv[3]
    theFile=homedir+theFile.replace('~','') if '~' in theFile else theFile 
    theCppFile=homedir+'/.cache/frog/'+os.path.basename(theFile)[:-5]+'-'+datetime.now().strftime("%Y%m%d%H%M%S")+'.cpp'
    try:
        theOutputFile=sys.argv[2] if sys.argv[2]!='-o' else sys.argv[3]
    except IndexError:
        theOutputFile=theFile[:-5]
    try:
        with open(theFile,'r') as f:
            with open(theCppFile,'w') as f2:
                f2.write(ana.ana(f.read()))
                f2.flush()
        os.system(f'g++ -o{theOutputFile} {theCppFile}')
        losttime=round(time.time()-current_time,2)
        print(f"Compile finished in {losttime}s")
    except IOError:
        print(f'{theFile} not found.')
except IndexError:
    print(f"---Frog Version {frog_current_version}.0---")





