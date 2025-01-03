# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt

scores = np.loadtxt('students_scores.txt', delimiter=',')

final_scores = np.mean(scores[:, 0:1], axis=1) + scores[:, 2]
final_scores[final_scores > 20] = 20

final_scores = final_scores.reshape(140, 1)

scores_all = np.concatenate((scores, final_scores), axis=1)

var_values = np.var(scores_all, axis=0)
mean_values = np.mean(scores_all, axis=0)
median_values = np.median(scores_all, axis=0)


hist_info1 = np.histogram(scores_all[:, 3], bins=10)

#hist_info2 = plt.hist(scores_all[:, 3], bins=10)


plt.figure(figsize=(6,10))
plt.subplots_adjust(hspace=.5)

plt.subplot(3,1,1)
hist_info2 = plt.hist(scores_all[:, 0], bins=10, color=(.3, .7, .2), alpha=.5)
plt.title('first_scores')
plt.grid(True)

plt.subplot(3,1,2)
hist_info2 = plt.hist(scores_all[:, 1], bins=10)
plt.title('second_scores')

plt.subplot(3,1,3)
hist_info2 = plt.hist(scores_all[:, 3], bins=10)
plt.title('final_scores')


plt.figure(figsize=(6,6))
plt.scatter(scores_all[:, 0], scores_all[:, 3], s=50, color=(.7, .5, .3) ,alpha=.5)

plt.xlabel('First Scores')
plt.ylabel('Final Scores')


plt.figure(figsize=(6,6))
plt.scatter(scores_all[:, 3], scores_all[:, 2], s=50, color=(.5, .2, .8) ,alpha=.5, marker='^')


plt.figure(figsize=(6,6))
plt.boxplot(scores_all, patch_artist=True)
plt.grid()

plt.show()
