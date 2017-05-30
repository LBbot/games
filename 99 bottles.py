def bottlesong(before):
    after = (before - 1)
    if before == 2:
        print("{} bottles of beer on the wall, {} bottles of beer. Take one down and pass it around, {} bottle of beer "
               "on the wall.\n".format(before, before, after))
        before -= 1
        return bottlesong(before)
    if before == 1:
        print("{} bottle of beer on the wall, {} bottle of beer. Take one down and pass it around, No more bottles of "
               "beer on the wall.\n".format(before, before, after))
        before = 99
        print("Go to the store and buy some more, {} bottles of beer on the wall.".format(before))
    else:
        print("{} bottles of beer on the wall, {} bottles of beer. Take one down and pass it around, {} bottles of beer"
               " on the wall.\n".format(before, before, after))
        before -= 1
        return bottlesong(before)

bottlesong(99)

def sing(b, end):
    print(b or 'No more', 'bottle' + ('s' if b - 1 else ''), end)


for i in range(99, 0, -1):
    sing(i, 'of beer on the wall,')
    sing(i, 'of beer,')
    print('Take one down, pass it around,')
    sing(i - 1, 'of beer on the wall.\n')
