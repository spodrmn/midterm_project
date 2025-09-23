#!/usr/bin/env python3

import random
import math
from ringbuffer import RingBuffer

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        '''
        # TO-DO: implement this
        self.capacity = math.ceil(44100/frequency) 
        self.buffer =   RingBuffer(self.capacity)
        self.tcount = 0

        for x in range(self.capacity):
            self.buffer.enqueue(0)

    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg
    

    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        for i in range(self.buffer.size()):
            self.buffer.dequeue()
            self.buffer.enqueue(random.uniform(-0.5,0.5))

    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        temp = self.buffer.peek()
        self.buffer.dequeue()
        temp = temp + self.buffer.peek()
        self.buffer.enqueue(temp/2*0.996)

        self.tcount +=1

    def sample(self) -> float:
        '''
        Return the current sample
        '''
        return self.buffer.peek()

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        return self.tcount
