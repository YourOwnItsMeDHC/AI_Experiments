def did_burglary(burglary):
    if burglary is True:
       return 0.01
    else:
       return 0.99

def did_earthquake(earthquake):
    if earthquake is True:
          return 0.02
    else:
        return 0.98

def did_alarm(burglary, earthquake, alarm):
    table = dict()
    table['ttt'] = 0.95
    table['ttf'] = 0.05
    table['tft'] = 0.94
    table['tff'] = 0.06
    table['ftt'] = 0.29
    table['ftf'] = 0.71
    table['fft'] = 0.001
    table['fff'] = 0.999
    key = ''
    key = key + 't' if burglary else key + 'f'
    key = key + 't' if earthquake else key + 'f'
    key = key + 't' if alarm else key + 'f'
    return table[key]

def did_santaCall(alarm, santaCalls):
     table = dict()
     table['tt'] = 0.9
     table['tf'] = 0.1
     table['ft'] = 0.05
     table['ff'] = 0.95
     key = ''
     key = key + 't' if alarm else key + 'f'
     key = key + 't' if santaCalls else key + 'f'
     return table[key]

def did_bantaCall(alarm, bantaCalls):
    table = dict()
    table['tt'] = 0.7
    table['tf'] = 0.3
    table['ft'] = 0.01
    table['ff'] = 0.99
    key = ''
    key = key + 't' if alarm else key + 'f'
    key = key + 't' if bantaCalls else key + 'f'
    return table[key]

if __name__ == '__main__':
 
    ask = bool(input("Hey Deepak Bro, I just wanna ask you a question, should I ? : "))     
    if ask is True:

        print()
        print()
        print("Ye raha aapka sawaal, aapke Computer isscrrreeen par 😁 : ")

        print()
        print()
        print("What is the probability that the alarm has sounded but neither a burglar nor an earthquake has occured and both santa and banta call ?")
        burglary = bool(input("Did burglary happened ? True or False: "))
        print()
        
        print("Probability of Burglary : ")
        print(did_burglary(burglary))

        earthquake = bool(input("Did earthquake come ? True or False: "))
        print("Probability of Earthquake : ")
        print(did_earthquake(earthquake))

        alarm = bool(input("Did alarm ring ? True or False: "))
        print("Probability of Alarm ringing : ")
        print(did_alarm(burglary, earthquake, alarm))

        santaCalls = bool(input("Deepak Bro 🤟😁, did Santa call you ? True or False: "))
        print("Probability of Santa calling : ")
        print(did_santaCall(alarm, santaCalls))

        bantaCalls = bool(input("Deepak Bro 🤟, did Banta call you ? True of False: "))
        print("Probability of Banta calling : ")
        print(did_bantaCall(alarm, bantaCalls))

        print()
        print()
        print("Probability of the above given query is : ")
        print(did_burglary(burglary) * did_earthquake(earthquake) * did_alarm(burglary, earthquake, alarm) * did_santaCall(alarm, santaCalls) * did_bantaCall(alarm, bantaCalls))

    else :

        print()
        print()
        print("Taa taa, Bye Bye 👋👋👋, Khatam")
        


    # P(santa ^ banta ^ alarm ^ ~burglar ^ ~earthquake) =
    # P(santa|alarm) * P(banta|alarm) * P(alarm| ~burglar, ~earthquake) * P(~burglar) * P(~earthquake)

    # print()
    # print()
    # print("What is the probability that Santa call ? ")
    # print((did_santaCall(True, True) *
    #        (did_alarm(True, True, True) * ((did_burglary(True)*did_earthquake(True)))) + 
    #        (did_alarm("", True, True) * ((did_burglary("")*did_earthquake(True)))) + 
    #        (did_alarm(True, "", True) * ((did_burglary(True)*did_earthquake("")))) + 
    #        (did_alarm("", "", True) * ((did_burglary("")*did_earthquake("")))))
    #        + 
    #        (did_santaCall("", True) *
    #        (did_alarm(True, True, "") * ((did_burglary(True)*did_earthquake(True)))) +
    #        (did_alarm("", True, "") * ((did_burglary("")*did_earthquake(True)))) +
    #        (did_alarm(True, "", "") * ((did_burglary(True)*did_earthquake("")))) + 
    #        (did_alarm("", "", "") * ((did_burglary("")*did_earthquake("")))))
           
    #        )

    # print(did_santaCall(True, True))

    # print(did_alarm(True, True, True) * ((did_burglary(True)* did_earthquake(True))))
    # print(did_alarm("", True, True) * ((did_burglary("")*did_earthquake(True)))) 
    # print(did_alarm(True, "", True) * ((did_burglary(True)* did_earthquake(""))))
    # print(did_alarm("", "", True) * ((did_burglary("")*did_earthquake(""))))

    # print(did_santaCall("", True))

    # print(did_alarm(True, True, "") * ((did_burglary(True)*did_earthquake(True))))
    # print(did_alarm("", True, "") * ((did_burglary("")*did_earthquake(True))))
    # print(did_alarm(True, "", "") * ((did_burglary(True)*did_earthquake(""))))
    # print(did_alarm("", "", "") * ((did_burglary("")*did_earthquake(""))))
    