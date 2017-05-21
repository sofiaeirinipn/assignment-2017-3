import sys
import random
v =int(sys.argv[1])

def element_check():
    i = 0
    element=0
    element = random.choice(cereal)
    for x in D:
        for k in x:
            if element == k:
                i += 1

    if i < (v-1)/2 :
        return element
    else:
        return element_check()

D = []
CD = v*(v-1)/6
while CD>0:
    i=0
    cereal= [x for x in range( 1, v+1)]
    random_element = element_check()
    cereal.pop(cereal.index(random_element))
    first_pair = random.choice(cereal)
    cereal.pop(cereal.index(first_pair))
    second_pair = random.choice(cereal)
    for sinolo in D:
        if ((random_element in sinolo) and (first_pair in sinolo)) or ((random_element in sinolo ) and (second_pair in sinolo)):
            i +=1

        while i > 0:
            i=0
            cereal= [x for x in range( 1, v+1)]
            cereal.pop(cereal.index(random_element))
            first_pair = random.choice(cereal)
            cereal.pop(cereal.index(first_pair))
            second_pair = random.choice(cereal)
            for sinolo in D:
                if ((random_element in sinolo) and (first_pair in sinolo)) or ((random_element in sinolo ) and (second_pair in sinolo)):
                    i +=1

    for sinolo in D:
        if first_pair in sinolo and second_pair in sinolo:
            D.pop(D.index(sinolo))
            CD += 1

    elements =(random_element, first_pair, second_pair)
    D.append(tuple(sorted(elements)))
    CD -=  1

print(sorted(D))
print(len(D))
