from os import system

system('cp ./* /usr/local/Cellar/frog@0.1/*')
system('rm -rf /usr/local/Cellar/frog@0.1/install*')
system('mv /usr/local/Cellar/frog@0.1/frog /usr/local/bin/')
