opCodes={'add':'00000','sub':'00001','mov':['00010', '00011'],'ld':'00100','st':'00101','mul':'00110','div':'00111','rs':'01000','ls':'01001','xor':'01010','or':'01011',
         'and':'00110','not':'01101','cmp':'01110','jmp':'01111','jlt':'11100','jgt':'11101','je':'11111','hlt':'11010'}
registers={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}
var_num=0
var_dict={}
labels={}

f1=open('sample.txt','r')
l=f1.readlines()
l1=[]
for i in l:
    if i!='\n' and i.find(':')== -1:
        l1.append(i.strip().split())
    elif i.find(':') != -1 and i!='\n':
        labels[i[:i.find(':')]]=l.index(i)
        l1.append((i[i.find(':')+1:]).strip().split())

#writing binary of supported instructions
with open('binary.txt','w') as f2:
    for i in l1:
        if len(i)==1:
            try: l[l.index(i[0])+1]
            except IndexError: 
                string=opCodes[i[0]]+'00000000000'
                f2.write(string)
            else:
                print('Syntax Error')
                #need to clear the binary.txt
        if len(i)==2:
            if i[0]=='var':    #variable handling
                var_num+=1
                code=f'{var_num:07b}'
                var_dict[i[2]]=code
            elif i[0] in ['jmp','jlt','jgt','je']:
                string=opCodes[i[0]]+'0000'+f'{(labels[i[1]]):07b}'
        elif len(i)==4:
            string=opCodes[i[0]]+'00'+registers[i[1]]+registers[i[2]]+registers[i[3]]+'\n'
            f2.write(string)
        elif len(i)==3:
            if i[0]=='mov':
                if i[2][0]=='R':
                    string=opCodes[i[0]][1]+'00000'+registers[i[1]]+registers[i[2]]+'\n'
                    f2.write(string)
                else:
                    string=opCodes[i[0]][0]+'0'+registers[i[1]]+f'{int(i[2][1:]):07b}'+'\n'
                    f2.write(string)
            else:
                if i[0] in ['div','not','cmp']:
                    string=opCodes[i[0]]+'00000'+registers[i[1]]+registers[i[2]]+'\n'
                    f2.write(string)
                else:
                    if i[0] in ['ls','rs']:
                        string=opCodes[i[0]]+'0'+registers[i[1]]+f'{int(i[2][1:]):07b}'+'\n'
                    # elif i[0] in ['ld','st']:
            
#handling labels


f1.close()


