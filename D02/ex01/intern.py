#!/usr/bin/env python3
# -*-coding:utf-8 -*-

class Intern(object):
    """docstring for Intern."""

    def __init__(self, name = "My name ? I'm nobody, an intern, i have no Name "):
        super(Intern, self).__init__()
        self.Name = name

    def __str__(self):
        return self.Name

    class Coffee():
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise  Exception("I'm just an intern i can do that")

    def make_coffee(self):
        return self.Coffee()

if __name__ == '__main__':
    frst = Intern()
    print(frst)
    scd = Intern("Mark")
    print(scd)
    print(scd.make_coffee())
    try:
        print(frst.work())
    except Exception as e:
        print(e)
