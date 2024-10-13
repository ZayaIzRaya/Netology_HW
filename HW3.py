# #Задание 1
#
# word = 'testing'
# dlina=len(word)
# if dlina%2==0:
#     print(word[int(dlina/2-1):int(dlina/2+1)])
# else:
#     print(word[int(dlina/2)])
# t
#
# #Задание 2
#
# import copy
# i=0
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# if len(boys)!=len(girls):
#     print('Внимание, кто-то может остаться без пары!')
# else:
#     boys_sorted=sorted(boys)
#     girls_sorted=sorted(girls)
#     print('Идеальные пары:')
#     while i < len(boys_sorted):
#         print(boys_sorted[i],'и',girls_sorted[i] )
#         i=i+1
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha