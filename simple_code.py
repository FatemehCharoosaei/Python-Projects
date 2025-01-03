# -*- coding: utf-8 -*-



def show_students(names, scores):

    if type(names) != list:
        print ('error')
        return 0

    
    results = dict(zip(names, scores))
    for i in results:
        if int(results[i]) > 15:
            print ('Cong! Dear ' + i + ' your score is ' + str(results[i]))
        elif int(results[i]) <= 15 and int(results[i]) > 10:
            print ('Luckily! Dear ' + i + ' your score is ' + str(results[i]))
        else:
            print ('Sorry! Dear ' + i + ' your score is ' + str(results[i]))



scores = input('Enter you score list: ')
scores = scores.split(',')
names = input('Enter you name list: ')
names = names.split(',')

show_students(names, scores)


