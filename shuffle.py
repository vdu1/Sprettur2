from random import shuffle
nums = [4, 6, 8]
shuffle(nums)
print(nums)
x = ("Fílar Viktor hávaða?", "Nei")
print(x)
print(x[0])
spur = [('Viktor segir', 'Nei'),('Viktor', 'Ja')]
print(spur)
print(spur[0])
print(spur[0][0])
print(spur[0][1])
print(spur[1][0])
print(spur[1][1])
for spurning, rettsvar in spur:
    print('Spurningin er: ' + spurning + ' og svarid er ' + rettsvar)
