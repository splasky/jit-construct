#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Last modified: 2017-08-26 12:46:39
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
            loop = 1
            while loop > 0:
                self.pc += 1
                char = self.program[self.pc]
                if char == ']':
                    loop -= 1
                elif char == '[':
                    loop += 1

    def __jmp_forward(self):
        if self.stack[self.pointer] != 0:
            loop = 1
            while loop > 0:
                self.pc -= 1
                char = self.program[self.pc]
                if char == ']':
                    loop += 1
                elif char == '[':
                    loop -= 1

    def exec(self, program: list):
        try:
            self.pc = 0
            self.program = program
            while self.pc < len(self.program):
                char = self.program[self.pc]
                if char in self.__instructions:
                    self.__instructions[char]()
                self.pc += 1

        except Exception as e:
            print("Exception:{}".format(e))
            print("pc:{}".format(self.pc))
            print("char:{}".format(char))
            print("stack:\n{}".format(self.stack))
            print("program:\n{}".format(self.program))
            sys.exit(1)


def parse(program: list):
    return [x for x in program if x in Brainf_VirtualMachine.ByteCode]


def run(input_file: str)->None:
    with open(input_file, 'r') as f:
        program = parse(f.read())

    vm = Brainf_VirtualMachine()
    vm.exec(list(program))


if __name__ == "__main__":
    run(sys.argv[1])
