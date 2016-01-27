# -*- coding: utf-8 -*- 

#usage: 
#	count_lines.py filename
#       count lines of source file

import sys,os

def count_line1(fna,stype):
    fd1 = open(fna,'r')
    if stype == 'c':
        ret  = divide_lines(fd1,'c')
        print(ret)
        ret1 = divide_lines(fd1,'S')
        print(ret1)
        ret2 = divide_lines(fd1,'h')
        print(ret2)
        ret3 = divide_lines(fd1,'cpp')
        print(ret3)
        fd1.close()
        i=0
        a0=ret[i]+ret1[i] +ret2[i] +ret3[i]
        i=1
        a1=ret[i]+ret1[i] +ret2[i] +ret3[i]
        i=2
        a2=ret[i]+ret1[i] +ret2[i] +ret3[i]
        print(a0,a1,a2)
        return (a0,a1,a2)
    else:
        ret4 = divide_lines(fd1,stype)
        fd1.close()

    return ret4

def divide_lines(fd,ft):
    l1 = 0 # source
    l2 = 0 # comment
    l3 = 0 # empty

    multi_comment = 0
    print("ft "+ft)
    if ft == 'c' or ft == 'cpp' or ft == 'S' or ft == 'h':
        for line in fd:
# strips space in line start and end 
            line = line.strip()
            if len(line) >= 1:
                if multi_comment == 0:
                    # comment line start from "/*" or single line comment "//"
                    if len(line) >= 2 and line[0] == '/' and line[1] == '*':
                        l2 += 1
                        multi_comment = 0
                    elif len(line) >= 2 and line[0] == '/' and line[1] == '/':
                        l2 += 1
                    else :
                        # source line
                        l1 += 1
                elif multi_comment == 1:
                    # comment line till meet "*/"
                    l2 += 1
                    if len(line) >= 2 and line[-2] == '*' and line[-1] == '/':
                        multi_comment = 0
            else :
                # empty line
                l3 += 1
    elif ft == 'py':
        for line in fd:
            line = line.strip()
            if len(line) > 1:
                if multi_comment == 0:
                    if line[0] == '#':
                        l2 += 1
                    elif len(line) == 3 and line[0] == '"' and line[1] == '"' and line[2] == '"':#multiline comment detection should be refacted
                        l2 += 1
                        multi_comment = 1
                    else:
                        l1 += 1
                elif multi_comment == 1:
                    if len(line) == 3 and line[0] == '"' and line[1] == '"' and line[2] == '"':
                        l2 += 1
                        multi_comment = 0
                    else:
                        l2 += 1
	    else:
		l3 += 1
    else:
        print("not supported files "+ft)

    #print(l1,l2,l3)
    return (l1,l2,l3)

if __name__ == "__main__":
    argn = len(sys.argv)
    if argn < 4:
        print("usage:python count_lines.py [t]<t> <filename>")
        exit

    #get filename
    filename = sys.argv[3]
    print("source file: "+filename)
    stype = sys.argv[2]
    aa = count_line1(filename,stype)
    print("source %d\ncomment %d\nempty %d\n" % aa)
