# https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/killer-monsters-0b5cb283/

class Monsters():
    def __init__(self):
        self.monsters = []

    def push(self, monster):
        # lesson learnt dont update the same list in the loop on which it is dependent upon make a new list or it causes unexpected errors
        updated_monsters = []
        for existingMonster in self.monsters:
            if existingMonster <= monster:
                continue
            updated_monsters.append(existingMonster)
        updated_monsters.append(monster)
        self.monsters = updated_monsters
        return self.monsters

    def size(self):
        return len(self.monsters)


T = int(input("Enter number of test cases "))

while T > 0:
    N = int(input("Enter number of monsters "))
    monsterList = list(map(int, input("Enter all monsters ").split()))
    monsters = Monsters()
    output = []
    for monster in monsterList:

        monsters.push(monster)
        # print(monsters.monsters)
        output.append(monsters.size())
    print(*output)
    T -= 1
