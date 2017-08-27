#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-08-27 16:46:24
import sys


class Brainf_VirtualMachine(object):
    ByteCode = {'>', '<', '+', '-', '.', ',', '[', ']'}

    def __init__(self):
        self.__instructions = {
            '>': self.__advance,
            '<': self.__devance,
            '+': self.__inc,
            '-': self.__dec,
            '.': self.__put,
            ',': self.__get,
            '[': self.__jmp_backward,
            ']': self.__jmp_forward,
        }

        self.stack = [0]
        self.pointer = 0
        self.pc = 0
        self.program = []
        self.bracket_map = {}

    def __advance(self):
        self.stack.append(0)
        self.pointer += 1

    def __devance(self):
        self.pointer -= 1

    def __inc(self):
        self.stack[self.pointer] += 1

    def __dec(self):
        self.stack[self.pointer] -= 1

    def __put(self):
        sys.stdout.write(chr(self.stack[self.pointer]))

    def __get(self):
        self.stack[self.pointer] = ord(sys.stdin.read(1))

    def __jmp_backward(self):
        if self.stack[self.pointer] == 0:
            self.pc = self.bracket_map.get(self.pc)

    def __jmp_forward(self):
        if self.stack[self.pointer] != 0:
            self.pc = self.bracket_map.get(self.pc)

    def exec(self, program: list):
        try:
            self.pc = 0
            self.bracket_map, self.program = self.parse(program)
            while self.pc < len(self.program):
                char = self.program[self.pc]
                if char in self.__instructions:
                    self.__instructions[char]()
                self.pc += 1

        except Exception as e:
            print(e)
            sys.exit(1)

    def parse(self, program: list):
        program_list = [x for x in program if x in Brainf_VirtualMachine.ByteCode]

        pc = 0
        leftstack = []
        bracket_map = {}

        for char in program_list:
            if char == '[':
                leftstack.append(pc)
            elif char == ']':
                left = leftstack.pop()
                right = pc
                bracket_map[left] = right
                bracket_map[right] = left
            pc += 1

        return bracket_map, program_list


def run(argv):
    if len(argv) < 1:
        print("Please supply a filename")
        sys.exit(1)

    with open(argv[1], 'r') as f:
        program = f.read()

    vm = Brainf_VirtualMachine()
    vm.exec(list(program))


if __name__ == "__main__":
    run(sys.argv)
