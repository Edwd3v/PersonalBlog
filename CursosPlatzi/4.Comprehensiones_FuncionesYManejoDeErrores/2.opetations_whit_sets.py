def run():

    '''
    par_numbers = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    prime_numbers = {2, 3, 5, 7, 11, 13, 17}

    new_set = par_numbers.union(prime_numbers)
    print(new_set)

    other_numbers = {1, 9, 15, 19}
    new_set = new_set | other_numbers
    print(new_set)
    '''

    '''set_1 = {'c', 'o', 'm', 'i', 'd', 'a'}
    set_2 = {'c', 'o', 'r', 't', 'a', 'r'}

    intersection_set = set_1.intersection(set_2) 
    print(intersection_set)

    difference_set = set_1.difference(set_2)
    print(difference_set)'''

    '''set_x = {'Manzana', 'Pera', 'Papaya'}
    set_y = {'Manzana', 'Papaya', 'Uva', 'Mango'}

    set_difference_x_y = set_x.difference(set_y)
    print(set_difference_x_y) 
    
    set_difference_x_y = set_x - set_y
    print(set_difference_x_y)

    set_difference_y_x = set_y.difference(set_x)
    print(set_difference_y_x) 
        
    set_difference_y_x = set_y - set_x
    print(set_difference_y_x)'''

    set_x = {'Manzana', 'Pera', 'Papaya'}
    set_y = {'Manzana', 'Papaya', 'Uva', 'Mango'}

    set_symmetric_dif_y_x = set_y.symmetric_difference(set_x)
    print(set_symmetric_dif_y_x) # => {'Uva', 'Mango', 'Pera'}

    set_symmetric_dif_x_y = set_x.symmetric_difference(set_y)
    print(set_symmetric_dif_x_y)  

    set_symmetric_dif_x_y = set_x ^ set_y
    print(set_symmetric_dif_x_y) # => {'Uva', 'Mango', 'Pera'}


if __name__ == '__main__':
    run()