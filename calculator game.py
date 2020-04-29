from random import *
from time import *

global c_right,c_left,left,right,user,c_right_caption,c_left_caption,left_caption,right_caption,dictionary,move

c_right,c_left,right,left=1,1,1,1
c_right_caption,c_left_caption,right_caption,left_caption='','','',''
user=''
move=''
dictionary={0:0,1:1,2:2,3:3,4:4,5:5,6:1,7:2,8:3,9:4}



def display():
    print'-'*13
    print'COMPUTER'
    print'-'*13
    print'RIGHT'+'\t'+'LEFT'
    print str(c_right)+'\t'+str(c_left)
    print str(c_right_caption)+'\t'+str(c_left_caption)
    print str(left_caption)+'\t'+str(right_caption)
    print str(left)+'\t'+str(right)
    print'LEFT'+'\t'+'RIGHT'
    print'-'*13
    print user
    print'-'*13
    print move

def instructions():
    print'''
    INSTRUCTIONS
    ============
    
    Simple calculator game, rules are as usual.
    Gameplay is through text. eg; left to right, shuffle 3:2
    While shuffling mention ratio.
    
    '''

def check_elimination():
    global c_right,c_left,left,right,user,c_right_caption,c_left_caption,left_caption,right_caption,dictionary,move
    if 5 in [c_left,c_right,left,right]:
        if c_left==5:
            c_left_caption='eliminated'
            c_left=0
        elif c_right==5:
            c_right_caption='eliminated'
            c_right=0
        elif left==5:
            left_caption='eliminated'
            left=0
        elif right==5:
            right_caption='eliminated'
            right=0
        
    else:
        pass
def eliminator():
    global c_right,c_left,left,right,user,c_right_caption,c_left_caption,left_caption,right_caption,dictionary,move
    if c_left==0 and c_right==0:
        return 'Computer eliminated.\nYou won!'
    elif left==0 and right==0:
        return str(user)+' eliminated.\nComputer won.\nYou lose.'
    else:
        return ''

def player_shuffle(x):
    global c_right,c_left,left,right,user,c_right_caption,c_left_caption,left_caption,right_caption,dictionary,move
    if int((str(x).split(':'))[0])+int((str(x).split(':'))[1])!=left + right:
        4/0
              
    p=left
    q=right
    left=dictionary[int((str(x).split(':'))[0])]
    right=dictionary[int((str(x).split(':'))[1])]
    
    if p==left or q==right:
        
        4/0

        
def attack():
    global c_right,c_left,left,right,user,c_right_caption,c_left_caption,left_caption,right_caption,dictionary,move
    if c_left+left==5 or c_left+right==5 or c_right+right==5 or c_right+left==5:
        return 'possible'
    else:
        return 'notpossible'

def proceed():
    global c_right,c_left,left,right,user,c_right_caption,c_left_caption,left_caption,right_caption,dictionary,move
    a=[1,2,3,4]
    for we in range(101):
        print'k0'
        b=a[randint(0,1)]
        c=a[randint(2,3)]
        if (b==1 and c_right!=0) or (b==2 and c_left!=0):
            print b,c
            break
    else:
        if c_right!=0:
            b=1
            c=3
        elif c_left!=0:
            b=2
            c=4
    if b==1 and c==3:
        left=dictionary[left+c_right]
        move='c_right->left'
        print 'k1'
    elif b==1 and c==4:
        right=dictionary[right+c_right]
        move='c_right->right'
        print'k2'
    elif b==2 and c==3:
        left=dictionary[left+c_left]
        move='c_left->left'
        print 'k3'
    elif b==2 and c==4:
        right=dictionary[right+c_left]
        move='c_left->right'
        print'k4'
    
    print'k'
    #print b,c

def shuffle():
    global c_right,c_left,left,right,user,c_right_caption,c_left_caption,left_caption,right_caption,dictionary,move
    
    a=5-right
    b=5-left
    total=c_left+c_right
    d=str(c_right)+':'+str(c_left)
    sd=0
    for ss in range(101):
        sd+=1
        c=randint(0,4)
        if (total-c!=5) and ((c not in[a,b]) and (total-c not in[a,b])) and (dictionary[c] not in [c_left]) and (total-c>=0) and (dictionary[total-c] not in [c_right]):
            break
    else:
        proceed()
    if sd<100:
        c_left=dictionary[c]
        c_right=dictionary[total-c]
        move=d+' -> '+str(c_right)+':'+str(c_left)
        print 'j'
    


def play():
    global c_right,c_left,left,right,user,c_right_caption,c_left_caption,left_caption,right_caption,dictionary,move
    flag=''
    a=c_right+left
    b=c_right+right
    c=c_left+left
    d=c_left+right
    for e in [a,b,c,d]:
        if e+c_left==5 or e+c_right==5:
            flag='out kore debe'
            break
    else:
        flag='thik ache no problem'

    if flag=='thik ache no problem':
        proceed()
    elif flag=='out kore debe':
        shuffle()
        
def player_hand(x):
    global c_right,c_left,left,right,user,c_right_caption,c_left_caption,left_caption,right_caption,dictionary,move
    if 'shuffle' in x:
        a=x.split()
        for b in a:
            if ':' in b:
                a=b
        a=str(a)
        
        player_shuffle(a)
        return 'done'
    elif 'to' in x:
        a=x.split('to')
        b=a[0]
        c=a[1]
        if 'left' in b and 'left' in c:
            c_left=dictionary[c_left+left]
        elif 'left' in b and 'right' in c:
            c_right=dictionary[c_right+left]
        elif 'right' in b and 'right' in c:
            c_right=dictionary[c_right+right]
        elif 'right' in b and 'left' in c:
            c_left=dictionary[c_left+right]
        return 'done'
    else:
        return ''
        
        
################################################################################################


print'''
CALCULATOR GAME
===============

@ tamojitdas
____________
'''

while True:
    print
    print'''
    MENU
    ====

    1. New Game
    2. Instructions
    3. Exit

    <enter serial num to access>
    '''
    
    while True:
        try:
            a=input('>>> ')
            if a in [1,2,3]:
                break
        except:
            print'\n<enter valid serial number.>'
            print

    if a==1:
        c_right,c_left,right,left=1,1,1,1
        c_right_caption,c_left_caption,right_caption,left_caption='','','',''
        user=''
        move=''

        print
        user=raw_input('Enter Your Name - ').title()
        move=''
        print
        useless_counter=0
        bb=raw_input('Do you want to start first ? (y/n)').lower()
        if bb=='y':
            useless_counter=1
        else:
            useless_counter=2
        
        while True:
            print
            display()
            print

            check_elimination()
            c=eliminator()
            if c!='':
                
                print
                print 'RESULT : \n',c
                sleep(4)
                break

            if useless_counter%2!=0:
                
                while True:
                    try:
                        
                        move=''
                        c_right_caption,c_left_caption,right_caption,left_caption='','','',''
                        sleep(1)
                        b=raw_input('>>> ').lower()
                        print
                        c=player_hand(b)
                        if c=='':
                            print'\n<not a valid move.>\n'
                        elif c=='done':
                        #useless_counter+=1
                            break
                    except:
                        print'\n<not a vvalid move.>\n'

            elif useless_counter%2==0:
                print
                print"COMPUTER'S TURN"
                print 'Thinking....'
                sleep(2)
                b=attack()
                if b=='possible':
                    
                    if c_left+left==5:
                        left=left+c_left
                        move='c_left->left'
                    elif c_left+right==5:
                        right=right+c_left
                        move='c_left->right'
                    elif c_right+left==5:
                        left=left+c_right
                        move='c_right->left'
                    elif c_right+right==5:
                        right=right+c_right
                        move='c_right->right'

                    #check_elimination()
                    #c=eliminator()
                    #useless_counter+=1
                        
                        
                    

                elif b=='notpossible':
                    print
                    
                    play()
                    print
                    #useless_counter+=1
            
         
            useless_counter+=1
            check_elimination()
            c=eliminator()
            if c!='':
                display()
                
                print
                print 'RESULT : '
                print c
                sleep(4)
                break
    



    elif a==2:
        print
        instructions()
        print
        raw_input('<= BACK')



    elif a==3:
        print'\n====END===='
        raw_input()
        quit()
        









    
