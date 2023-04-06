#!/usr/bin/env python3


class Topic:
    def __init__(self, name, deadline):
        self.deadline = deadline
        self.name = name
        self.done = list()
        self.left = list()

        self.left.append(self.name)

        def finished_topic(self):
            self.left.remove(self.name)


class Subject:
    def __init__(self, name):
        self.all = dict()
        self.name = name

    def add_to_subject(self, name, deadline):
        if name not in self.all.keys:
            new_topic = Topic(name, deadline)
            self.all.update({self.name: new_topic})
            return 'Added'
        else:
            return 'Already here?!?'
