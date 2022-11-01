stmnt = True
score = 0
while stmnt == True:

    import random
    from random import randint
    #low = list(f'{range(1,11)}')
    low = ['1','2','3','4','5','6','7','8','9','10']
    big = ['25','50','75','100']
    nob = int(input("How many big numbers: ")) #number of big
    lob = random.sample(big,nob) #length of big
    lol = random.sample(low,(6-nob)) #length of low
    numbers = [*lol,*lob]
    print(numbers)

    operators = ['+','-','*','/']

    #recursions = random.randint(1,6)
    #for i in range(recursions):
    #    numbersinuse = random.sample(numbers,2)
     #   operator = random.sample(operators,1)
      #  numbersinuse[0] operator numbersinuse[1]
        
    #tokenizing
    #make a list consisting of number operator number operator etc..

    numans = 0
    def create_number():
        maths = []
        clone_numbers = numbers.copy()
        for i in range(5):
            n = random.choice(clone_numbers)
            maths.append(n)
            clone_numbers.remove(n)
            o = random.choice(operators)
            maths.append(o)
        maths.append(clone_numbers[0])
        maths.insert(0,'(((((')
        maths.insert(4, ')')
        maths.insert(7,')')
        maths.insert(10,')')
        maths.insert(13,')')
        maths.insert(16,')')
        
        #global ans
        ans = ""
        ans = ans.join(maths)
        global numans
        numans = eval(ans)
        
        return ans, numans


    while type(numans) != int or numans < 100 or numans > 999:
        ans, numans = create_number()
        if type(numans) == int and numans > 100 and numans < 1000:
            print(numans)
            #print(ans)
            
    
    def get_number():
        global score
        gnumber = input('Input method of calculation - brackets are very important:')
        check = eval(gnumber)
        cn = check-numans
        cn = abs(cn)
        if check == numans:
            print('Correct')
            score += 10
            print(score)
        elif cn < 9:
            print(f'Close, you were {cn} off the target')
            score += 9-cn
            print(f' Your score is {score}')

    get_number()
    ply_agn = input('Would you like to play again? (yes/no) ')
    ply_agn.lower()
    if ply_agn == 'yes':
        create_number()
    else:
        stmnt = False       
        
    
    

        


    




