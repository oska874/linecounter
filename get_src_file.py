# -*- coding: utf-8 -*- 

#usage:
#	get_src_file.py [r] dir 
# not support hidden file(.file)

import sys,os
import re
import count_lines

if __name__ == "__main__":
    argn=len(sys.argv)
    if argn < 2:
        print("usage:get_src_file.py [t]<t> <dir>")
        exit

# get filename
# check recurise walk dir
# select specific type files

    if sys.argv[1] != 't':
        print("parameters error")
        exit	
    else:		
        dst_dir = sys.argv[3]
        stype = sys.argv[2]

# check the given path is directory or source file
    if os.path.isdir(sys.argv[3]) != True:
        print("path error")
        exit

    fnames = os.walk(dst_dir)
    if stype == 'c'
        stype = '[cSh]'
    matchStr = '^(\S)*\.'+ stype + '$'
    stRe = re.compile(matchStr)

    hidedir = '^\.'
    hideRe = re.compile(hidedir)

    l1 = 0
    l2 = 0
    l3 = 0

    if stype == '[cSh]':
        stype = 'c'

    for fn in fnames:
        #print(fn)
        res = 0
        for name in fn[2]:
            if fn[1] == []:
                res = stRe.match(fn[0] + "/" + name)
            else:
                if os.path.isdir(fn[1][0]) and hideRe.match(fn[1][0]):
                    res = stRe.match(fn[0] +'/' +name)
            if res:
                print(res.group())
                if stype == 'c':
                    aa =count_lines.count_line1(res.group(), stype)
                    l1 += aa[0]
                    l2 += aa[1]
                    l3 += aa[2]
        
    print("source %d\ncomment %d\nempty %d\n" % (l1,l2,l3))
