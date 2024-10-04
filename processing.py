import random
import re

def validate_roll(roll):
    roll = roll.replace(' ','')
    roll = roll.lower()

    if '+-' not in roll:
        roll = roll.replace('-','+-')

    splitroll = re.split('d|\+', roll)


    digitsonly = all(x.isnumeric() for x in [x.lstrip('-') for x in splitroll])

    if (len(splitroll) == 2 or len(splitroll) == 3) and digitsonly:
        return True
    else:
        return False

def gbtable(results):
    tabletotal = 0
    for result in results:
        if result >1:
            if result <=5:
                tabletotal = tabletotal + 1
            elif result <=9:
                tabletotal = tabletotal + 2
            else:
                tabletotal = tabletotal + 4
    return(tabletotal)

def modify(results, mod):
    modvalues = []
    newresults = results
    for i in range(0, len(results) ) :
        newresults[i] = newresults[i] + mod
        modvalues.append(gbtable(newresults))
        newresults[i] = newresults[i] - mod
    #print(f'modified results {modvalues}')
    return(max(modvalues))


def rolldice(roll, multiple, target):

    roll = roll.replace(' ','')
    roll = roll.lower()

    if '+-' not in roll:
        roll = roll.replace('-','+-')

    splitroll = re.split('d|\+', roll)


    if splitroll[0] == '':
        numdice = 1
    else:
        numdice = int(splitroll[0])

    sides = int(splitroll[1])

    modifier = 0
    if len(splitroll) == 3:
        modifier = int(splitroll[2])

    output = ''

    sresults = random.choices(population = range(1,sides+1), k=numdice)

    ttotal2 = modify(sresults, modifier)
    stotal = sum(sresults) + modifier

    if multiple == False:
        if sides not in [2,3,4,6,8,10,12,20]:
            output= f'NONSTANDARD ROLL = {numdice}d{sides}+{modifier} <br/> <br/>'
        else:
            output = f'Roll = {numdice}d{sides}+{modifier} <br/> <br/>'

        output = output + f'table damage = <b>{ttotal2}</b> <br/> <br/>'
        output = output + f'die results = {sresults} <br/> <br/>'
        output = output + f'straight damage = {stotal} <br/> <br/>'

    elif target ==1:
        if sides not in [2,3,4,6,8,10,12,20]:
            output = f'NONSTANDARD ROLL = {numdice}d{sides}+{modifier} <br/><br/>Target {target}:   table {ttotal2}  straight {stotal} <br/><br/>'
        else:
            output = f'Roll = {numdice}d{sides}+{modifier} <br/><br/>Target {target}:   table {ttotal2}  straight {stotal} <br/><br/>'

    else:
        output = output + f'Target {target}:   table {ttotal2}  straight {stotal} <br/><br/>'

    return(output)
