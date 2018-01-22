yours = ['Purdue', 'Yale', 'Harvard']
mine =['Ohio', 'Michigan', 'NYU']

ours1 =yours + mine

ours2 = []
ours2.append(yours)
ours2.append(mine)

print(ours1)
print(ours2)
#ours1 is a list with elements in each of yours and mine; while ours2 is a list with elements of the list yours and the
# list mine.

yours[0] = 'IU'
print(ours1)
print(ours2)
#ours1 did not change because ours1 is a new list created by combining the original two lists and changing the original
#lists would not change the newly created list that exists by its own. However, ours2 is created by appending yours and mine,
#if the one of the original lists changes, the appended list, ours2, will also change.

