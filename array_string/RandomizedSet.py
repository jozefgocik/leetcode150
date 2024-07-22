# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150

import random


class RandomizedSet(object):

    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val):
        result = val not in self.map
        if result:
            self.map[val] = len(self.list)
            self.list.append(val)

        return result

    def remove(self, val):
        result = val in self.map
        if result:
            indexToRemove = self.map[val]
            self.map.pop(val)

            lastValue = self.list[-1]
            self.list[indexToRemove] = self.list[-1]
            self.list.pop()

            if lastValue in self.map:
                self.map[lastValue] = indexToRemove

        return result

    def getRandom(self):
        return random.choice(self.list)
