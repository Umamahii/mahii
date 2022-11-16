# def reverse_while_loop(s):
    # s1 = ''
    # length = len(s) - 1
    # while length >= 0:
        # s1 = s1 + s[length]
        # length = length - 1
    # return s1

# input_str = 'ABç∂EF'

# if __name__ == "__main__":
    # print('Reverse String using while loop =', reverse_while_loop(input_str))
# ##  
# def reverse_join_reversed_iter(s):
    # s1 = ''.join(reversed(s))
    # return s1

-m timeit --number 100000 --unit usec 'import string_reverse' 'string_reverse.reverse_slicing("ABç∂EF"*10)'

def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)