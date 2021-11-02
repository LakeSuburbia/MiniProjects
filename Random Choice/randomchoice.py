import random
CHOICES = list(map(lambda x: x[:-1], open('choices.txt', 'r').readlines()))
random.seed(a=None, version=2)
print(random.choice(CHOICES))
