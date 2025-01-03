# -*- coding: utf-8 -*-


import numpy as np
import random
from matplotlib import pyplot as plt

random.seed(0)

#totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
#purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
#
#totalPurchases = 0
#
#for _ in range(100000):
#    ageDecade = random.choice(totals.keys())
#    purchaseProbability = ageDecade / 100.0
#    totals[ageDecade] +=1
#    if (random.random() < purchaseProbability):
#        totalPurchases += 1
#        purchases[ageDecade] += 1
    
count = 100000
users_age = np.random.randint(20, 70, count)
users_purchased = []

totalPurchases = 0

for age in users_age:
    
    purchaseProbability = age / 100.0
    if (random.random() < purchaseProbability):
        users_purchased.append(True)
    else:
        users_purchased.append(False)

users = np.zeros((count, 2))
users[:, 0] = users_age
users[:, 1] = users_purchased

#plt.scatter(scores_table[:, 0], scores_table[:, 1])
#plt.show()

np.savetxt('users_shop.txt', users, fmt='%2.2f', delimiter=',')

