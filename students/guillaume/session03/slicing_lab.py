#!/usr/bin/env python3
def exch_first_last(seq):
    '''
    Exchange the first & last item of a sequence
    '''
    l = len(seq) - 1
    seq = (seq[-1:] + seq[1:l] + seq[0:1])
    return seq


def every_other_rem(seq):
    '''
    Print a sequence with every other item of the initial sequence
    '''
    l = len(seq)
    seq_ret = seq[0:1]
    for i in range(2, l, 2):
        seq_ret = seq_ret + seq[i:i + 1]
    return seq_ret


def first_last_in_bet(seq):
    '''
    return a sequence with the first and last 4 items removed,
    and every other item in between
    '''
    return every_other_rem(seq[4:len(seq) - 4])


def reverse_slic(seq):
    '''
    return a sequence reversed (just with slicing)
    '''
    l = len(seq)
    seq_ret = seq[l - 1:l]
    for i in range(l - 1, -1, -1):
        seq_ret = seq_ret + seq[i - 1:i]
    return seq_ret


def third(seq):
    '''
    return a sequence with the middle third, then last third,
    then the first third in the new order
    '''
    l = len(seq)
    if l % 3 == 0:
        third = l // 3
        new_seq = seq[third:2 * third] + seq[2 * third: ] + seq[0:third]
        return new_seq
    print('len of the sequence is not a multiple of 3')
    return None

if __name__ == '__main__':

    functions = [exch_first_last, every_other_rem, first_last_in_bet, reverse_slic, third]
    test_lst = ['', 'tesu', 'ab',''.join(map(str,list(range(10)))), [1,2,3], list(range(24)), list(range(9)),['1third', '2third', '3third'], []]

    for function in functions:
        print(repr(function.__name__))
        print(repr(function.__doc__))
        for seq in test_lst:
            print(seq)
            print(function(seq))
        print()
        
