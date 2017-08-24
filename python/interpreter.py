#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-08-24 13:03:53
import sys


class Brainf_VirtualMachine(object):

    def __init__(self):
        self.__instructions = {
            '>': self.advance,
            '<': self.devance,
            '+': self.inc,
            '-': self.dec,
            '.': self.put,
            ',': self.get,
            '[': self.jmp_forward,
            ']': self.jmp_backward,
        }

        self.stack = []
        self.pointer = 0

    def advance(self, pointer):
        return pointer += 1

    def devance(self, pointer):
        return pointer -= 1

    def inc(self, pointer):
        self.stack[pointer] += 1
        return pointer

    def dec(self, pointer):
        self.stack[pointer] -= 1
        return pointer

    def put(self, pointer):
        print(ord(self.stack[pointer]))
        return pointer

    def get(self, pointer):
        self.stack[pointer] = input()
        return pointer

    def jmp_backward(self):
        pos = self.pointer

    def exec(self, program):
        pointer = 0
        while pointer < len(program):
            char = program[pointer]
            if char in self.__instructions:
                pointer = self.__instructions[pointer]()
            elif:
                raise Exception("instruction: " + char + " is not instruction.")


def run(input_file: str)->None:
    with open(input_file, 'r') as f:
        program = f.read()


if __name__ == "__main__":
    run(sys.argv[1])
