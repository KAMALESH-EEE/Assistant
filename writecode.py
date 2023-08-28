cod=[]
indentation = ''

def code_line(com):
    global indentation, cod
    words = com.split(' ')
    str =''
    str += indentation
    if words[0] == 'get':
            str += 'input()'
    elif words[0] == 'show':
            str +='print('
            for i in words:
                if i == 'show': continue
                str+=i+' '
            str +=')'
    else:
        for word in words:
            if word == 'of':
                str += '('
            elif word == '_':
                str += ' '
            elif word == 'fo':
                str +=')'
            elif word == 'let':
                pass
            elif word == 'is':
                str+='='
            elif word == 'pluse':
                str +='+'
            elif word == 'minus':
                str += '-'
            elif word == 'mul':
                str += '-'
            elif word == 'product':
                str += '-'
            elif word == 'isbig':
                str += '>'
            elif word == 'issmall':
                str += '<'
            else:
                str += word
    str+='\n'
    #print(str)
    cod.append(str)
    if ':' in str:
        indentation+='\t'


def get_code():
    global indentation,cod
    command = input("C: ")
    if command == 'end':
        return 
    elif command == 'getin':
        indentation+='\t'
    elif command == 'getout':
        indentation = indentation[0:len(indentation)-4]
    elif command == 'del_line':
        cod.pop()
    elif command == 'kaatu':
        for i in cod:
            print(i,end="")
    else:
        code_line(command)
    
    get_code()

#name = input("code name:")
#name+='.py'
get_code()
fil = open ('Assistant/mycode.py','w')
fil.writelines(cod)

fil.close()

print ("**********************************")
print ("*  RUNNING YOUR CODE  *")
print ("**********************************")
print('\n')

import mycode