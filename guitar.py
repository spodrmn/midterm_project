#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    keylist = list(r'q2we4r5ty7u8i9op-[=]')
    stringlist = []

    for i in range(20):
        stringlist.append(GuitarString(440*1.059463**(i-12)))
        

    CONCERT_A = 440
    CONCERT_C = CONCERT_A * (1.059463**3)
    string_A = GuitarString(CONCERT_A)
    string_C = GuitarString(CONCERT_C)

    n_iters = 0
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        sample = 0

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            for j in range(len(keylist)):
                if key == keylist[j]:
                    stringlist[j].pluck()
                    
            
        # compute the superposition of samples

        sample = sum(string.sample() for string in stringlist)

        # play the sample on standard audio

        play_sample(sample)
    
        # advance the simulation of each guitar string by one step

        for string in stringlist: 
            string.tick()