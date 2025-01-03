# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

users = np.loadtxt('users_shop.txt', delimiter=',')

purchased = users[users[:, 1] == 1, 0]

users_hist, users_range = np.histogram(users[:, 0], bins=10, range=(20, 70))
users_range = users_range[:-1]
users_cat = dict(zip(users_range, users_hist))

purchases_hist, purchases_range = np.histogram(purchased, bins=10, range=(20, 70))
purchases_range = purchases_range[:-1]
purchases = dict(zip(purchases_range, purchases_hist))

plt.scatter(purchases_range, purchases_hist)

## Corelation & Covariance

np.corrcoef(purchases_hist, purchases_range)
np.cov(purchases_hist, purchases_range)


age_range = users_range[4]

## Simple Probability

Pa = users_cat[age_range] / users.shape[0] * 100
Pp = sum(purchases.values()) / users.shape[0] * 100


## Conditional Probability

Ppa = purchases[age_range] / users_cat[age_range] * 100
Pap = purchases[age_range] / sum(purchases.values()) * 100


