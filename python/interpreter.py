#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-08-27 22:38:10
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
        self.pointer += 1
        if len(self.stack) <= self.pointer:
            self.stack.append(0)

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

    def program_exec(self, program):
        self.pc = 0
        self.bracket_map, self.program = self.parse(program)
        while self.pc < len(self.program):
            char = self.program[self.pc]
            if char in self.__instructions:
                self.__instructions[char]()
            self.pc += 1

    def parse(self, program: list):
        program_list = [
            x for x in program if x in Brainf_VirtualMachine.ByteCode]

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
        return 1

    with open(argv[1], 'r') as f:
        program = f.read()

    vm = Brainf_VirtualMachine()
    vm.program_exec(list(program))
    return 0


def entry_point(argv):
    run(argv)
    return 0


def target(*args):
    return entry_point


if __name__ == "__main__":
    run(sys.argv)
