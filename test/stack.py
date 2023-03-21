#!/usr/bin/env python3

stack = []


def push(element):
    stack.append(element)


def pop():
    if len(stack) == 0:
        return "Stack is Empty"
    else:
        return stack.pop()


def display():
    return l[::-1]
