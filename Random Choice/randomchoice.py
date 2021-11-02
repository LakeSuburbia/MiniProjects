from random import seed, choice
CHOICES = list(map(lambda x: x[:-1], open('choices.txt', 'r').readlines()))
seed(a=None, version=2)
print(choice(CHOICES))
